from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AdviserSearchDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame, popup_control):
        super().__init__(parent_page)
        self.popup_control = popup_control
        self.FRAME = (By.XPATH, AdviserSearchDialog.Locators._FRAME.format(self.popup_control))
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_search(self):
        self.page.click(AdviserSearchDialog.Locators.SEARCH_BUTTON)
        return self

    def click_first_result(self):
        self.page.click(AdviserSearchDialog.Locators.FIRST_RESULT)
        return self

    def clear_adviser_firstname_field(self):
        self.page.clear(AdviserSearchDialog.Locators.FIRST_NAME)
        return self

    def fill_in_adviser_firstname_field(self, data):
        self.page.fill_in_field(AdviserSearchDialog.Locators.FIRST_NAME, data)
        return self

    class Locators(object):
        FIRST_NAME = (By.ID, "id_ActiveAdviser_FirstName")
        _FRAME = "//iframe[contains(translate(@src, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'/nio/adviser/searchdialogactiveadviser?popup_control=')]"
        SEARCH_BUTTON = (By.XPATH, "//a[text()='Search']")
        FIRST_RESULT = (By.XPATH, "//td[@class='first']/a")



