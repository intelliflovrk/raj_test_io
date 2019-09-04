import shutil
import sys
import tempfile
import urllib
import pytest
import os
import platform
import requests
import werkzeug
from pytest_html import extras
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from sauceclient import SauceClient
import re
from selenium.common.exceptions import UnexpectedAlertPresentException
import utils
from py._xmlgen import html
import datetime
import time
import json
import logging


TEST_NAME = re.compile('(?P<name>test.*?)(\[.*])', re.IGNORECASE)
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
log = logging.getLogger()


def pytest_addoption(parser):
    parser.addoption("-U", "--username", help="Username")
    parser.addoption("-P", "--password", help="Password")
    parser.addoption("-C", "--client_id", help="OAuth client id")
    parser.addoption("-S", "--client_secret", help="OAuth client secret")
    parser.addoption("-K", "--api_key", help="API key")
    parser.addoption("-D", "--domain",
                     help="Domain and protocol i.e. https://abc.com",
                     default='https://www.intelligent-office.net')
    parser.addoption("-B", "--browsertype",
                     help="Browser type. Available values: chrome, firefox, edge, ie, saucelabs",
                     default="chrome")
    parser.addoption("-E", "--env",
                     help="Environment eg: prd-10, uat-10, tst-01, tst-02 etc. Domains will be derived from this",
                     default='prd-10')
    parser.addoption("-T", "--tdata",
                     help="New value in env_data.json e.g. -T=common_data.api_data.create_client.tst-02.person.firstName."
                          "MyFirstName" "If not provided the env_data.json is used")


def pytest_generate_tests(metafunc):
    env = "prd-10"
    if metafunc.config.option.env is not None:
        env = metafunc.config.option.env
    if 'env' in metafunc.fixturenames:
        metafunc.parametrize("env", [env])

    if 'username' in metafunc.fixturenames:
        if metafunc.config.option.username is not None:
            metafunc.parametrize("username", [metafunc.config.option.username])
        else:
            metafunc.parametrize("username", [
                metafunc.config._variables["environments"][env]["data"]["users"]["default"]["username"]])

    if 'password' in metafunc.fixturenames:
        if metafunc.config.option.password is not None:
            metafunc.parametrize("password", [metafunc.config.option.password])
        else:
            metafunc.parametrize("password", [
                metafunc.config._variables["environments"][env]["data"]["users"]["default"]["password"]])

    if 'domain' in metafunc.fixturenames and metafunc.config.option.domain is not None:
        metafunc.parametrize('domain', [metafunc.config.option.domain])
    if 'browsertype' in metafunc.fixturenames and metafunc.config.option.browsertype is not None:
        metafunc.parametrize("browsertype", [metafunc.config.option.browsertype])
    if 'client_id' in metafunc.fixturenames and metafunc.config.option.client_id is not None:
        metafunc.parametrize("client_id", [metafunc.config.option.client_id])
    if 'client_secret' in metafunc.fixturenames and metafunc.config.option.client_secret is not None:
        metafunc.parametrize("client_secret", [metafunc.config.option.client_secret])
    if 'scopes' in metafunc.fixturenames and metafunc.config.option.scopes is not None:
        metafunc.parametrize("scopes", [metafunc.config.option.scopes])
    if 'api_key' in metafunc.fixturenames and metafunc.config.option.api_key is not None:
        metafunc.parametrize("api_key", [metafunc.config.option.api_key])
    if type(metafunc.config.option.tdata) == str:
        user_test_data = metafunc.config.option.tdata.split(".")
        utils.update_json(metafunc.config._variables, user_test_data[:-1], user_test_data[-1])


def pytest_namespace():
    return {'ui_config': None}


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.test_name = get_test_name(item)
    report.test_area = get_test_area(item)
    cfg = pytest.ui_config
    add_timestamp_to_report(item, call, report)
    add_test_markers_to_report(item, report)
    add_test_markers_to_json_report(report)
    add_screenshots_to_report(report, TEST_NAME, cfg, item)
    add_test_details_to_report(report, cfg)
    add_pytest_logs(cfg, report)
    if cfg:
        quit_driver(cfg, report)


