from selenium.webdriver.common.by import By
from ioffice.clients.client_dashboard import BaseClientPage


class QuotesAppsPage(BaseClientPage):

    def click_quotes_illustrations(self):
        self.click(QuotesAppsPage.Locators.QUOTES_ILLUSTRATIONS_SUB_TAB)
        return self

    def click_quotes_apps(self):
        self.click(QuotesAppsPage.Locators.QUOTES_APPS_SUB_TAB)
        return self

    def click_refresh(self):
        return self.click(QuotesAppsPage.Locators.REFRESH_BUTTON)

    def get_quote_status(self):
        return self.get_text(QuotesAppsPage.Locators.TABLE_FIRST_ROW_QUOTE_STATUS_TEXT)

    def click_first_open_link(self):
        return self.click(QuotesAppsPage.Locators.OPEN_LINK)

    def click_delete(self):
        self.click(self.Locators.DELETE_BUTTON)
        return self

    def get_plan_reference(self):
        return self.get_text(QuotesAppsPage.Locators.PLAN_REFERENCE_LINK)

    def open_plan(self):
        return self.click(QuotesAppsPage.Locators.OPEN_PLAN_LINK)

    def get_product_type(self):
        return self.get_text(QuotesAppsPage.Locators.PRODUCT_TYPE)

    def select_first_row(self):
        return self.click(QuotesAppsPage.Locators.TABLE_FIRST_ROW_RADIO_BUTTON)

    class Locators(object):
        QUOTES_ILLUSTRATIONS_SUB_TAB = (By.XPATH, "//*[@id='id_root_2_2_5']/ul/li[2]/a/div")
        QUOTES_APPS_SUB_TAB = (By.XPATH, "//*[@id='id_root_2_2_5']/ul/li[1]/a/div")
        PLAN_REFERENCE_LINK = (By.XPATH, "//*[starts-with(@id, 'quotesGrid')]/td/span/a")
        TABLE_FIRST_ROW_QUOTE_STATUS_TEXT = (By.XPATH,
            "//*[starts-with(@id, 'quotesGrid')]//table//tbody//tr[not(self::node()[contains(concat(' ',normalize-space(@class),' '),' filter ')])]/td[7]")
        REFRESH_BUTTON = (By.XPATH, "//a[@id='QuotesAndAppTabWrapper_3_2_2']")
        OPEN_LINK = (By.XPATH, "//*[contains(., 'Complete')]/td[12]/a")
        OPEN_PLAN_LINK = (By.XPATH, "//*[starts-with(@id, 'quotesGrid')]/td[11]/span/a")
        DELETE_BUTTON = (By.CSS_SELECTOR, "#quotesGrid_15")
        PRODUCT_TYPE = (By.XPATH,
            "//*[starts-with(@id, 'quotesGrid')]//table//tbody//tr[not(self::node()[contains(concat(' ',normalize-space(@class),' '),' filter ')])]/td[6]")
        TABLE_FIRST_ROW_RADIO_BUTTON = (By.CSS_SELECTOR, "[class='rowselect first'] [type='radio']")
