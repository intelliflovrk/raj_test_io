from selenium.webdriver.common.by import By
from ioffice.base import IOFrameDialog
from ioffice.clients.base import BaseClientPage
from pageobjects import BasePageSection


class ClientRestrictProcessing(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.client_id = BaseClientPage(self.config).get_client_id()
        self.FRAME = (By.XPATH, ClientRestrictProcessing.Locators._FRAME.format(self.client_id))
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_confirm_button(self):
        return self.page.click(ClientRestrictProcessing.Locators.CONFIRM_BUTTON)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/Client/{0}/RestrictProcessing']"
        CONFIRM_BUTTON = (By.ID, "id_root_2_2_2_4")
