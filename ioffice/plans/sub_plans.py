from ioffice.plans.base import *


class PlanSubPlanPage(BasePlanPage):

    def is_title_matches(self):
        return "Adviser Workplace | Clients | Plans | Plans | Intelligent Office" == self.driver.title

    def get_plan_type_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PlanSubPlanPage.Locators.PLAN_TYPE_VALUE)).text

    def click_open_sub_plan(self):
        return self.click(self.Locators.OPEN_SUB_PLAN)

    class Locators(object):
        PLAN_TYPE_VALUE = (By.XPATH, "//table/tbody//td[3]/span")
        OPEN_SUB_PLAN = (By.CSS_SELECTOR, "[title='Open']")