def add_test_markers_to_report(item, report):
    report.test_markers = set()
    markers_list = getattr(item, 'own_markers', [])
    markers_list.extend(getattr(item.parent, 'own_markers', []))
    for marker in markers_list:
        if marker.name not in ['usefixtures', 'parametrize', 'skip', 'skipif', 'io_all', 'first', 'last']:
            report.test_markers.add(marker.name)


def add_test_markers_to_json_report(report):
    if hasattr(report, 'test_markers') and report.when == 'setup':
        markers_list = list(report.test_markers)
        report.test_metadata = json.dumps(markers_list)
    elif hasattr(report, 'test_markers') is False:
        report.test_metadata = ''


def get_test_name(item):
    return re.search(r'(?P<area>test.*)(.py::)(?P<name>test.*?)(\[.*])', item.nodeid).group('name')


def get_test_area(item):
    return re.search(r'(?P<area>test.*)(.py::)(?P<name>test.*?)(\[.*])', item.nodeid).group('area')


def add_test_details_to_report(report, cfg):
    extra = getattr(report, 'extra', [])
    extra.append(extras.html(getattr(cfg, 'worker', '') + " " + getattr(cfg, 'username', '')))
    report.extra = extra


def add_pytest_logs(cfg, report):
    sys.stdout.flush()
    if report.when == 'setup':
        log.info(f"Setup completed: {report.test_name}|{getattr(cfg, 'worker', '')}|{' '.join(report.test_markers)}")


