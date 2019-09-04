from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class ActivityDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_save(self):
        self.page.click(ActivityDialog.Locators.SAVE_BUTTON)
        return self

    def get_start_date_value(self):
        return self.page.get_attribute(ActivityDialog.Locators.START_DATE_FIELD, "value")

    def get_due_date_value(self):
        return self.page.get_attribute(ActivityDialog.Locators.DUE_DATE_FIELD, "value")

    def get_subject_value(self):
        return self.page.get_attribute(ActivityDialog.Locators.SUBJECT_FIELD, "value")

    def get_task_type_value(self):
        return self.page.get_text(ActivityDialog.Locators.TASK_TYPE_FIELD)

    class Locators(object):
        FRAME = (By.XPATH, "// iframe[contains(@src,'viewactivitydialogbytaskid')]")
        SAVE_BUTTON = (By.ID, "TaskChildGrid_3_8")
        START_DATE_FIELD = (By.CSS_SELECTOR, "#id_StartDate[type='text']")
        DUE_DATE_FIELD = (By.CSS_SELECTOR, "#id_DueDate[type='text']")
        SUBJECT_FIELD = (By.CSS_SELECTOR, "#id_Subject[type='text']")
        TASK_TYPE_FIELD = (By.CSS_SELECTOR, "#ActivityCategoryId")
