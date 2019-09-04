from ioffice.plans.base import *


class PlanValuationsPage(BasePlanPage):

    def is_title_matches(self):
        return "Valuations | Intelligent Office" == self.driver.title

    def get_valuation_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PlanValuationsPage.Locators.VALUATION_VALUE)).text

    def check_select_all_valuations(self):
        return self.click(PlanValuationsPage.Locators.SELECT_ALL_CHECKBOX)

    def click_delete(self):
        return self.click(PlanValuationsPage.Locators.DELETE_BUTTON)

    class Locators(object):
        VALUATION_VALUE = (By.XPATH, "//table/tbody//*[contains(text(), '£')]")  # the FIRST row in the grid
        SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, "#grid_ClientPlanValuationsGrid thead input[type='checkbox']")
        DELETE_BUTTON = (By.ID, "ClientPlanValuationsGrid_8")