def add_timestamp_to_report(item, call, report):
    report.start = datetime.datetime.strptime(time.ctime(call.start), "%a %b %d %H:%M:%S %Y").strftime('%H:%M:%S')
    report.stop = datetime.datetime.strptime(time.ctime(call.stop), "%a %b %d %H:%M:%S %Y").strftime('%H:%M:%S')
    item.user_properties.append(report.start)
    item.user_properties.append(report.stop)
    report.user_properties = item.user_properties


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.pop(1)
    cells.insert(1, html.th('Area', class_='sortable'))
    cells.insert(2, html.th('Name', class_='sortable'))
    cells.insert(3, html.th('Markers', col='markers'))
    cells.insert(4, html.th('Setup Start', col='timestamp', class_='sortable'))
    cells.insert(5, html.th('Start', col='timestamp', class_='sortable'))
    cells.insert(6, html.th('End ', col='timestamp', class_='sortable'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.pop(1)
    cells.insert(1, html.td(report.test_area))
    cells.insert(2, html.td(report.test_name))
    cells.insert(3, html.td(' '.join(report.test_markers)))
    cells.insert(4, html.td(report.user_properties[0], class_='col-timestamp'))
    cells.insert(5, html.td(report.start, class_='col-timestamp'))
    cells.insert(6, html.td(report.stop, class_='col-timestamp'))
    cells.pop()


@pytest.fixture(scope='function')
def config(browsertype, variables, username, password, domain, env, file=None):
    """ Creates a webdriver browser instance """

    temp_dir = tempfile.TemporaryDirectory(None, None, utils.get_system_download_folder())
    temp_download_folder = temp_dir.name

    if 'chrome' in browsertype:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1200")
        options.add_argument("start-maximized")
        options.add_experimental_option("prefs", {"download.default_directory": temp_download_folder})
        browser_instance = webdriver.Chrome(options=options)

    elif 'firefox' in browsertype:
        options = webdriver.FirefoxOptions()
        browser_instance = webdriver.Firefox(firefox_options=options)
        browser_instance.maximize_window()

    elif 'ie' in browsertype:
        browser_instance = webdriver.Ie()
        browser_instance.maximize_window()

    elif 'edge' in browsertype:  # Edge is very slow and all steps will throw a timeout error.
        browser_instance = webdriver.Edge()
        browser_instance.maximize_window()

    else:
        browser_name = variables['browser']['name']
        browser_version = variables['browser']['version']
        platform = "{} {}".format(variables['os']['name'], variables['os']['version'])
        desired_cap = {
            'browserName': browser_name,
            'version': browser_version,
            'platform': platform,
            'tags': ["login", "IO"],
            'build': "1.2.3.4"
        }
        browser_instance = webdriver.Remote(
            command_executor="http://{}:{}@ondemand.saucelabs.com:80/wd/hub".format(variables['saucelabs']['username'],
                                                                                    variables['saucelabs']['password']),
            desired_capabilities=desired_cap)

    cfg = BaseConfig()
    domains = {} if not env else DomainResolver(variables).get_domains(env)

    cfg.driver = browser_instance
    cfg.username = username
    cfg.password = password
    if os.environ.get("PYTEST_XDIST_WORKER") is not None:
        io_field = os.environ.get("IO_FIELD").split("/")
        cfg.username = io_field[0]
        cfg.password = io_field[1]
        cfg.worker = os.environ.get("PYTEST_XDIST_WORKER")
        if ('temp_data' in variables) is False:
            if len(io_field) == 3:
                utils.update_json(variables, ["common_data", "clients", "default", "lastname"],
                                  variables["common_data"]["clients"]["default"]["lastname"] + io_field[2])
            elif re.match("automationuser(?P<user_number>\d)\w{3}\d*", cfg.username):
                automation_client_to_use = re.match("automationuser(?P<user_number>\d)\w{3}\d*", cfg.username).group('user_number')
                utils.update_json(variables, ["common_data", "clients", "default", "lastname"],
                                  variables["common_data"]["clients"]["default"]["lastname"] + automation_client_to_use)
            else:
                raise Exception("Please provide a default client to use.")
            
    if env:
        cfg.domain = domains["io"]
    elif domain:
        cfg.domain = domain
    cfg.env = env

    # Obtain token through internal credentials
    internal_api_data = variables["environments"][env]["data"]["api_data"]
    cfg.internal_token_client_id = internal_api_data["client_id"]
    cfg.internal_token_client_secret = internal_api_data["client_secret"]
    cfg.internal_token_scopes = internal_api_data["scopes"]

    # Obtain token through app credentials (Tenant Client Credentials)
    api_data = variables["environments"][env]["data"]["app"]
    cfg.token_client_id = api_data["tenant_client_credential_client_id"]
    cfg.token_client_secret = api_data["tenant_client_credential_client_secret"]
    cfg.token_scopes = api_data["tenant_client_credential_scopes"]

    cfg.domains = domains
    cfg.variables = variables
    cfg.variables.update({"temp_data": {}})
    cfg.temp_download_folder = temp_download_folder

    pytest.ui_config = cfg

    yield cfg

    if 'saucelabs' in browsertype:
        sauce_client = SauceClient(variables['saucelabs']['username'],
                                   variables['saucelabs']['password'])
        sauce_client.jobs.update_job(
            browser_instance.session_id, name='IO Login Tests(s)', passed=True)


class BaseConfig(object):
    driver = None
    access_token = None
    token_client_id = None
    token_client_secret = None
    token_scopes = None
    api_key = None
    username = None
    password = None
    domain = None
    env = None
    domains = None
    variables = {}

    def get_data(self):
        return {**self.variables["environments"][self.env]["data"], **self.variables["common_data"]}

    def get_io_domain(self):
        if "io" in self.domains:
            return self.domains["io"]
        else:
            return self.domain

    def get_devhub_domain(self):
        return self.domains["devhub"]

    def get_pfp_domain(self):
        return self.domains["pfp"]

    def get(self, path, domain, **kwargs):
        args = self._merge_headers(kwargs, self.get_api_headers())
        return requests.get(werkzeug.urls.url_fix(u"{0}{1}".format(self.get_ms_domain(domain), path)), **args)

    def post(self, path, domain, **kwargs):
        args = self._merge_headers(kwargs, {**self.get_api_headers(), **{"Content-Type": "application/json"}})
        return requests.post("{0}{1}".format(self.get_ms_domain(domain), path), **args)

    def put(self, path, domain, **kwargs):
        args = self._merge_headers(kwargs, {**self.get_api_headers(), **{"Content-Type": "application/json"}})
        return requests.put("{0}{1}".format(self.get_ms_domain(domain), path), **args)

    def patch(self, path, domain, **kwargs):
        args = self._merge_headers(kwargs, {**self.get_api_headers(), **{"Content-Type": "application/json"}})
        return requests.patch("{0}{1}".format(self.get_ms_domain(domain), path), **args)

    def delete(self, path, domain, **kwargs):
        args = self._merge_headers(kwargs, self.get_api_headers())
        return requests.delete("{0}{1}".format(self.get_ms_domain(domain), path), **args)

    def _merge_headers(self, args1, headers):
        if not args1: args1 = {}
        if "headers" in args1:
            args1["headers"] = dict(headers + args1["headers"])
        else:
            args1["headers"] = headers
        return args1

    def get_api_headers(self):
        if not self.access_token:
            self.get_access_token_for_tcc_flow()
        auth_value = "Bearer {0}".format(self.access_token)
        return {"Accept": "application/json", "Authorization": auth_value, "x-api-key": self.api_key}

    def get_api_data(self, data):
        return self.variables["common_data"]["api_data"][data][self.env]

    def get_ms_domain(self, service):
        return DomainResolver(self.variables).get_ms_domain(self.env, service)

    def get_identity_domain(self):
        return self.domains["identity"]

    def get_access_token_using_internal_credentials(self, new=True):
        if not new:
            return self.access_token
        tenant_id = re.findall("[0-9]{5}(?![0-9])(?!.*[0-9]{5})",
                               utils.get_user_by_type(self, "default")["username"])
        resp = requests.post("{0}/core/connect/token".format(self.get_identity_domain()),
                             auth=HTTPBasicAuth(
                                 self.variables["environments"][self.env]["data"]["api_data"]["client_id"],
                                 self.variables["environments"][self.env]["data"]["api_data"][
                                     "client_secret"]),
                             headers={'content-type': 'application/x-www-form-urlencoded',
                                      "cache-control": "no-cache"},
                             data="grant_type=tenant_client_credentials&scope={0}&tenant_id={1}".format(
                                 self.variables["environments"][self.env]["data"]["api_data"]["scopes"],
                                 str(tenant_id[0])))
        json = resp.json()
        self.access_token = json["access_token"]
        return self.access_token

    def get_access_token_for_tcc_flow(self, new=True):
        if not new:
            return self.access_token
        tenant_id = re.findall("[0-9]{5}(?![0-9])(?!.*[0-9]{5})",
                               utils.get_user_by_type(self, "default")["username"])
        resp = requests.post("{0}/core/connect/token".format(self.get_identity_domain()),
                             auth=HTTPBasicAuth(self.token_client_id, self.token_client_secret),
                             headers={'content-type': 'application/x-www-form-urlencoded',
                                      "cache-control": "no-cache"},
                             data="grant_type=tenant_client_credentials&scope={0}&tenant_id={1}".format(
                                 self.token_scopes, str(tenant_id[0])))
        json = resp.json()
        self.access_token = json["access_token"]
        return self.access_token

    def get_app_tcc_token(self, app):
        tenant_id = utils.get_automation_tenant_id(self)
        app = utils.get_app_by_type(self, app)
        resp = requests.post("{0}/core/connect/token".format(self.get_identity_domain()),
                             auth=HTTPBasicAuth(app["tenant_client_credential_client_id"], app["tenant_client_credential_client_secret"]),
                             headers={'content-type': 'application/x-www-form-urlencoded',
                                      "cache-control": "no-cache"},
                             data="grant_type=tenant_client_credentials&scope={0}&tenant_id={1}".
                             format(app["tenant_client_credential_scopes"], tenant_id))
        return resp.json()["access_token"]

    def get_access_token_for_resource_owner_flow(self):
        resp = requests.post("{0}/core/connect/token".format(self.get_identity_domain()),
                             headers={'content-type': 'application/x-www-form-urlencoded',
                                      "cache-control": "no-cache"},
                             data="grant_type=password&username={0}&password={1}"
                                  "&client_id={2}&scope={3}&client_secret={4}"
                             .format(self.username, self.password,
                                     self.variables["environments"][self.env]["data"]["app"][
                                         "resource_owner_client_id"],
                                     self.variables["environments"][self.env]["data"]["app"][
                                         "resource_owner_scopes"],
                                     urllib.parse.quote_plus(
                                         self.variables["environments"][self.env]["data"]["app"][
                                             "resource_owner_client_secret"])))
        json = resp.json()
        self.access_token = json["access_token"]
        return self.access_token


def add_screenshots_to_report(report, TEST_NAME, cfg, item):
    add_screenshot_for(report, TEST_NAME, cfg, item, "setup")
    add_screenshot_for(report, TEST_NAME, cfg, item, "call")
    add_screenshot_for(report, TEST_NAME, cfg, item, "teardown")


def add_screenshot_for(report, TEST_NAME, cfg, item, type):
    if report.when == type and report.outcome == 'failed' and (cfg is not None):
        test_name = TEST_NAME.search(item.name).group('name')
        print("Saving screenshot for failed test: {0}".format(test_name))
        try:
            create_screenshot_and_add_to_report(test_name, report)
        except UnexpectedAlertPresentException:
            alert = cfg.driver.switch_to_alert()
            alert.accept()
            create_screenshot_and_add_to_report(test_name, report)


def create_screenshot_and_add_to_report(test_name, report):
    if pytest.ui_config.driver:
        image_name = '{0}_{1}.png'.format(test_name, datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        pytest.ui_config.driver.save_screenshot(image_name)
    try:
        create_ui_tests_folder()
    except FileExistsError:
        pass
    try:
        move_screenshots_into_ui_tests(report, image_name)
    except:
        pass


def create_ui_tests_folder():
    if platform.system() == "Windows":
        os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "\\ui_tests\\")
    elif platform.system() == "Linux":
        os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "/ui_tests/")


def move_screenshots_into_ui_tests(report, image_name):
    if image_name:
        if platform.system() == "Windows":
            shutil.move(os.path.abspath(image_name), os.path.dirname(os.path.abspath(__file__)) + "\\ui_tests\\")
            report.extra = [extras.image(os.path.dirname(os.path.abspath(__file__)) + "\\ui_tests\\" + image_name)]
        elif platform.system() == "Linux" and os.environ.get("JENKINS_URL"):
            shutil.move(os.path.abspath(image_name), os.path.dirname(os.path.abspath(__file__)) + "/ui_tests/")
            report.extra = [extras.image(os.environ.get("BUILD_URL") + "artifact/ui_tests/" + image_name)]
        elif platform.system() == "Linux" and not os.environ.get("JENKINS_URL"):
            shutil.move(os.path.abspath(image_name), os.path.dirname(os.path.abspath(__file__)) + "/ui_tests/")
            report.extra = [extras.image(os.path.dirname(os.path.abspath(__file__)) + "/ui_tests/" + image_name)]


def quit_driver(cfg, report):
    if cfg.driver:
        if report.when == 'teardown' and (cfg is not None):
            cfg.driver.quit()
            pytest.ui_config.driver = None


class DomainResolver(object):

    def __init__(self, variables):
        self.DOMAINS = variables["environments"]

    def get_domains(self, env):
        if not env: return {}
        if env in ["prd-10", "uat-10"]:
            return self.DOMAINS[env]["domains"]
        if env.startswith("tst"):
            tst_domains = self.DOMAINS["tst"]["domains"]
            for key, value in tst_domains.items():
                if key == "ms-api":
                    continue
                else:
                    tst_domains[key] = value.format(env)
            return tst_domains
        else:
            raise Exception("Unknown env (" + str(env) + "), unable to resolve domain")

    def get_ms_domain(self, env, service):
        if "tst" in env:
            return self.get_domains(env)["ms-api"].format(env + "-" + service)
        else:
            return self.get_domains(env)["ms-api"].format(service)