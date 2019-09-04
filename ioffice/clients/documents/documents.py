from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from ioffice.clients.documents.base import BaseDocumentsPage, BaseClientPage


class ClientDocumentsPage(BaseDocumentsPage):
    def is_title_matches(self):
        return "Documents | Intelligent Office" == self.driver.title

    def verify_document_exists(self):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(ClientDocumentsPage.Locators.TABLE_FIRST_ROW, "Fact Find"))

    def click_select_all_documents(self):
        return self.click(self.Locators.SELECT_ALL_DOCUMENTS_CHECK_BOX)

    def click_delete(self):
        return self.click(self.Locators.DELETE_BUTTON)

    def click_add_to_binder(self):
        return self.click(ClientDocumentsPage.Locators.ADD_TO_BINDER_BUTTON)

    def get_first_table_row(self):
        return self.get_text(ClientDocumentsPage.Locators.TABLE_ROWS)

    def click_open_first_document(self):
        return self.click(self.Locators.FIRST_DOCUMENT_TITLE_LINK)

    def get_last_update_date(self):
        return self.get_text(self.Locators.LAST_UPDATE_DATE_TEXT)

    class Locators(object):
        TABLE_FIRST_ROW = (By.CSS_SELECTOR, "#sidebar-container table tbody tr:not(.filter)")
        SELECT_ALL_DOCUMENTS_CHECK_BOX = (By.XPATH, "//th[@class='first rowselect']//input[@type='checkbox']")
        DELETE_BUTTON = (By.CSS_SELECTOR, "tfoot a[onclick*='Delete']")
        LAST_UPDATE_DATE_TEXT = (By.CSS_SELECTOR, "tbody tr:nth-of-type(2) td:nth-of-type(7) span")
        ADD_TO_BINDER_BUTTON = (By.XPATH, "//tfoot//a[text()='Add To Binder']")
        TABLE_ROWS = (By.CSS_SELECTOR, "table tbody tr:not(.filter)")
        FIRST_DOCUMENT_TITLE_LINK = (By.CSS_SELECTOR, "tbody tr:nth-of-type(2) td:nth-of-type(3)")


class DocumentProfilePage(BaseClientPage):

    def get_category_text(self):
        return self.get_drop_down_selected_value(self.Locators.SELECTED_CATEGORY_TEXT)

    def get_subcategory_text(self):
        return self.get_drop_down_selected_value(self.Locators.SELECTED_SUBCATEGORY_TEXT)

    def get_created_on_date(self):
        return self.get_text(self.Locators.CREATED_ON_TEXT)

    class Locators(object):
        CREATED_ON_TEXT = (By.ID, "id_CreatedDate_ro")
        SELECTED_CATEGORY_TEXT = (By.ID, "id_Document_Category")
        SELECTED_SUBCATEGORY_TEXT = (By.ID, "id_Document_SubCategory")