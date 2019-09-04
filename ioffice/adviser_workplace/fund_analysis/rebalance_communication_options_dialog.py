from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class RebalanceCommunicationOptionsDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def get_models_that_apply_checkbox_elements(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_all_elements_located(
            RebalanceCommunicationOptionsDialog.Locators.MODELS_THAT_APPLY_CHECKBOXES))

    def click_model_that_apply(self, model_name):
        self.page.click((By.XPATH, RebalanceCommunicationOptionsDialog.Locators._MODEL_THAT_APPLY_CHECKBOX.format(model_name)))
        return self

    def fill_in_rebalance_recommendation_commentary(self, commentary_text):
        self.page.fill_in_field(RebalanceCommunicationOptionsDialog.Locators.REBALANCE_RECOMMENDATION_COMMENTARY_TEXT_BOX, commentary_text)
        return self

    def fill_in_model_update_recommendation_commentary(self, commentary_text):
        self.page.fill_in_field(RebalanceCommunicationOptionsDialog.Locators.MODEL_UPDATE_RECOMMENDATION_COMMENTARY_TEXT_BOX, commentary_text)
        return self

    def fill_in_no_action_recommendation_commentary(self, commentary_text):
        self.page.fill_in_field(RebalanceCommunicationOptionsDialog.Locators.NO_ACTION_RECOMMENDATION_COMMENTARY_TEXT_BOX, commentary_text)
        return self

    def click_proceed(self):
        self.page.click(RebalanceCommunicationOptionsDialog.Locators.PROCEED_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src='/nio/fundanalysis/rebalanceoptions']")
        MODELS_THAT_APPLY_CHECKBOXES = (By.CSS_SELECTOR, "#id_root_2_2_5_4 input:not([disabled])")
        _MODEL_THAT_APPLY_CHECKBOX = "//*[@id='id_root_2_2_5_4']//span[contains(text(), '{0}')]//preceding-sibling::input"
        REBALANCE_RECOMMENDATION_COMMENTARY_TEXT_BOX = (By.ID, "RebalanceCommentary")
        MODEL_UPDATE_RECOMMENDATION_COMMENTARY_TEXT_BOX = (By.ID, "ModelUpdateCommentary")
        NO_ACTION_RECOMMENDATION_COMMENTARY_TEXT_BOX = (By.ID, "NoActionCommentary")
        PROCEED_BUTTON = (By.CSS_SELECTOR, "[onclick*='RebalanceOptions']")
