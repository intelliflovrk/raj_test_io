from selenium.webdriver.common.by import By
from ioffice.clients.base import BaseClientPage


class QuoteResultBasePage(BaseClientPage):

    def click_results_tab(self):
        return self.click(QuoteResultBasePage.Locators.RESULTS_TAB)

    def click_documents_tab(self):
        return self.click(QuoteResultBasePage.Locators.DOCUMENTS_TAB)

    class Locators(object):
        RESULTS_TAB = (By.CSS_SELECTOR, "a[href*='QuoteResultSummary']")
        DOCUMENTS_TAB = (By.CSS_SELECTOR, "a[href*='QuoteResultDocuments']")
