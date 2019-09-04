import datetime
from selenium.common.exceptions import TimeoutException
from dsl.search import *
from ioffice.clients.activities.base import ActivitiesBasePage
from ioffice.clients.activities.open_activities import TasksAndApptsPage
from ioffice.clients.activities.upload_document_dialog import UploadDocumentToTaskDialog
from ioffice.clients.base import BaseClientPage
from ioffice.clients.activities.delete_client_task_options_dialog import DeleteClientTaskOptionsDialog
from ioffice.clients.add_client_task_dialog import AddClientTaskDialog
from ioffice.user_search_dialog import UserSearchDialog
from ioffice.clients.activities.task import TaskDetailsPage, TaskDocumentsPage, ClientTaskBasePage
from ioffice.clients.activities.add_notes_dialog import AddNotesDialog
from utils import *
import fakedata


class ClientActivities(SearchClient, SearchTask):

    def using_add_client_task_dialog(self):
        BaseClientPage(self.config)\
            .client_actions_menu()\
            .hover_over_client_actions()\
            .click_add_task()
        return ClientActivities._AddClientTask(BaseClientPage(self.config), self)

    def using_task_upload_document_dialog(self):
        TaskDetailsPage(self.config).hover_over_task_actions().click_upload_document()
        return ClientActivities._TaskDetails(self)

    def navigate_to_client_open_activities(self):
        BaseClientPage(self.config).level3_menu().click_activities()
        return ClientActivities._TasksAndAppts(self)

    def navigate_to_client_workflows(self):
        BaseClientPage(self.config).level3_menu().click_activities()
        ActivitiesBasePage(self.config).activities_navigation_menu().click_workflows()
        return self

    def navigate_to_task_documents(self):
        ClientTaskBasePage(self.config).task_navigation_menu().click_documents()
        return ClientActivities._TaskDocuments(self)

    class _AddClientTask:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddClientTaskDialog(parent_page)

        def add_task_details(self):
            self.select_assigned_to_user(get_user_by_type(self.config, "default")["username"])
            self.dialog.wait_until_please_wait_spinner_present()\
                .select_status(get_common_data(self.config)["basic_data"]["task_status"])
            return self

        def select_assigned_to_user(self, user_name):
            self.dialog.click_select_user()
            user_search_dialog = UserSearchDialog(self.dialog.page, self.dialog.frame_locator, 'id_AssignedToPartyId')
            user_search_dialog.click_clear_button()
            self._search_and_select_user(user_name)
            user_search_dialog.close_dialog()
            return self

        @retry(TimeoutException, 2)
        def _search_and_select_user(self, user_name):
            UserSearchDialog(self.dialog.page, self.dialog.frame_locator, 'id_AssignedToPartyId')\
                .fill_in_user(user_name)\
                .click_search()\
                .click_first_result()
            return self

        def save_task(self):
            self.dialog.click_save_task().wait_until_please_wait_spinner_present().close_dialog()
            return ClientActivities._TasksAndAppts(self.journey)

    class _TasksAndAppts:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = TasksAndApptsPage(self.config)

        def show_all_tasks_and_appts(self):
            self.page.click_pick_task_fliter() \
                .click_all_tasks_and_appts()
            return self

        def open_task(self):
            self.page.click_first_open_link()
            return ClientActivities._TaskDetails(self)

        def delete_client_open_activities(self):
            tasks_and_appts_page = TasksAndApptsPage(self.config)
            tasks_and_appts_page.check_select_all_activities().click_delete() \
                .wait_until_please_wait_spinner_present()
            DeleteClientTaskOptionsDialog(tasks_and_appts_page).click_ok() \
                .wait_until_please_wait_spinner_present() \
                .close_io_dialog()
            return self

        @retry(AssertionError, 60)
        def verify_workflow_task_visible_on_client_activities(self):
            open_activities_page = TasksAndApptsPage(self.config)
            open_activities_page.activities_navigation_menu().click_tasks_and_appts()
            client_activity_details_list = get_str_list_from_list_of_webelements(
                open_activities_page.get_activity_table_rows())
            assert is_string_present(client_activity_details_list, get_common_data(
                self.config)["test_data"]["workflow_data"]["select_step_task"]), "Task is not found"
            return self.journey

    class _TaskDocuments:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = TaskDocumentsPage(self.config)

        def verify_task_documents_uploaded(self):
            assert datetime.datetime.now().strftime("%d/%m/%Y") in self.page.get_last_updated_date(), \
                "Incorrect document updated date"
            return self

    class _TaskDetails:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = TaskDetailsPage(self.config)

        def add_task_note(self):
            self.page.hover_over_task_actions().click_add_a_task_note()
            task_note = fakedata.rand_text()
            add_temp_data(self.config, "task", {"notes": [{"notes": task_note}]})
            AddNotesDialog(self.page).fill_in_note_details(task_note).click_save().close_dialog()
            self.page.wait_until_please_wait_spinner_present()
            return self

        def upload_task_document(self):
            UploadDocumentToTaskDialog(self.page).click_file_type().send_file_url().click_upload_button()
            return ClientActivities(self.config)

        def verify_client_mobile_present(self):
            observed_mobile = self.page.get_mobile()
            expected_mobile = get_temp_data(self.config, "client_contacts")["value"]
            assert observed_mobile == expected_mobile, \
                f"Expected mobile is {expected_mobile}. Observed mobile is {observed_mobile}."
            return self

        def verify_client_address_present(self):
            observed_address = self.page.get_address()
            address_lines_list = [line for line in list(get_temp_data(self.config, "address")["address"].values())
                                  if type(line) == str]
            expected_address = ', '.join(address_lines_list)
            assert observed_address == expected_address, \
                f"Expected address is {expected_address}. Observed address is {observed_address}"
            return self

        def verify_assigned_to_user_is(self, assigned_to_user):
            observed_user = self.page.get_assigned_to()
            expected_user = assigned_to_user
            assert observed_user == expected_user, \
                f"Expected user is {expected_user}. Observed user is {observed_user}"
            return self

        def verify_status_is(self, status):
            observed_status = self.page.get_status()
            expected_status = status
            assert observed_status == expected_status, \
                f"Expected status is {expected_status}. Observed status is {observed_status}."
            return self

        def verify_task_note_present(self):
            observed_note_text = self.page.get_note()
            expected_note_text = get_temp_data(self.config, "task")["notes"][0]["notes"]
            assert observed_note_text == expected_note_text, \
                f"Expected note is {expected_note_text}. Observed note is {observed_note_text}"
            return self

        def verify_task_details(self):
            self.verify_client_mobile_present()
            self.verify_client_address_present()
            user = get_common_data(self.config)["advisers"]["default"]["firstname"] + " " + \
                            get_common_data(self.config)["advisers"]["default"]["lastname"]
            self.verify_assigned_to_user_is(user)
            status = get_common_data(self.config)["basic_data"]["task_status"]
            self.verify_status_is(status)
            self.verify_task_note_present()
            return self.journey
