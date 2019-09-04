import os
from selenium.webdriver.common.by import By
import utils
from ioffice.base import IOBasePage, IOFrameDialog


class ImportProviderStatementDialog(IOBasePage, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, self.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def send_unique_file(self, file_name):
        self.config.unique_file_url = utils.get_test_documents_file_url(file_name)
        os.renames(utils.get_test_documents_file_url(utils.get_common_data(
            self.config)["test_data"]["provider_statement_data"][self.config.file_name]), self.config.unique_file_url)
        utils.send_file_to_element(self, self.Locators.BROWSE_BUTTON_INPUT_ID, self.config.unique_file_url)
        return self

    def click_run_button(self):
        self.click(self.Locators.RUN_BUTTON)
        return self

    class Locators:
        RUN_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_2_3")
        _FRAME = "//iframe[@src='/nio/providerstatement/ImportCsv']"
        BROWSE_BUTTON_INPUT_ID = 'FileUpload-fileinput'
