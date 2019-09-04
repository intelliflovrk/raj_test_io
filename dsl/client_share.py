import utils
from dsl.create_client import CreateClient
from dsl.login_to_io import LogIn
from ioffice.clients.activities.open_activities import TasksAndApptsPage
from ioffice.clients.client_dashboard import ClientDashboardPage, BaseClientPage
from ioffice.clients.add_client_share_dialog import ShareClientDialog
from utils import *


class ShareClient(CreateClient, LogIn):
    def __init__(self, config):
        super().__init__(config)
        self.dialog = {}
        self.page = {}

    def navigate_to_client_open_activities(self):
        BaseClientPage(self.config).level3_menu().click_activities()
        return self

    def using_client_share_dialog(self):
        clientdashboard = ClientDashboardPage(self.config)
        clientdashboard.client_actions_menu().hover_over_client_actions().client_share()
        self.dialog = ShareClient._ShareClientDialog(clientdashboard, self)
        return self.dialog

    def verify_access_to_shared_client(self):
        assert get_temp_data(self.config, "client")["person"]["firstName"] + " " + get_temp_data(self.config, "client")["person"]["lastName"] == ClientDashboardPage(self.config).get_client_bar_info(), "Shared client not found"
        return self

    @retry(AssertionError, 60)
    def verify_task_assigned_to_client_share_adviser(self):
        open_activities_page = TasksAndApptsPage(self.config)
        open_activities_page.activities_navigation_menu().click_tasks_and_appts()
        client_activity_details_list = get_str_list_from_list_of_webelements(
            open_activities_page.get_activity_table_rows())
        assert utils.is_string_present(client_activity_details_list, get_common_data(
            self.config)["test_data"]["client_share_data"]["assigned_to"]), "Task is not found"
        return self

    class _ShareClientDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ShareClientDialog(current_page)

        def select_additional_adviser(self):
            self.dialog \
                .open_client_share_adviser_search_dialog() \
                .fill_in_adviser_firstname_field(get_user_by_type(self.config, "clientshare_user")["firstname"]) \
                .click_search() \
                .click_first_result() \
                .close_io_dialog()
            return self

        def fill_in_client_share_dialog(self):
            self.select_additional_adviser()
            self.dialog\
                .click_create_task_check_box()\
                .wait_until_please_wait_spinner_present()\
                .fill_in_notes(get_common_data(self.config)["basic_data"]["basic_text"]["BASIC_TEXT"])\
                .click_add_button() \
                .click_ok_in_browser_confirmation_dialog()
            self.dialog.close_dialog()
            return self.journey