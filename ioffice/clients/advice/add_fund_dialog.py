from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AddFundDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame):
        super().__init__(parent_page)
        self.frame_locator = AddFundDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_model_portfolio(self, model_portfolio_name):
        self.page.select_by_visible_text(AddFundDialog.Locators.MODEL_PORTFOLIO_SELECT_BOX, model_portfolio_name)
        return self

    def click_return_chosen_funds(self):
        self.page.click(AddFundDialog.Locators.RETURN_CHOSEN_FUNDS_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='AddNewFund']")
        MODEL_PORTFOLIO_SELECT_BOX = (By.ID, "id_Id")
        RETURN_CHOSEN_FUNDS_BUTTON = (By.CSS_SELECTOR, "a[onclick*='ReturnModelPortfolio']")
