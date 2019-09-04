from ioffice.plans.base import BasePlanPage, By


class PlanRecommendationsTabPage(BasePlanPage):

    def click_details(self):
        return self.click(PlanRecommendationsTabPage.Locators.DETAILS_BUTTON)

    def get_recommendations_table_rows(self):
        return self.get_table_rows(PlanRecommendationsTabPage.Locators.TABLE_ROWS)

    class Locators(object):
        DETAILS_BUTTON = (By.CSS_SELECTOR, "#grid_grdRecommendations [id*='grdRecommendations'] a")
        TABLE_ROWS = (By.CSS_SELECTOR, "#grid_grdRecommendations tbody tr")
