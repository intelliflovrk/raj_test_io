from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AddDocumentsToBinderDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_add(self):
        self.page.click(AddDocumentsToBinderDialog.Locators.ADD_BUTTON)
        return self

    def select_binder(self, text):
        self.page.select_by_visible_text(AddDocumentsToBinderDialog.Locators.BINDER_SELECT_BOX, text)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='AddToBinder']")
        BINDER_SELECT_BOX = (By.ID, "id_Binder")
        ADD_BUTTON = (By.XPATH, "//form//a[text()='Add']")