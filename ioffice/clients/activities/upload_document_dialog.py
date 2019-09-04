import utils
from ioffice.adviser_search_dialog import *


class UploadDocumentToTaskDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = UploadDocumentToTaskDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_file_type(self):
        self.page.click(self.Locators.FILE_RADIO_BUTTON)
        return self

    def send_file_url(self):
        utils.send_file_to_element(self, self.Locators.BROWSE_BUTTON_INPUT, utils.get_test_documents_file_url("UploadDocument.pdf"))
        return self

    def click_upload_button(self):
        self.page.click(self.Locators.UPLOAD_BUTTON)
        return self

    class Locators(object):
        FILE_RADIO_BUTTON = (By.ID, "UploadType_1")
        BROWSE_BUTTON_INPUT ="grpUpload_2_2"
        UPLOAD_BUTTON = (By.CSS_SELECTOR, "#grpUpload_2_2_upload")
        FRAME = (By.XPATH, "// iframe[contains(@src,'/nio/DocumentUpload')]")