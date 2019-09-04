from ioffice.base import BasePageSection ,IOFrameDialog
from selenium.webdriver.common.by import By


class ChangeFeeStatusDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None, popup_control=None):
        super().__init__(parent_page)
        self.popup_control = popup_control
        self.FRAME = (By.XPATH, ChangeFeeStatusDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_status(self, status):
        self.page.select_by_visible_text(ChangeFeeStatusDialog.Locators.CHANGE_STATUS_TO, status)
        return self

    def click_save(self):
        self.page.click(ChangeFeeStatusDialog.Locators.SAVE_BUTTON)
        return self

    def click_close(self):
        self.page.click(ChangeFeeStatusDialog.Locators.CLOSE_BUTTON)
        return self

    class Locators(object):
        _FRAME = "// iframe[contains(@src,'/nio/')]"
        CHANGE_STATUS_TO = (By.ID, "IsCancelled")
        CLOSE_BUTTON = (By.XPATH, "//a[contains(text(), 'Close')]")
        SAVE_BUTTON = (By.ID, "id_root_2_2_4_5")
