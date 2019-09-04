from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class DeleteBinderDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_yes(self):
        self.page.click(DeleteBinderDialog.Locators.YES_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='Binder']")
        YES_BUTTON = (By.XPATH, "//form//a[text()='Yes']")
