from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection, IOFrameDialog


class AddSchemeMemberDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.frame_locator = AddSchemeMemberDialog.Locators.FRAME
        self._switch_to_frame()

    def click_save(self):
        self.page.click(self.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='addschememembers']")
        SAVE_BUTTON = (By.ID, "id_root_2_2_3_4")
