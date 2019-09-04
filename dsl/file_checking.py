from utils import *
from selenium.common.exceptions import TimeoutException
from dsl.add_mortgage_plan import AddMortgagePlan, IOBasePage
from ioffice.file_checking import FileCheckingPage
from ioffice.userdashboard import UserDashboardPage
from ioffice.compliance.post_search import PostSearchPage
from ioffice.compliance.pre_search import PreSearchPage


class FileChecking(AddMortgagePlan):

    def navigate_to_post_search(self):
        UserDashboardPage(self.config).level1_menu().hover_over_navigation_menu() \
            .click_compliance()
        IOBasePage(self.config).level2_menu() \
            .click_file_checking()
        FileCheckingPage(self.config) \
            .click_post_search()
        return self

    def navigate_to_pre_search(self):
        UserDashboardPage(self.config).level1_menu().hover_over_navigation_menu() \
            .click_compliance()
        IOBasePage(self.config).level2_menu() \
            .click_file_checking()
        FileCheckingPage(self.config) \
            .click_pre_search()
        return self

    def search_and_open_client(self):
        client_name = get_temp_data(self.config, "client")["name"]
        FileCheckingPage(self.config) \
            .select_search_type(get_common_data(self.config)["test_data"]["compliance_data"]["SEARCH_TYPE"]) \
            .click_clear_button() \
            .using_select_client_dialog() \
            .click_clear_button() \
            .fill_in_first_name(client_name.split(" ")[0]) \
            .fill_in_last_name(client_name.split(" ")[1]) \
            .click_search() \
            .click_first_result()
        return self

    @retry(TimeoutException)
    def wait_until_pre_search_results_appear(self):
        PreSearchPage(self.config).click_search_button()\
            .get_first_search_result()
        return self

    @retry(TimeoutException)
    def wait_until_post_search_results_appear(self):
        PostSearchPage(self.config).click_search_button()\
            .get_first_search_result()
        return self

    def verify_plan_present_in_search_results(self):
        plan = get_temp_data(self.config, "plan")
        assert plan["reference"] == FileCheckingPage(self.config).get_io_ref(), \
            "Plan not preset in search results"
        return self
