from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AddToWrapperDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.frame_locator = AddToWrapperDialog.Locators.FRAME
        self.prev_frame_locator = None
        self._switch_to_frame()

    def click_first_radio_button(self):
        self.page.click(AddToWrapperDialog.Locators.FIRST_RADIO_BUTTON)
        return self

    def click_link_button(self):
        self.page.click(AddToWrapperDialog.Locators.LINK_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='ViewPlanToWrapper']")
        FIRST_RADIO_BUTTON = (By.CSS_SELECTOR, '[id="id_root_2_2_2"] [type="radio"]')
        LINK_BUTTON = (By.ID, 'id_root_2_2_2_8')
