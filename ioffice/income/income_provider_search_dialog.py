from selenium.webdriver.common.by import By
from ioffice.base import IOFrameDialog
from pageobjects import BasePageSection


class IncomeProviderSearchDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, self.Locators._FRAME)
        self.frame_locator = self.FRAME
        self._switch_to_frame()

    def select(self, provider_text):
        self.page.select_by_visible_text(self.Locators.SELECT_BOX, provider_text)
        return self

    def click_ok(self):
        self.page.click(self.Locators.OK_BUTTON)
        return self

    class Locators(object):
        _FRAME = "// iframe[contains(@src,'/nio/')]"
        SELECT_BOX = (By.ID, "ProviderListDropDown")
        PROVIDER_VALUE = (By.XPATH, "//*[@id='ProviderListDropDown']/option")
        OK_BUTTON = (By.XPATH, "//a[text()='OK']")