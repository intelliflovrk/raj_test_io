import utils
from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class UploadDocumentDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = UploadDocumentDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_file_type(self):
        self.page.click(self.Locators.FILE_RADIO_BUTTON)
        return self

    def send_file_url(self):
        utils.send_file_to_element(self, self.Locators.BROWSE_BUTTON_INPUT, utils.get_test_documents_file_url("UploadDocument.pdf"))
        return self

    def select_document_category(self, data):
        self.page.select_by_visible_text(self.Locators.CATEGORY_SELECT_BOX, data)
        return self

    def select_document_subcategory(self, data):
        self.page.select_by_visible_text(self.Locators.SUB_CATEGORY_SELECT_BOX, data)
        return self

    def click_upload_button(self):
        self.page.click(self.Locators.UPLOAD_BUTTON)
        return self

    class Locators(object):
        FILE_RADIO_BUTTON = (By.ID, "UploadType_1")
        BROWSE_BUTTON_INPUT ="grpUpload_2_2"
        UPLOAD_BUTTON = (By.ID, "grpUpload_2_2_upload")
        FRAME = (By.CSS_SELECTOR, "iframe")
        CATEGORY_SELECT_BOX = (By.ID, "CategoryId")
        SUB_CATEGORY_SELECT_BOX = (By.ID, "SubCategoryId")
