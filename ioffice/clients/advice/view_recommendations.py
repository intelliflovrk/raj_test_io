from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection
from ioffice.clients.base import BaseClientPage
from ioffice.clients.advice.planning_tabs_section import PlanningTabsSection


class ViewRecommendationsPage(BaseClientPage):

    def __init__(self, config):
        super().__init__(config)
        self.planning_tabs = PlanningTabsSection(self)

    def hover_over_recommendations_actions(self):
        self.hover_over(ViewRecommendationsPage.Locators.RECOMMENDATION_ACTIONS_MENU)
        return RecommendationsActionsMenuSection(self)

    def click_first_transaction_details_button(self):
        return self.click(ViewRecommendationsPage.Locators.FIRST_TRANSACTION_DETAILS_BUTTON)

    def click_first_accept_button(self):
        return self.click(ViewRecommendationsPage.Locators.ACCEPT_BUTTONS)

    def click_first_sequential_ref_link(self):
        return self.click(ViewRecommendationsPage.Locators.SEQUENTIAL_REF_LINKS)

    def click_first_select_radio_button(self):
        return self.click(ViewRecommendationsPage.Locators.SELECT_RADIO_BUTTONS)

    class Locators(object):
        RECOMMENDATION_ACTIONS_MENU = (By.ID, "secondary")
        FIRST_TRANSACTION_DETAILS_BUTTON = (By.CSS_SELECTOR, "a[id*='transactionDetails']")
        ACCEPT_BUTTONS = (By.CSS_SELECTOR, "a[id*='AcceptRecommendation']")
        SEQUENTIAL_REF_LINKS = (By.CSS_SELECTOR, "a[href*='SummaryPlan']")
        SELECT_RADIO_BUTTONS = (By.CSS_SELECTOR, "#tblRecommendations tbody tr [type='radio']")


class RecommendationsActionsMenuSection(BasePageSection):
    def click_add_manual_rec(self):
        self.page.click(RecommendationsActionsMenuSection.Locators.ADD_MANUAL_REC_LINK)
        return self

    def click_delete_recommendations(self):
        self.page.click(RecommendationsActionsMenuSection.Locators.DELETE_RECOMMENDATIONS_LINK)
        return self

    class Locators(object):
        ADD_MANUAL_REC_LINK = (By.CSS_SELECTOR, "a[onclick*='AddManualRecommendation']")
        DELETE_RECOMMENDATIONS_LINK = (By.CSS_SELECTOR, "a[onclick*='DeleteRecommendations']")
