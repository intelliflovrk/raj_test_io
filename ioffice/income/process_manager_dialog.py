from selenium.webdriver.common.by import By
from ioffice.base import IOFrameDialog
from pageobjects import BasePageSection


class PaymentRunProcessManagerDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, self.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = None
        self._switch_to_frame()

    def click_advisers_check_box(self):
        self.page.click(self.Locators.ADVISERS_CHECK_BOX)
        return self

    def click_introducers_check_box(self):
        self.page.click(self.Locators.INTRODUCERS_CHECK_BOX)
        return self

    def click_clients_check_box(self):
        self.page.click(self.Locators.CLIENTS_CHECK_BOX)
        return self

    def click_staff_check_box(self):
        self.page.click(self.Locators.STAFF_CHECK_BOX)
        return self

    def click_start_button(self):
        self.page.click(self.Locators.START_BUTTON)
        return self

    def click_confirm_button(self):
        self.page.click(self.Locators.CONFIRM_BUTTON)
        return self

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/paymentruns/generatepaymentrun']"
        ADVISERS_CHECK_BOX = (By.CSS_SELECTOR, "#id_IsPayPractitioner")
        INTRODUCERS_CHECK_BOX = (By.CSS_SELECTOR, "#id_IsPayIntroducer")
        CLIENTS_CHECK_BOX = (By.CSS_SELECTOR, "#id_IsPayClient")
        STAFF_CHECK_BOX = (By.CSS_SELECTOR, "#id_IsPayUser")
        START_BUTTON = (By.XPATH, "//a[@id='id_root_2_2_2_5']")
        CONFIRM_BUTTON = (By.XPATH, "//a[@id='id_root_2_2_2_4']")


class MonthEndProcessManagerDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, self.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = None
        self._switch_to_frame()

    def fill_in_description_text_box(self, data):
        self.page.clear_and_fill_in_field(self.Locators.DESCRIPTION_TEXT_BOX, data)
        return self

    def click_start_button(self):
        self.page.click(self.Locators.START_BUTTON)
        return self

    def click_confirm_button(self):
        self.page.click(self.Locators.CONFIRM_BUTTON)
        return self

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/paymentruns/CloseMonthEnd']"
        DESCRIPTION_TEXT_BOX = (By.CSS_SELECTOR, "#id_Description")
        START_BUTTON = (By.XPATH, "//a[contains(text(),'Start')]")
        CONFIRM_BUTTON = (By.XPATH, "//a[contains(text(),'Confirm')]")
