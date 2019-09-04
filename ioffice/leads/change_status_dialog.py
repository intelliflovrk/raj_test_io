from ioffice.wizard import *
from selenium.webdriver.common.by import By


class ChangeStatusDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = ChangeStatusDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_cancel_button(self):
        self.page.click(ChangeStatusDialog.Locators.CANCEL_BUTTON)
        return self

    def click_save_button(self):
        self.page.click(ChangeStatusDialog.Locators.SAVE_BUTTON)
        return self

    def select_status(self, status):
        self.page.select_by_visible_text(ChangeStatusDialog.Locators.STATUS_DROPDOWN_MENU, status)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='LeadChangeStatus']")
        CANCEL_BUTTON = (By.XPATH, "//*[@id='form_CanConvertToClient_2']/div[2]/div/a[2]")
        SAVE_BUTTON = (By.XPATH, "//*[@id='CanConvertToClient_2_3']")
        STATUS_DROPDOWN_MENU = (By.XPATH, "//*[@id='LeadStatus']")
