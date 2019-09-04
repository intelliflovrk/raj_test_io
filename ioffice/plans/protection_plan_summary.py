from ioffice.plans.base_summary import *


class ProtectionPlanSummaryPage(BasePlanSummaryPage):

    def get_premium_id(self):
        return self.get_attribute(self.Locators.FIRST_PREMIUM_ID, "value")

    def get_premium_amount(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(ProtectionPlanSummaryPage.Locators.PREMIUM_AMOUNT_VALUE)).text

    def get_premium_frequency(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(ProtectionPlanSummaryPage.Locators.PREMIUM_FREQUENCY_VALUE)).text

    def get_premium_start_date(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(ProtectionPlanSummaryPage.Locators.PREMIUM_START_DATE_VALUE)).text

    def get_life_cover_sum_assured_value(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(ProtectionPlanSummaryPage.Locators.LIFE_COVER_SUM_ASSURED_VALUE)).get_attribute('value')

    def get_life_cover_term_value(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(ProtectionPlanSummaryPage.Locators.LIFE_COVER_TERM_VALUE)).get_attribute('value')

    class Locators(object):
        PREMIUM_AMOUNT_VALUE = (By.ID, "id_PremiumAmount_ro")
        PREMIUM_FREQUENCY_VALUE = (By.XPATH, "//*[@id='id_PremiumFrequencyId']/option")
        PREMIUM_START_DATE_VALUE = (By.ID, "PremiumEndDate_ro")
        LIFE_COVER_SUM_ASSURED_VALUE = (By.ID, "id_SumAssuredLifeCover")
        LIFE_COVER_TERM_VALUE = (By.ID, "id_LifeCoverTerm")
        FIRST_PREMIUM_ID = (By.CSS_SELECTOR, "#id_PremiumPolicyMoneyInId")
