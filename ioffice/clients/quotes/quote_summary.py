from ioffice.clients.quotes.base import BaseQuotesPage
from selenium.webdriver.common.by import By


class QuoteSummaryPage(BaseQuotesPage):
    def click_apply_for_first_quote(self):
        return self.click(QuoteSummaryPage.Locators.FIRST_QUOTE_APPLY_BUTTON)

    class Locators(object):
        FIRST_QUOTE_APPLY_BUTTON = (
            By.XPATH, "//*[starts-with(@id, 'termGridAll')and contains(., 'Aegon')]/td[12]/a")
