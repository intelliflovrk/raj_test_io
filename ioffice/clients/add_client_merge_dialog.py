from selenium.webdriver.common.by import By
from ioffice.base import IOFrameDialog
from pageobjects import BasePageSection


class MergeClientDialog(BasePageSection, IOFrameDialog):
    def __init__(self,parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, MergeClientDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def fill_in_firstname_field(self, data):
        self.page.clear_and_fill_in_field(MergeClientDialog.Locators.FIRST_NAME_FIELD, data)
        return self

    def fill_in_lastname_field(self, data):
        self.page.clear_and_fill_in_field(MergeClientDialog.Locators.LAST_NAME_FIELD, data)
        return self

    def click_search_button(self):
        self.page.click(MergeClientDialog.Locators.SEARCH_BUTTON)
        return self

    def click_first_check_box(self):
        self.page.click(MergeClientDialog.Locators.FIRST_CHECK_BOX)
        return self

    def click_select_for_merge_button(self):
        self.page.click(MergeClientDialog.Locators.SELECT_FOR_MERGE_BUTTON)
        return self

    def click_merge_button(self):
        self.page.click(MergeClientDialog.Locators.MERGE_BUTTON)
        return self

    def click_close_button(self):
        self.page.click(MergeClientDialog.Locators.CLOSE_BUTTON)
        return self

    class Locators(object):
        _FRAME = "// iframe[contains(@src,'BeginMergeClientSearch')]"
        FIRST_NAME_FIELD = (By.ID, "id_Client_FirstName")
        LAST_NAME_FIELD = (By.ID, "id_Client_LastName")
        SEARCH_BUTTON = (By.XPATH, "//a[@class='button button-enabled isDefault' and contains(text(),'Search')]")
        FIRST_CHECK_BOX = (By.CSS_SELECTOR, "[name='__s']")
        SELECT_FOR_MERGE_BUTTON = (By.XPATH, "//a[contains(text(),'Select For Merge')]")
        MERGE_BUTTON = (By.ID, "SaveAction")
        CLOSE_BUTTON = (By.XPATH, "//body[@class='body']/a[@href='#']")
