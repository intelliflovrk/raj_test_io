from selenium.common.exceptions import TimeoutException
import utils
from dsl.create_lead import CreateLead
from dsl.search import SearchLead
from ioffice.leads.add_lead_task_dialog import AddLeadTaskDialog
from ioffice.leads.delete_options_dialog import DeleteOptionsDialog
from ioffice.leads.lead_details_page import LeadDetailsPage
from utils import *
from ioffice.leads.lead_activites_page import LeadTasksPage, BaseLeadPage
from utils import get_common_data


class AddLeadTask(CreateLead, SearchLead):

    def using_add_lead_task_dialog(self):
        lead_details_page = LeadDetailsPage(self.config)
        lead_details_page.lead_actions_menu() \
            .hover_over_lead_actions() \
            .click_add_task()
        return AddLeadTask._AddLeadTask(lead_details_page, self)

    @retry(TimeoutException, 5)
    def open_lead_task(self):
        LeadTasksPage(self.config).click_tasks_and_appts().open_first_open_link()
        return self

    def navigate_to_lead_task_and_appts(self):
        BaseLeadPage(self.config).click_activities()
        return self

    def delete_all_lead_tasks(self):
        LeadTasksPage(self.config)\
            .check_select_all_task()\
            .click_delete()\
            .wait_until_please_wait_spinner_present()
        DeleteOptionsDialog(LeadTasksPage(self.config))\
            .click_ok() \
            .wait_until_please_wait_spinner_present() \
            .close_io_dialog()
        return self

    def verify_lead_task_added(self):
        data = get_common_data(self.config)["test_data"]["lead_data"]
        assert LeadTasksPage(self.config).get_task_category() == data["task_category"], "Task Category not matching"
        assert LeadTasksPage(self.config).get_task_type() == data["task_type"], "Task Type not matching"
        assert LeadTasksPage(self.config).get_task_notes() == self.config.task_notes, "Task Notes not matching"

    class _AddLeadTask:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddLeadTaskDialog(parent_page)

        def add_lead_task(self):
            data = get_common_data(self.config)["test_data"]["lead_data"]
            self.config.task_notes = utils.fakedata.rand_text(5)
            self.dialog.select_task_category(data["task_category"]) \
                .wait_until_please_wait_spinner_present() \
                .select_task_type(data["task_type"]) \
                .fill_in_notes(self.config.task_notes) \
                .click_save_task()
            return self.journey