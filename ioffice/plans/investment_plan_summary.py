from ioffice.plans.base_summary import *


class InvestmentPlanSummaryPage(BasePlanSummaryPage):

    def get_total_lumpsum_value(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(InvestmentPlanSummaryPage.Locators.TOTAL_LUMP_SUM_VALUE)).text

    def get_current_regular_contribution_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvestmentPlanSummaryPage.Locators.CURRENT_REGULAR_CONTRIBUTION_VALUE)).text

    class Locators(object):
        TOTAL_LUMP_SUM_VALUE = (By.ID, "id_TotalLumpSum_ro")
        CURRENT_REGULAR_CONTRIBUTION_VALUE = (By.ID, "id_PolicyBusiness_TotalRegularPremium_ro")
