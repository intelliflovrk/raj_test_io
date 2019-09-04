import utils
from dsl.login_to_io import LogIn
from dsl.search import SearchClient
from identity.login import LoginPage
from ioffice.activity_dialog import ActivityDialog
from ioffice.base import IOBasePage
from ioffice.home import HomePage
from ioffice.organiser.base import BaseOrganiserPage
from ioffice.organiser.delete_user_task_options_dialog import DeleteUserTaskOptionsDialog
from ioffice.organiser.tasks import TasksPage
from ioffice.userdashboard import UserDashboardPage
import datetime


class UserTasks(SearchClient, LogIn):
    def navigate_my_dashboard(self):
        UserDashboardPage(self.config).level3_menu().click_my_dashboard()
        return self

    def navigate_to_home(self):
        IOBasePage(self.config).level1_menu().click_home()
        return self

    def navigate_to_organiser(self):
        IOBasePage(self.config).level1_menu().hover_over_navigation_menu().click_organiser()
        return self

    def navigate_to_tasks(self):
        BaseOrganiserPage(self.config).level2_menu().click_tasks()
        return self

    def navigate_to_my_tasks(self):
        TasksPage(self.config).level3_menu().click_my_tasks()
        return self

    def open_my_tasks_widget(self):
        UserDashboardPage(self.config).click_my_tasks()
        return self

    def using_activity_dialog(self):
        UserDashboardPage(self.config).click_individual_task_in_widget()
        return UserTasks._ActivityDialog(UserDashboardPage(self.config), self)

    class _ActivityDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ActivityDialog(current_page)

        def verify_task_details_in_activity_dialog(self):
            assert datetime.datetime.strftime(datetime.datetime.strptime(utils.get_api_data(
                self.config, "create_task")["startDate"], '%Y-%m-%d'), "%d/%m/%Y") == str(
                self.dialog.get_start_date_value()), "Start date is incorrect."
            assert datetime.datetime.strftime(datetime.datetime.strptime(utils.get_api_data(
                self.config, "create_task")["dueDate"], '%Y-%m-%d'), "%d/%m/%Y") == str(
                self.dialog.get_due_date_value()), "Due date is incorrect."
            assert self.dialog.get_subject_value() == utils.get_api_data(
                self.config, "create_task")["subject"], "Subject is incorrect."
            assert self.dialog.get_task_type_value() == utils.get_api_data(
                self.config, "create_task")["taskType"], " Activity Type is incorrect."
            return self

        def close_activity_dialog(self):
            self.dialog.click_save()
            self.dialog.close_io_dialog()
            return self.journey

    def change_date_filter(self):
        TasksPage(self.config).click_date_filter().click_all_open_date()
        return self

    def verify_task_exists_in_user_tasks(self):
        my_tasks_page = TasksPage(self.config)
        assert datetime.datetime.strftime(datetime.datetime.strptime(utils.get_api_data(
            self.config, "create_task")["startDate"], '%Y-%m-%d'), "%d %b %Y") == str(
            my_tasks_page.get_start_date_cell_value()), "Start date is incorrect."
        assert datetime.datetime.strftime(datetime.datetime.strptime(utils.get_api_data(
            self.config, "create_task")["dueDate"], '%Y-%m-%d'), "%d %b %Y") + " 01:00" == str(
            my_tasks_page.get_due_date_cell_value()), "Due date is incorrect."
        assert my_tasks_page.get_subject_cell_value() == utils.get_api_data(
            self.config, "create_task")["subject"], "Subject is incorrect."
        assert my_tasks_page.get_activity_type_cell_value() == utils.get_api_data(
            self.config, "create_task")["taskType"], " Activity Type is incorrect."
        return self

    def delete_user_open_tasks(self):
        my_tasks_page = TasksPage(self.config)
        my_tasks_page.check_select_all_tasks().click_delete() \
            .wait_until_please_wait_spinner_present()
        DeleteUserTaskOptionsDialog(my_tasks_page).click_ok() \
            .wait_until_please_wait_spinner_present() \
            .close_io_dialog()
        utils.click_browser_back_button(self)
        return self
