import os
import platform
import PyPDF2
import json
import fakedata
import time
from functools import wraps
import requests
from docx import Document
import csv


# <editor-fold desc="files_and_folders">


def open_docx_file(file_name):
    return Document(file_name)


def read_csv_file(csvfile):
    return csv.reader(csvfile)


def remove_file(self, file):
    if os.path.exists(file):
        os.remove(file)
    else:
        print("The file does not exist")
    return self


def get_test_documents_file_url(file_name):
    url = get_project_url()
    if platform.system() == "Windows":
        return url + "\\" + "test_documents" + "\\" + file_name
    elif platform.system() == "Linux":
        return url + "/" + "test_documents" + "/" + file_name
    else:
        print("The current OS is not supported.")


def get_pdf_outline(self, file_name):
    file = open_downloaded_file(self, file_name)
    pdfreader = PyPDF2.PdfFileReader(file)
    self.pdf_outline = pdfreader.outlines
    file.close()
    return self


def make_file_name_unique(file_name):
    file_name, extension = file_name.split(".")
    return file_name + fakedata.rand_int(5) + "." + extension


def open_downloaded_file(self, file_name, mode='rb'):
    if platform.system() == "Windows":
        file = open(get_download_folder(self.config) + f"\\{file_name}", mode)
        return file
    elif platform.system() == "Linux":
        file = open(get_download_folder(self.config) + f"/{file_name}", mode)
        return file
    else:
        print("The current OS is not supported.")


def get_file_path(config, file_name):
    if platform.system() == "Windows":
        file = get_download_folder(config) + "\\{}".format(file_name)
    elif platform.system() == "Linux":
        file = get_download_folder(config) + "/{}".format(file_name)
    else:
        print("The current OS is not supported.")
    return file


def get_project_url():
    return os.path.dirname(os.path.abspath(__file__))


def get_vars_file_url(file_name):
    if platform.system() == "Windows":
        return get_project_url() + "\\" + "vars" + "\\" + file_name
    elif platform.system() == "Linux":
        return get_project_url() + "/" + "vars" + "/" + file_name
    else:
        print("The current OS is not supported.")


def get_download_folder(config):
    return config.temp_download_folder


def get_text_from_docx_section(document, xpath_to_section):
    return document.element.xpath(xpath_to_section)


def get_files_in_folder(folder):
    return os.listdir(folder)


def verify_file_is_downloaded(url, file_name):
    file = None
    if platform.system() == "Windows":
        file = open(url + "\\" + file_name)
    elif platform.system() == "Linux":
        file = open(url + "/" + file_name)
    else:
        print("The current OS is not supported.")
    file.close()


def send_file_to_element(self, locator, file_url):
    return self.driver.find_element_by_id(locator).send_keys(file_url)


if os.name == 'nt':
    import ctypes
    from ctypes import windll, wintypes
    from uuid import UUID


    class GUID(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", wintypes.BYTE * 8)
        ]

        def __init__(self, uuidstr):
            uuid = UUID(uuidstr)
            ctypes.Structure.__init__(self)
            self.Data1, self.Data2, self.Data3, \
            self.Data4[0], self.Data4[1], rest = uuid.fields
            for i in range(2, 8):
                self.Data4[i] = rest >> (8 - i - 1) * 8 & 0xff


    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(GUID), wintypes.DWORD,
        wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
    ]


    def _get_known_folder_path(uuidstr):
        pathptr = ctypes.c_wchar_p()
        guid = GUID(uuidstr)
        if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
            raise ctypes.WinError()
        return pathptr.value


    FOLDERID_Download = '{374DE290-123F-4565-9164-39C4925E467B}'


    def get_system_download_folder():
        return _get_known_folder_path(FOLDERID_Download)
else:
    def get_system_download_folder():
        home = os.path.expanduser("~")
        return os.path.join(home, "Downloads")


# </editor-fold>


