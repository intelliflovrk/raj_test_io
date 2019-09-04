from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class DeleteServiceCaseDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = DeleteServiceCaseDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_delete(self):
        self.page.click(DeleteServiceCaseDialog.Locators.DELETE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='DeleteAdviceCase']")
        DELETE_BUTTON = (By.XPATH, "//a[text()='Delete']")
