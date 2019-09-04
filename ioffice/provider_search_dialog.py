from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By

class ProviderSearchDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame):
        super().__init__(parent_page)
        self.frame_locator = ProviderSearchDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()
    
    def select(self, provider_text):
        self.page.select_by_visible_text(ProviderSearchDialog.Locators.SELECT_BOX, provider_text)
        return self
    
    def click_ok_button(self):
        self.page.click(ProviderSearchDialog.Locators.OK_BUTTON)
        return self
        
    class Locators(object): 
        FRAME = (By.XPATH,"// iframe[contains(@src,'/nio/ProductProvider')]")
        SELECT_BOX = (By.ID, "ProviderListDropDown")
        OK_BUTTON = (By.XPATH, "//a[text()='OK']")


class FullProviderSearchDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame):
        super().__init__(parent_page)
        self.frame_locator = FullProviderSearchDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select(self, provider_text):
        self.page.select_by_visible_text(ProviderSearchDialog.Locators.SELECT_BOX, provider_text)
        return self

    def click_ok_button(self):
        self.page.click(ProviderSearchDialog.Locators.OK_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.XPATH,"// iframe[contains(@src,'/nio/ProductProvider')]")
        SELECT_BOX = (By.ID, "ProviderListDropDown")
        OK_BUTTON = (By.XPATH, "//a[text()='OK']")
