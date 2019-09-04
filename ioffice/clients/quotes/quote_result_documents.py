from selenium.webdriver.common.by import By
from ioffice.clients.quotes.quote_result_base import QuoteResultBasePage


class QuoteResultDocumentsPage(QuoteResultBasePage):

    def get_document_title(self):
        return self.get_text(QuoteResultDocumentsPage.Locators.DOCUMENTS_FIRST_COLUMN_CELL)

    def get_document_description(self):
        return self.get_text(QuoteResultDocumentsPage.Locators.DOCUMENTS_SECOND_COLUMN_CELL)

    def get_document_category(self):
        return self.get_text(QuoteResultDocumentsPage.Locators.DOCUMENTS_THIRD_COLUMN_CELL)

    def get_document_subcategory(self):
        return self.get_text(QuoteResultDocumentsPage.Locators.DOCUMENTS_FORTH_COLUMN_CELL)

    def click_view_button(self):
        return self.click(QuoteResultDocumentsPage.Locators.VIEW_BUTTON)

    class Locators(object):
        VIEW_BUTTON = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[7]/a")
        DOCUMENTS_FIRST_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[2]/span")
        DOCUMENTS_SECOND_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[3]/span")
        DOCUMENTS_THIRD_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[4]/span")
        DOCUMENTS_FORTH_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[5]/span")
