from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class RecommendationViewDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = RecommendationViewDialog.Locators.FRAME
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_close(self):
        self.page.click(RecommendationViewDialog.Locators.CLOSE_BUTTON)
        return self

    def get_firm_commentary(self):
        return self.page.get_text(RecommendationViewDialog.Locators.FIRM_COMMENTARY_TEXT_BOX)

    def get_rebalance_table_rows(self):
        return self.page.get_table_rows(RecommendationViewDialog.Locators.TABLE_ROWS)

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='/nio/Recommendation/']")
        CLOSE_BUTTON = (By.CSS_SELECTOR, "[class='actions ux-ctl-form-actions'] a")
        FIRM_COMMENTARY_TEXT_BOX = (By.ID, "id_Rebalance_Commentary")
        TABLE_ROWS = (By.CSS_SELECTOR, "#grid_grdRebalance tbody tr")
