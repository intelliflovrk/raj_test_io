from ioffice.base import BasePageSection, BasePage, IOFrameDialog
from selenium.webdriver.common.by import By


class ShareClientAdviserSearchDialog(BasePageSection, IOFrameDialog, BasePage):

    def __init__(self, parent_page, current_frame):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_search(self):
        self.click(ShareClientAdviserSearchDialog.Locators.SEARCH_BUTTON)
        return self

    def click_first_result(self):
        self.click(ShareClientAdviserSearchDialog.Locators.FIRST_RESULT)
        return self

    def fill_in_adviser_firstname_field(self, data):
        self.clear_and_fill_in_field(ShareClientAdviserSearchDialog.Locators.FIRST_NAME, data)
        return self

    class Locators(object):
        FIRST_NAME = (By.ID, "id_AdviserByLegalEntity_FirstName")
        FRAME = (By.XPATH, "// iframe[contains( @ src, 'AdviserSearchWithinLegalEntity')]")
        SEARCH_BUTTON = (By.XPATH, "//a[text()='Search']")
        FIRST_RESULT = (By.XPATH, "//td[@class='first']/a")
