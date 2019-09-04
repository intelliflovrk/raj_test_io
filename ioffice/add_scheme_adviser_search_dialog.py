from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AddSchemeAdviserSearchDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame):
        super().__init__(parent_page)
        self.FRAME = AddSchemeAdviserSearchDialog.Locators.FRAME
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_search(self):
        self.page.click(AddSchemeAdviserSearchDialog.Locators.SEARCH_BUTTON)
        return self

    def click_first_result(self):
        self.page.click(AddSchemeAdviserSearchDialog.Locators.FIRST_RESULT)
        return self

    def clear_adviser_firstname_field(self):
        self.page.clear(AddSchemeAdviserSearchDialog.Locators.FIRST_NAME)
        return self

    def fill_in_adviser_firstname_field(self, data):
        self.page.fill_in_field(AddSchemeAdviserSearchDialog.Locators.FIRST_NAME, data)
        return self

    class Locators(object):
        FIRST_NAME = (By.ID, "id_Adviser_FirstName")
        FRAME = (By.XPATH, "//iframe[@src='/nio/adviser/searchdialog?popup_control=SellingAdviser']")
        SEARCH_BUTTON = (By.XPATH, "//a[text()='Search']")
        FIRST_RESULT = (By.XPATH, "//td[@class='first']/a")

