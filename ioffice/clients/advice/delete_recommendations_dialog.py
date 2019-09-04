from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class DeleteRecommendationsDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = DeleteRecommendationsDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def tick_select_all(self):
        self.page.click(DeleteRecommendationsDialog.Locators.SELECT_ALL_CHECK_BOX)
        return self

    def click_delete(self):
        self.page.click(DeleteRecommendationsDialog.Locators.DELETE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='DeleteRecommendations']")
        SELECT_ALL_CHECK_BOX = (By.CSS_SELECTOR, "#grid_grdRecommendations thead [type='checkbox']")
        DELETE_BUTTON = (By.CSS_SELECTOR, "a[onclick*='DeleteSelectedRecommendations']")
