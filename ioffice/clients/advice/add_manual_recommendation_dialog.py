from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AddManualRecommendationDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = AddManualRecommendationDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_existing_plan(self, plan_id):
        self.page.select_by_value(AddManualRecommendationDialog.Locators.EXISTING_PLAN_SELECT_BOX, plan_id)
        return self

    def click_model_portfolio(self):
        self.page.click(AddManualRecommendationDialog.Locators.MODEL_PORTFOLIO_RADIO_BUTTON)
        return self

    def click_add(self):
        self.page.click(AddManualRecommendationDialog.Locators.ADD_BUTTON)
        return self

    def click_save(self):
        self.page.click(AddManualRecommendationDialog.Locators.SAVE_BUTTON)
        return self

    def fill_in_recommendation_name(self, rec_name_text):
        self.page.fill_in_field(AddManualRecommendationDialog.Locators.RECOMMENDATION_NAME_TEXT_BOX, rec_name_text)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='AddManualRecommendation']")
        EXISTING_PLAN_SELECT_BOX = (By.ID, "PlanDropDown")
        MODEL_PORTFOLIO_RADIO_BUTTON = (By.ID, "FundTypeId_3")
        ADD_BUTTON = (By.ID, "FundTypeSelectionAjaxId_2")
        SAVE_BUTTON = (By.ID, "ManualRecommendation_4")
        RECOMMENDATION_NAME_TEXT_BOX = (By.ID, "id_RecommendationName")
