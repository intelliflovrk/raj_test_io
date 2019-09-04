from ioffice.plans.base_summary import *


class RetirementPlanSummaryPage(BasePlanSummaryPage):

    def get_total_single_contribution(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(RetirementPlanSummaryPage.Locators.TOTAL_SINGLE_CONTRIBUTION)).text

    def get_current_regular_contribution_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RetirementPlanSummaryPage.Locators.CURRENT_REGULAR_CONTRIBUTION_VALUE)).text

    class Locators(object):
        TOTAL_SINGLE_CONTRIBUTION = (By.ID, "id_TotalLumpSum_ro")
        CURRENT_REGULAR_CONTRIBUTION_VALUE = (By.ID, "id_PremiumAmount_ro")
