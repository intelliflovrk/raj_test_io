from selenium.webdriver.common.by import By

from ioffice.base import IOFrameDialog
from pageobjects import BasePageSection


class AllocateLineItemDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, self.Locators._FRAME)
        self.frame_locator = self.FRAME
        self._switch_to_frame()

    def fill_in_first_name(self, data):
        self.page.clear_and_fill_in_field(self.Locators.FIRST_NAME, data)
        return self

    def click_clear(self):
        self.page.click(self.Locators.CLEAR_BUTTON)
        return self

    def click_search(self):
        self.page.click(self.Locators.SEARCH_BUTTON)
        return self

    def select_first_line_item(self):
        self.page.click(self.Locators.LINE_ITEM_RADIO_BUTTON)
        return self

    def click_allocate(self):
        self.page.click(self.Locators.ALLOCATE_BUTTON)
        return self

    def select_first_link_to_fee(self):
        self.page.click(self.Locators.LINK_TO_FEE_RADIO_BUTTON)
        return self

    def click_allocate_to_fee(self):
        self.page.click(self.Locators.ALLOCATE_TO_FEE_BUTTON)
        return self

    class Locators(object):
        _FRAME = "// iframe[contains(@src,'/nio/')]"
        FIRST_NAME = (By.CSS_SELECTOR, "#id_FirstName")
        LINE_ITEM_RADIO_BUTTON = (By.XPATH, "//*[@id='grid_id_root_2_2_4']/tbody//tr/td[1]/input")
        SEARCH_BUTTON = (By.XPATH, "//a[text()='Search']")
        ALLOCATE_BUTTON = (By.XPATH, "//a[text()='Allocate']")
        LINK_TO_FEE_RADIO_BUTTON = (By.CSS_SELECTOR, "[name='__s']")
        ALLOCATE_TO_FEE_BUTTON = (By.XPATH, "//a[text()='Allocate to Fee']")
        CLEAR_BUTTON = (By.XPATH, "//a[text()='Clear']")