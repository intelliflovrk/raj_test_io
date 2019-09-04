from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AddClientTaskDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = AddClientTaskDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_select_user(self):
        self.page.click(AddClientTaskDialog.Locators.SELECT_USER_BUTTON)
        return self

    def select_status(self, status_text):
        self.page.select_by_visible_text(AddClientTaskDialog.Locators.STATUS_SELECT_BOX, status_text)
        return self

    def click_save_task(self):
        self.page.click(AddClientTaskDialog.Locators.SAVE_TASK_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='AddTask']")
        SELECT_USER_BUTTON = (By.CSS_SELECTOR, "[for='id_AssignedToPartyId'] + span [class='hpick']")
        STATUS_SELECT_BOX = (By.ID, "StatusDropDown")
        SAVE_TASK_BUTTON = (By.ID, "SaveTask")
