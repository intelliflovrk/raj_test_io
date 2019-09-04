from ioffice.income.base import IncomeBasePage, By


class CashReceiptSearchPage(IncomeBasePage):

    def click_select_category(self):
        return self.click(CashReceiptSearchPage.Locators.SELECT_CATEGORY_BUTTON)

    def select_fee_category(self):
        return self.click(CashReceiptSearchPage.Locators.FEE_CATEGORY)

    def fill_in_amount(self, amount):
        return self.clear_and_fill_in_field(CashReceiptSearchPage.Locators.AMOUNT_TEXT_BOX, amount)

    def fill_in_description(self, description):
        return self.fill_in_field(CashReceiptSearchPage.Locators.DESCRIPTION_TEXT_BOX, description)

    def click_create(self):
        return self.click(CashReceiptSearchPage.Locators.CREATE_BUTTON)

    def click_clear(self):
        return self.click(CashReceiptSearchPage.Locators.CLEAR_BUTTON)

    def fill_in_description_search(self, description):
        return self.fill_in_field(CashReceiptSearchPage.Locators.DESCRIPTION_SEARCH_TEXT_BOX, description)

    def click_search(self):
        return self.click(CashReceiptSearchPage.Locators.SEARCH_BUTTON)

    def click_match(self):
        return self.click(CashReceiptSearchPage.Locators.MATCH_BUTTON)

    def select_first_search_result_record(self):
        self.click(CashReceiptSearchPage.Locators.SEARCH_RESULT_RADIO_BUTTON)
        return self

    def click_delete(self):
        return self.click(CashReceiptSearchPage.Locators.DELETE_BUTTON)

    class Locators(object):
        SELECT_CATEGORY_BUTTON = (By.CSS_SELECTOR, "#id_CashReceipt_Category1 + span a")
        FEE_CATEGORY = (By.CSS_SELECTOR, "#id_CashReceipt_Category1 + div select [value='Fee']")
        AMOUNT_TEXT_BOX = (By.CSS_SELECTOR, "#id_CashReceipt_Amount")
        DESCRIPTION_TEXT_BOX = (By.CSS_SELECTOR, "#id_CashReceipt_Description")
        CREATE_BUTTON = (By.LINK_TEXT, "Create")
        CLEAR_BUTTON = (By.LINK_TEXT, "Clear")
        DESCRIPTION_SEARCH_TEXT_BOX = (By.CSS_SELECTOR, "#id_Description")
        SEARCH_BUTTON = (By.LINK_TEXT, "Search")
        MATCH_BUTTON = (By.XPATH, "//table[@id='grid_CashReceiptGrid']//tbody//td/a[contains(text(),'Match')]")
        SEARCH_RESULT_RADIO_BUTTON = (By.CSS_SELECTOR, "#grid_CashReceiptGrid [type='radio']")
        DELETE_BUTTON = (By.LINK_TEXT, "Delete")
