from ioffice.plans.base import *


class PlanContributionsPage(BasePlanPage):

    def get_contribution_id(self):
        return self.get_attribute(self.Locators.FIRST_CONTRIBUTION_ID, "value")

    def get_amount(self):
        return self.get_text(self.Locators.FIRST_AMOUNT)

    def get_start_date(self):
        return self.get_text(self.Locators.FIRST_START_DATE)

    class Locators(object):
        FIRST_START_DATE = (By.XPATH, "//*[@id='grid_ec1Grid']/tbody/tr[1]/td[7]/span")
        FIRST_AMOUNT = (By.CSS_SELECTOR, "tbody td:nth-of-type(4) .alignRight")
        FIRST_CONTRIBUTION_ID = (By.XPATH, "//*[@id='grid_ec1Grid']//td[1]/input")