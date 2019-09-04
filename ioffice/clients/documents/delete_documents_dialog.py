from ioffice.base import IOFrameDialog
from pageobjects import BasePageSection
from selenium.webdriver.common.by import By


class DeleteDocumentDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_yes(self):
        self.page.click(self.Locators.YES_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.XPATH, "// iframe[contains(@src,'Delete')]")
        YES_BUTTON = (By.ID, "id_root_2_2_2_3")
