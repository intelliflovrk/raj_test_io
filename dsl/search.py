from selenium.common.exceptions import TimeoutException
from ioffice.admin.admin import AdministrationPage
from ioffice.admin.manageusers.user.base import BaseUserPage
from ioffice.clients.client_dashboard import ClientDashboardPage, BaseClientPage
from ioffice.admin.manageusers.user.userssearch import UsersSearchPage
from ioffice.base import IOBasePage
from ioffice.client_search import ClientSearch
from utils import *


class Search:

    def __init__(self, config):
        self.config = config

    @retry(TimeoutException)
    def search_and_open_first_link(self):
        ClientSearch(self.config).click_full_search_button().click_open_first_link()

    @retry(TimeoutException)
    def search_and_open_first_fee(self):
        ClientSearch(self.config).click_fee_search_button().click_open_first_fee_link()

    @retry(TimeoutException)
    def search_client_by_name_and_open_first_result(self):
        ClientSearch(self.config).click_search_button().click_open_first_client()


class SearchFee:

    def __init__(self, config):
        self.config = config

    def open_fee(self):
        data = get_common_data(self.config)["test_data"]["fee_search_data"]
        fee = get_temp_data(self.config, "fee")
        IOBasePage(self.config).level1_menu() \
            .hover_over_navigation_menu() \
            .click_adviserworkplace()
        ClientSearch(self.config).click_clear_button()\
            .select_search_option(data["fee_search"]) \
            .select_reference_type(data["fee_iob_ref"]) \
            .fill_in_reference(fee["sequentialRef"])
        Search(self.config).search_and_open_first_fee()
        return self


class SearchPlan:

    def __init__(self, config):
        self.config = config

    def open_plan(self, plan_ref):
        data = get_common_data(self.config)["test_data"]["client_search_data"]
        IOBasePage(self.config).level1_menu() \
            .hover_over_navigation_menu() \
            .click_adviserworkplace()
        ClientSearch(self.config).select_search_option(data["full_search"]) \
            .select_reference_type(data["plan_iob_ref"]) \
            .clear_reference() \
            .clear_firstname() \
            .clear_lastname() \
            .fill_in_reference(plan_ref)
        Search(self.config).search_and_open_first_link()
        return self

    def open_sub_plan(self):
        data = get_common_data(self.config)["test_data"]["client_search_data"]
        IOBasePage(self.config).level1_menu() \
            .hover_over_navigation_menu() \
            .click_adviserworkplace()
        ClientSearch(self.config).select_search_option(data["full_search"]) \
            .select_reference_type(data["plan_iob_ref"]) \
            .clear_reference() \
            .clear_firstname() \
            .clear_lastname() \
            .fill_in_reference("IOB" + self.config.sub_plan_id)
        Search(self.config).search_and_open_first_link()
        return self

    def open_plan_by_url(self, *args):
        """Non-keyword arguments:
        args[0] -- client id
        args[1] -- plan id
        """
        if args:
            open_url_path(self, f"/nio/plan/{args[0]}/SummaryPlan/{args[1]}/")
        else:
            open_url_path(self, f"/nio/plan/{get_temp_data(self.config, 'client')['id']}/SummaryPlan/{get_temp_data(self.config, 'plan')['id']}/")
        return self


class SearchTask:

    def __init__(self, config):
        self.config = config

    def open_task_by_url(self, *args):
        if args:
            open_url_path(self, f"/nio/OrganiserClient/{args[0]}/ViewClientActivity/{args[1]}/")
        else:
            open_url_path(self, f"/nio/OrganiserClient/{get_temp_data(self.config, 'client')['id']}/ViewClientActivity/{get_temp_data(self.config, 'task')['organiserActivityId']}/")
        return self


class SearchUser:

    def __init__(self, config):
        self.config = config
        self.page = {}

    def navigate_to_manage_users(self):
        ClientDashboardPage(self.config).level1_menu().hover_over_navigation_menu().click_administration()
        AdministrationPage(self.config).level2_menu().click_manage_users()
        assert UsersSearchPage(self.config).is_title_matches(), "Title does not match the Users page"
        return self

    def find_user(self):
        users = UsersSearchPage(self.config)
        users.click_clear().fill_in_username(self.config.username).click_search()
        users.open_first_result()
        self.config.user_id = BaseUserPage(self.config).get_user_id()
        return self


class QuickClientSearch:
    def __init__(self, config):
        self.config = config

    def quick_search_client(self, client_name):
        IOBasePage(self.config).fill_in_client_search_field(client_name)\
            .click_go_button()
        return self

    def save_client_id(self):
        client_id = BaseClientPage(self.config).get_client_id()
        add_temp_data(self.config, "client", {"id": client_id})
        return self


class SearchClient(QuickClientSearch):

    def open_client_by_url(self, *client_id):
        if client_id:
            open_url_path(self, f"/nio/clientDashboard/{client_id[0]}/dashboard/0")
        else:
            open_url_path(self, f"/nio/clientDashboard/{get_temp_data(self.config, 'client')['id']}/dashboard/0")
        return self

    def open_created_client_by_search(self):
        created_client = get_temp_data(self.config, "client")["person"]
        self.search_client_by_name(created_client["firstName"], created_client["lastName"])
        return self

    def search_client_by_name(self, first_name, last_name):
        IOBasePage(self.config).level1_menu() \
            .hover_over_navigation_menu() \
            .click_adviserworkplace()
        ClientSearch(self.config) \
            .select_search_option(get_common_data(self.config)["test_data"]["client_search_data"]["clients_by_name"]) \
            .click_clear_button() \
            .fill_in_firstname(first_name)\
            .fill_in_lastname(last_name)
        Search(self.config).search_client_by_name_and_open_first_result()
        return self


class SearchLead:

    def open_created_lead_by_url(self, *lead_id):
        if lead_id:
            open_url_path(self, f"/nio/leads/{lead_id[0]}/viewlead")
        else:
            open_url_path(self, f"/nio/leads/{self.config.variables['temp_data']['lead'][0]['externalReference'].split('-')[1]}/viewlead")
        return self
