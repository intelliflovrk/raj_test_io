from ioffice.base import IOFrameDialog
from ioffice.wizard import *
from selenium.webdriver.common.by import By


class LinkedDocumentsDialog(BasePageSection, IOFrameDialog):
    def __init__(self, client_id, parent_page):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, LinkedDocumentsDialog.Locators._FRAME.format(client_id))
        self.frame_locator = self.FRAME
        self._switch_to_frame()

    def click_close_button(self):
        return self.page.click(LinkedDocumentsDialog.Locators.CLOSE_BUTTON)

    def click_view_button(self):
        return self.page.click(LinkedDocumentsDialog.Locators.VIEW_BUTTON)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/ClientFactFind/{0}/ViewLinkedDocuments']"
        VIEW_BUTTON = (By.XPATH, "//*[@id='id_root_2_2_2__2615204']/td[2]/a")
        CLOSE_BUTTON = (By.XPATH, "//*[@id='form_id_root_2_2_3']/div/div/a")
