from ioffice.base import BasePageSection, BasePage, IOFrameDialog
from selenium.webdriver.common.by import By


class SelectDelegateDialog(BasePageSection, IOFrameDialog, BasePage):
    def __init__(self, parent_page, current_frame, popup_control):
        super().__init__(parent_page)
        self.popup_control = popup_control
        self.FRAME = (By.XPATH, SelectDelegateDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_first_result(self):
        return self.click(SelectDelegateDialog.Locators.FIRST_RESULT)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/system/delegatesearch?popup_control=id_DelegatePartyId']"
        FIRST_RESULT = (By.XPATH, "//td[@class='first']/a")
