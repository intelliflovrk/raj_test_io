from selenium.webdriver.common.by import By
from ioffice.base import IOBasePage


class UploadsPage(IOBasePage):

    def click_data_uploader(self):
        self.click(UploadsPage.Locators.DATA_UPLOADER)
        return self

    def click_download_template(self):
        return self.click(UploadsPage.Locators.DOWNLOAD_TEMPLATE)

    def click_import_completed_template(self):
        return self.click(UploadsPage.Locators.IMPORT_COMPLETED_TEMPLATE)

    def clear_file_name_field(self):
        self.clear(UploadsPage.Locators.FILE_NAME)
        return self

    def fill_in_file_name_field(self, data):
        self.fill_in_field(UploadsPage.Locators.FILE_NAME, data)
        return self

    def click_search_button(self):
        return self.click(UploadsPage.Locators.SEARCH_BUTTON)

    def get_status_value(self):
        return self.get_text(UploadsPage.Locators.FIRST_ROW_STATUS)

    def get_failed_count_value(self):
        return self.get_text(UploadsPage.Locators.FIRST_ROW_FAILED_COUNT)

    class Locators:
        DOWNLOAD_TEMPLATE = (By.CSS_SELECTOR, "body > div.quicklinks-wrapper.group > ul > li:nth-child(1) > a")
        IMPORT_COMPLETED_TEMPLATE = (By.CSS_SELECTOR, "body > div.quicklinks-wrapper.group > ul > li:nth-child(2) > a")
        FILE_NAME = (By.ID, "id_filename")
        SEARCH_BUTTON = (By.CSS_SELECTOR, ".ux-ctl-form-action-buttons")
        FIRST_ROW_STATUS = (By.CSS_SELECTOR, "tbody tr:nth-of-type(1) td:nth-of-type(4) span")
        FIRST_ROW_FAILED_COUNT = (By.CSS_SELECTOR, "tbody tr:nth-of-type(1) td:nth-of-type(6) .alignRight")
        DATA_UPLOADER = (By.CSS_SELECTOR, '.menu_node_home_uploads_datauploader')
