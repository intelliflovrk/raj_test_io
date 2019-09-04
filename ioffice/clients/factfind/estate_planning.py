from selenium.webdriver.common.by import By
from ioffice.clients.factfind.base import BaseFactFindPage
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects import EC


class EstatePlanningStage(BaseFactFindPage):

    def fill_in_estate_planning_fields(self, locator, data):
        return self.fill_in_field(locator, data)

    def click_current_position_subtab(self):
        return self.click(EstatePlanningStage.Locators.NEEDS_AND_PRIORITIES)

    def click_goals_subtab(self):
        return self.click(EstatePlanningStage.Locators.GOALS)

    def click_next_steps_subtab(self):
        return self.click(EstatePlanningStage.Locators.NEXT_STEPS)

    class Locators(BaseFactFindPage):
        GOALS = (By.CSS_SELECTOR, "#estateplanningneeds > a")
        NEEDS_AND_PRIORITIES = (By.CSS_SELECTOR, "#currentestateplanning > a")
        NEXT_STEPS = (By.CSS_SELECTOR, "#estatenextsteps > a")

    class Goals(BaseFactFindPage):

        def get_goals_form_value(self):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    self.Locators.GOALS_OR_NEEDS)).text

        class Locators(object):
            GOALS_OR_NEEDS = (By.ID, "624_GoalsAndNeeds_0")

    class CurrentPosition(BaseFactFindPage):

        def get_current_position_broad_content_value(self):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    self.Locators.BROAD_CONTENT)).text

        class Locators(object):
            BROAD_CONTENT = (By.ID, "626_BroadContent_0")
            GIFTS_OF_CAPITAL = (By.ID, "630_CapitalGifts_0")
            GIFTS_OF_TAX_YEAR = (By.ID, "631_UsedAnnualExemption_0")
            REGULAR_GIFTS = (By.ID, "632_RegularGifts_0")
            ANY_INHERITANCE = (By.ID, "Inheritance_Inheritance_0")

    class NextSteps(BaseFactFindPage):

        def get_next_steps_value(self):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    self.Locators.NEXT_STEPS)).text

        class Locators(object):
            NEXT_STEPS = (By.ID, "625_NextSteps_0")
