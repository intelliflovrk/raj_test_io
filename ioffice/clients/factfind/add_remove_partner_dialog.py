from selenium.webdriver.common.by import By
from ioffice.base import IOFrameDialog
from pageobjects import BasePageSection


class AddRemovePartnerDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.FRAME = AddRemovePartnerDialog.Locators._FRAME
        self.frame_locator = self.FRAME
        self._switch_to_frame()

    def click_add_first_partner(self):
        self.page.click(AddRemovePartnerDialog.Locators.ADD_BUTTON)
        return self

    def click_remove_first_partner(self):
        self.page.click(AddRemovePartnerDialog.Locators.REMOVE_BUTTON)
        return self

    def get_partner_name(self):
        return self.page.get_text(AddRemovePartnerDialog.Locators.CLIENT_NAME)

    class Locators(object):
        _FRAME = (By.XPATH, "//iframe")
        ADD_BUTTON = (By.XPATH, "//a[text()='Add']")
        LINE_LOCATOR = (By.ID, "grid_id_root_2_2_3")
        CLIENT_NAME = (By.CSS_SELECTOR, "#grid_id_root_2_2_3 td span")
        REMOVE_BUTTON = (By.XPATH, "//a[text()='Remove']")

