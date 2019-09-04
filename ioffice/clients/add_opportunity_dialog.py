from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AddOpportunityDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = AddOpportunityDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_first_campaign_type(self):
        self.page.select_by_index(AddOpportunityDialog.Locators.CAMPAIGN_TYPE_SELECT_BOX, 1)
        return self

    def click_save(self):
        self.page.click(AddOpportunityDialog.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='AddOpportunity']")
        CAMPAIGN_TYPE_SELECT_BOX = (By.ID, "id_CampaignTypeId")
        SAVE_BUTTON = (By.CSS_SELECTOR, "a[onclick*='SaveOpportunity']")
