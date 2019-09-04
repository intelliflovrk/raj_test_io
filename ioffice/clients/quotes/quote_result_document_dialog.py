from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class QuoteResultDocumentDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def get_first_quote_document_title(self):
        return self.page.get_text(self.Locators.FIRST_QUOTE_DOCUMENT_TITLE_TEXT)

    def click_close_button(self):
        return self.page.click(QuoteResultDocumentDialog.Locators.CLOSE_BUTTON)

    def click_view_button(self):
        return self.page.click(QuoteResultDocumentDialog.Locators.VIEW_BUTTON)

    def get_document_title(self):
        return self.page.get_text(QuoteResultDocumentDialog.Locators.DOCUMENTS_FIRST_COLUMN_CELL)

    def get_document_description(self):
        return self.page.get_text(QuoteResultDocumentDialog.Locators.DOCUMENTS_SECOND_COLUMN_CELL)

    def get_document_category(self):
        return self.page.get_text(QuoteResultDocumentDialog.Locators.DOCUMENTS_THIRD_COLUMN_CELL)

    def get_document_subcategory(self):
        return self.page.get_text(QuoteResultDocumentDialog.Locators.DOCUMENTS_FORTH_COLUMN_CELL)

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe")
        FIRST_QUOTE_DOCUMENT_TITLE_TEXT = (By.XPATH, "//table[@id='grid_DocumentsGrid']/tbody/tr")
        VIEW_BUTTON = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[7]/a")
        CLOSE_BUTTON = (By.XPATH, "//*[@id='form_quoteResultDocumentContainer_3']/div[2]/div/a")
        DOCUMENTS_FIRST_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[2]/span")
        DOCUMENTS_SECOND_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[3]/span")
        DOCUMENTS_THIRD_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[4]/span")
        DOCUMENTS_FORTH_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'DocumentsGrid')]/td[5]/span")
