from ioffice.base import IOFrameDialog
from ioffice.wizard import *
from selenium.webdriver.common.by import By


class ViewPDFSDialog(BasePageSection, IOFrameDialog):
    def __init__(self, client_id, factfind_ref, parent_page):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, ViewPDFSDialog.Locators._FRAME.format(client_id, factfind_ref))
        self.frame_locator = self.FRAME
        self._switch_to_frame()

    def click_add_document_button(self):
        return self.page.click(ViewPDFSDialog.Locators.ADD_DOCUMENT_BUTTON)

    def click_close_button(self):
        return self.page.click(ViewPDFSDialog.Locators.CLOSE_BUTTON)

    def click_open_first_document(self):
        return self.page.click(ViewPDFSDialog.Locators.OPEN_FIRST_DOCUMENT_LINK)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/ClientFactFind/{0}/ViewPdfs/{1}']"
        CLOSE_BUTTON = (By.LINK_TEXT, "Close")
        ADD_DOCUMENT_BUTTON = (By.LINK_TEXT, "Add Document")
        OPEN_FIRST_DOCUMENT_LINK = (By.XPATH, "//a[text()='Open']")
