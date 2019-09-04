from selenium.webdriver.common.by import By
from ioffice.base import IOBasePage, IOFrameDialog
from utils import get_test_documents_file_url, send_file_to_element


class DownloadTemplateDialog(IOBasePage, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, DownloadTemplateDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_import_leads(self):
        return self.click(DownloadTemplateDialog.Locators.IMPORT_LEADS)

    def click_close_button(self):
        return self.click(DownloadTemplateDialog.Locators.CLOSE)

    class Locators:
        IMPORT_LEADS = (By.XPATH, "//*[contains(@id, 'ListDownloadTemplates__04f52d48-fbaa-4fc8-a95d-ebf5ac2c596b')]//a[contains(@title, 'Download')]")
        CLOSE = (By.CSS_SELECTOR, ".ux-ctl-form-action-buttons")
        _FRAME = "//iframe[@src='/nio/FileImportTemplate/ListTemplates']"


class ImportCompleteTemplateDialog(IOBasePage, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, ImportCompleteTemplateDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_import_type(self, data):
        return self.select_by_visible_text(ImportCompleteTemplateDialog.Locators.IMPORT_TYPE, data)

    def send_file_url(self):
        send_file_to_element(self, self.Locators.BROWSE_BUTTON_INPUT_ID, get_test_documents_file_url("LeadsImport.csv"))
        return self

    def click_upload_button(self):
        return self.click(ImportCompleteTemplateDialog.Locators.UPLOAD_BUTTON)

    class Locators:
        IMPORT_TYPE = (By.CSS_SELECTOR, "#id_FileImportType")
        UPLOAD_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_3_2_2_6_upload")
        _FRAME = "//iframe[@src='/nio/fileimportdefault/DefaultFileImport']"
        BROWSE_BUTTON_INPUT_ID = 'id_root_2_2_3_2_2_6'

