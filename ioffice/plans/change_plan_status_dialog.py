from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class ChangePlanStatusDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = ChangePlanStatusDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def get_info_message(self):
        return self.page.get_text(ChangePlanStatusDialog.Locators.INFO_MESSAGE)

    def select_status(self, data):
        self.page.select_by_visible_text(ChangePlanStatusDialog.Locators.CHANGE_STATUS_TO, data)
        return self

    def click_save(self):
        self.page.click(ChangePlanStatusDialog.Locators.SAVE_BUTTON)
        return self

    def click_close(self):
        self.page.click(ChangePlanStatusDialog.Locators.CLOSE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe")
        INFO_MESSAGE = (By.CSS_SELECTOR, "#lifeCycleRules_2_2")
        CHANGE_STATUS_TO = (By.ID, "ChangeStatusTo")
        CLOSE_BUTTON = (By.XPATH, "//a[contains(text(), 'Close')]")
        SAVE_BUTTON = (By.ID, "btnUpdateStatus")
