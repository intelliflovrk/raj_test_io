from ioffice.wizard import *
from selenium.webdriver.common.by import By


class AddLeadTaskDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = AddLeadTaskDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_task_category(self, data):
        self.page.select_by_visible_text(AddLeadTaskDialog.Locators.TASK_CATEGORY_SELECT_BOX, data)
        return self

    def select_task_type(self, data):
        self.page.select_by_visible_text(AddLeadTaskDialog.Locators.TASK_TYPE_SELECT_BOX, data)
        return self

    def fill_in_notes(self, data):
        self.page.clear_and_fill_in_field(AddLeadTaskDialog.Locators.NOTES_FIELD, data)
        return self

    def click_save_task(self):
        self.page.click(AddLeadTaskDialog.Locators.SAVE_TASK_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='AddTask']")
        SAVE_TASK_BUTTON = (By.CSS_SELECTOR, "#SaveTask")
        NOTES_FIELD = (By.CSS_SELECTOR, "textarea")
        TASK_CATEGORY_SELECT_BOX = (By.CSS_SELECTOR, "#ActivityDropDown")
        TASK_TYPE_SELECT_BOX = (By.CSS_SELECTOR, "#ActivityCategoryId")
