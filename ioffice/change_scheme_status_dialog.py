from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class ChangeSchemeStatusDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.popup_control = popup_control
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_status(self, data):
        self.page.select_by_visible_text(ChangeSchemeStatusDialog.Locators.CHANGE_STATUS_TO_DROP_DOWN, data)
        return self

    def click_save(self):
        self.page.click(ChangeSchemeStatusDialog.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='ChangeSchemeStatus']")
        CHANGE_STATUS_TO_DROP_DOWN = (By.ID, "ChangeStatusTo")
        SAVE_BUTTON = (By.ID, "btnUpdateStatus")
