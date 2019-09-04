from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from ioffice.clients.documents.base import BaseDocumentsPage


class ClientDocumentQueuePage(BaseDocumentsPage):
    def is_title_matches(self):
        return "Client Document Queue | Intelligent Office" == self.driver.title

    def click_refresh(self):
        return self.click(ClientDocumentQueuePage.Locators.REFRESH_BUTTON)

    def get_documents_table_rows(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_all_elements_located(ClientDocumentQueuePage.Locators.DOCUMENTS_LIST))

    def get_documents_table_str_list(self):
        data = self.get_documents_table_rows()
        textlist = []
        for item in data:
            textlist.append(item.text)
        return textlist

    def click_download(self):
        return self.click(ClientDocumentQueuePage.Locators.DOWNLOAD_BUTTON)

    def click_delete(self):
        return self.click(ClientDocumentQueuePage.Locators.DELETE_BUTTON)

    def check_select_all_documents(self):
        return self.click(ClientDocumentQueuePage.Locators.SELECT_ALL_DOCUMENTS_CHECKBOX)

    class Locators(object):
        REFRESH_BUTTON = (By.LINK_TEXT, "Refresh")
        DOCUMENTS_LIST = (By.CSS_SELECTOR, "#grid_docQueueGrid tbody tr:not(.filter)")
        DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "[id='grid_docQueueGrid'] a[title='Download']")
        DELETE_BUTTON = (By.ID, "docQueueGrid_12")
        SELECT_ALL_DOCUMENTS_CHECKBOX = (By.CSS_SELECTOR, "[id='grid_docQueueGrid'] thead [type='checkbox']")
