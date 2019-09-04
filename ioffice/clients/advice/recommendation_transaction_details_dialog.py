from ioffice.base import BasePageSection, IOFrameDialog, WebDriverWait, EC, By


class RecommendationTransactionDetailsDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = RecommendationTransactionDetailsDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def get_funds_names(self):
        return WebDriverWait(self.driver, self.TIMEOUT) \
            .until(EC.presence_of_all_elements_located(RecommendationTransactionDetailsDialog.Locators.FUND_NAME_TABLE_CELL))

    def click_close(self):
        self.page.click(RecommendationTransactionDetailsDialog.Locators.CLOSE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='ClientTransactionDetails']")
        FUND_NAME_TABLE_CELL = (By.CSS_SELECTOR, "tbody tr .first")
        CLOSE_BUTTON = (By.ID, "Close")
