from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AddFundDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.frame_locator = AddFundDialog.Locators.FRAME
        self.prev_frame_locator = None
        self._switch_to_frame()

    def clear_number_of_units_holdings(self):
        self.page.clear(AddFundDialog.Locators.NUMBER_OF_UNITS_HOLDINGS_FIELD)
        return self

    def fill_in_number_of_units_holdings(self, value):
        self.page.fill_in_field(AddFundDialog.Locators.NUMBER_OF_UNITS_HOLDINGS_FIELD, value)
        return self

    def clear_gross_purchase_price(self):
        self.page.clear(AddFundDialog.Locators.GROSS_PURCHASE_PRICE)
        return self

    def fill_in_gross_purchase_price(self, value):
        self.page.fill_in_field(AddFundDialog.Locators.GROSS_PURCHASE_PRICE, value)
        return self

    def open_fund_search_dialog(self):
        self.page.click(AddFundDialog.Locators.FUND_SEARCH_BUTTON)
        return AddFundDialog.FundSearchDialog(self.page, self.frame_locator)

    def click_save(self):
        self.page.click(AddFundDialog.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='/addfund/']")
        FUND_SEARCH_BUTTON = (By.XPATH, "//*[@id='__display_id_FundId']//following-sibling::*/a[@class='hpick']")
        SAVE_BUTTON = (By.LINK_TEXT, "Save")
        GROSS_PURCHASE_PRICE = (By.ID, "id_FundTransaction_Gross")
        NUMBER_OF_UNITS_HOLDINGS_FIELD = (By.ID, "id_FundTransaction_UnitQuantity")

    class FundSearchDialog(BasePageSection, IOFrameDialog):

        def __init__(self, parent_page, current_frame):
            super().__init__(parent_page)
            self.frame_locator = AddFundDialog.FundSearchDialog.Locators.FRAME
            self.prev_frame_locator = current_frame
            self._switch_to_frame()

        def click_search(self):
            self.page.click(AddFundDialog.FundSearchDialog.Locators.SEARCH_BUTTON)
            return self

        def clear_and_fill_in_fund_name_field(self, data):
            self.page.clear_and_fill_in_field(AddFundDialog.FundSearchDialog.Locators.FUND_NAME, data)
            return self

        def click_first_result(self):
            first_result_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AddFundDialog.FundSearchDialog.Locators.FIRST_RESULT))
            """IP-40474 It needs to scroll to element because of the Start button.
            moveToElement method is not working in this case."""
            self.driver.execute_script("arguments[0].scrollIntoView();", first_result_element)
            first_result_element.click()
            return self

        class Locators(object):
            FRAME = (By.XPATH, "//iframe[@src='/nio/PriceMaintenance/FundSearchDialogForPlan?popup_control=id_FundId']")
            SEARCH_BUTTON = (By.LINK_TEXT, "Search")
            FIRST_RESULT = (By.XPATH, "//td[@class='first']/a")
            FUND_NAME = (By.ID, "id_FundSearch_FundName")
