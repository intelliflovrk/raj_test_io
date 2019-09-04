from selenium.webdriver.common.by import By
from ioffice.clients.client_dashboard import BaseClientPage


class QuotesIllustrationsPage(BaseClientPage):

    def click_refresh(self):
        return self.click(QuotesIllustrationsPage.Locators.REFRESH_BUTTON)

    def click_first_reference(self):
        return self.click(QuotesIllustrationsPage.Locators.FIRST_REFERENCE_LINK)

    def get_quote_status(self):
        return self.get_text(QuotesIllustrationsPage.Locators.TABLE_FIRST_ROW_QUOTE_STATUS_TEXT)

    def get_product_type(self):
        return self.get_text(QuotesIllustrationsPage.Locators.PRODUCT_TYPE)

    def get_provider(self):
        return self.get_text(QuotesIllustrationsPage.Locators.PROVIDER)

    def get_quote_reference(self):
        return self.get_text(QuotesIllustrationsPage.Locators.QUOTE_REFERENCE)

    def fill_in_reference_filter(self, reference):
        return self.fill_in_field(QuotesIllustrationsPage.Locators.REFERENCE_FILTER_FIELD, reference)

    def click_filter(self):
        return self.click(QuotesIllustrationsPage.Locators.FILTER_BUTTON)

    class Locators(object):
        TABLE_FIRST_ROW_QUOTE_STATUS_TEXT = (By.XPATH, "//*[@id='grid_QuotationGrid']/tbody/tr[2]/td[6]/span")
        REFRESH_BUTTON = (By.ID, "id_root_3_2_2")
        FIRST_REFERENCE_LINK = (By.CSS_SELECTOR, "a[href*='QuoteResultSummary']")
        PRODUCT_TYPE = (By.XPATH, "//*[@id='grid_QuotationGrid']/tbody/tr[2]/td[5]/span")
        PROVIDER = (By.XPATH, "//*[@id='grid_QuotationGrid']/tbody/tr[2]/td[3]/span")
        QUOTE_REFERENCE = (By.XPATH, "//*[@id='grid_QuotationGrid']/tbody/tr[2]/td[4]/span")
        REFERENCE_FILTER_FIELD = (By.ID, "id___filterReference")
        FILTER_BUTTON = (By.CSS_SELECTOR, "#QuotationGrid__ a[onclick*='Filter(this)']")