# <editor-fold desc="data">

def is_string_present(dataset, string):
    result = False
    for item in dataset:
        if string in item:
            result = True
    return result


def update_json(json, keys, new_value):
    for key, value in json.items():
        if keys[0] in key:
            if keys[0] in json and isinstance(value, dict) == False:
                json.update({keys[0]: new_value})
                break
            update_json(value, keys[1:], new_value)


def get_json_data_for_parameters(test_name):
    with open(get_vars_file_url("common_data.json"))as f:
        data = json.load(f)
    return data[test_name]


def get_common_data(config):
    return config.variables["common_data"]


def get_api_test_data(self, data_type):
    data = str(get_api_data(self, data_type))
    return data.replace("'", "\"")


def get_api_data(self, data):
    return self.variables["common_data"]["api_data"][data][self.env]


def get_adviser_id_by_name(list, config):
    adv = config.variables["common_data"]["advisers"]["default"]
    adv_name = adv["firstname"] + " " + adv["lastname"]
    for element in list:
        if element["name"] in adv_name:
            return element["user"]["id"]


def get_client_name(what_config, type):
    return what_config.config.variables["common_data"]["test_data"]["add_basic_client_details"][type]


def get_user_by_type(self, user_type):
    return self.variables["environments"][self.env]["data"]["users"][user_type]


def get_app_by_type(self, app_type):
    return self.variables["environments"][self.env]["data"]["apps"][app_type]


def get_automation_tenant_id(self):
    return self.variables["environments"][self.env]["data"]["tenant"]["id"]


def find_active_model_by_code(model_list, code):
    active_model = None
    for model in model_list:
        if model["code"] == code and model["isActive"] == True:
            active_model = model
            break
    return active_model

    
def get_temp_data(config, data, index=0):
    return config.variables["temp_data"][data][index]


def get_temp_data_collection(config, data):
    return config.variables["temp_data"][data]


def add_temp_data(config, data, item):
    config.variables["temp_data"].setdefault(data, []).append(item)


def update_temp_data(config, data, index, key, value):
    config.variables["temp_data"][data][index].update({key: value})
# </editor-fold>


# <editor-fold desc="browser">


def get_response_code_by_url(url):
    return requests.get(url).status_code


def refresh_page(self):
    self.config.driver.refresh()
    return self


def click_browser_back_button(self):
    self.config.driver.execute_script("window.history.go(-1)")
    return self


def open_url_path(self, url_path):
    return self.config.driver.get(f"{self.config.domain}{url_path}")


def switch_to_window_by_name(self, window_name):
    self.config.parent_window = self.config.driver.current_window_handle
    time.sleep(5)
    self.config.driver.switch_to.window(window_name)
    return self


def switch_to_window_by_title(self, window_title):
    self.config.parent_window = self.driver.current_window_handle
    time.sleep(20)
    handles = self.driver.window_handles
    for i in handles:
        current_window = self.driver.switch_to.window(i)
        if self.driver.title == window_title:
            return current_window
    return self


def switch_to_parent_window(self):
    self.config.driver.switch_to.window(self.config.parent_window)
    return self


def switch_and_accept_alert(self):
    alert = self.driver.switch_to.alert
    alert.accept()


def close_current_window(self):
    self.config.driver.close()
    return self


# </editor-fold>


def retry(exceptions, tries=18, delay=0):
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions as e:
                    time.sleep(mdelay)
                    mtries -= 1
            return f(*args, **kwargs)

        return f_retry

    return deco_retry


def get_str_list_from_list_of_webelements(webelements):
    str_list = []
    for item in webelements:
        str_list.append(item.text)
    return str_list


def get_web_element_from_list_by_text(webelements, element_text):
    for i in range(len(webelements)):
        if element_text == webelements[i].text:
            return webelements[i]


def execute_click_for_all_webelements(webelements_list):
    for webelement in webelements_list:
        webelement.click()
