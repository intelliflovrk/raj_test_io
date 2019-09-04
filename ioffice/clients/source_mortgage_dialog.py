from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class SourceMortgageDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, self.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_mortgage_brain_anywhere_radio_button(self):
        self.page.click(self.Locators.MORTGAGE_BRAIN_ANYWHERE_RADIO_BUTTON)
        return self

    def click_next_button(self):
        self.page.click(self.Locators.NEXT_BUTTON)
        return self

    class Locators(object):
        _FRAME = "// iframe[contains(@src,'/nio/')]"
        MORTGAGE_BRAIN_ANYWHERE_RADIO_BUTTON = (By.ID, "id_RefApplicationId_1")
        NEXT_BUTTON = (By.ID, "id_root_2_2_2_7")
