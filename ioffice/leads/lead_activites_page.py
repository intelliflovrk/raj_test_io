from ioffice.leads.base import *


class LeadTasksPage(BaseLeadPage):

    def click_tasks_and_appts(self):
        return self.click(self.Locators.TASK_AND_APPTS_BUTTON)

    def click_delete(self):
        return self.click(self.Locators.DELETE_BUTTON)

    def open_first_open_link(self):
        return self.click(self.Locators.FIRST_OPEN_LINK)

    def check_select_all_task(self):
        return self.click(self.Locators.SELECT_ALL_CHECKBOX)

    def get_task_category(self):
        return self.get_drop_down_selected_value(self.Locators.TASK_CATEGORY_SELECT_BOX)

    def get_task_type(self):
        return self.get_drop_down_selected_value(self.Locators.TASK_TYPE_SELECT_BOX)

    def get_task_notes(self):
        return self.get_text(self.Locators.TASK_NOTES_TEXT)

    class Locators(object):
        TASK_AND_APPTS_BUTTON = (By.CSS_SELECTOR, ".ux-ctl-tabs-current .ux-lib-tbody")
        FIRST_OPEN_LINK = (By.CSS_SELECTOR, "[title='Open']")
        TASK_CATEGORY_SELECT_BOX = (By.CSS_SELECTOR, "#ActivityDropDown")
        TASK_TYPE_SELECT_BOX = (By.CSS_SELECTOR, "#ActivityCategoryId")
        TASK_NOTES_TEXT = (By.CSS_SELECTOR, ".task-note-content")
        SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, "thead [type]")
        DELETE_BUTTON = (By.CSS_SELECTOR, "#LeadTaskGrid_16")

