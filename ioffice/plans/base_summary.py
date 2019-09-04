from ioffice.plans.base import *


class BasePlanSummaryPage(BasePlanPage):

    def is_title_matches(self):
        return "Adviser Workplace | Clients | Plans | Plans | Intelligent Office" == self.driver.title

    def open_first_plan(self):
        return self.click(BasePlanSummaryPage.Locators.FIRST_PLAN_IOB_LINK)

    class Locators(object):
        FIRST_PLAN_IOB_LINK = (By.XPATH, "//*[starts-with(@id, 'ClientPlansGrid')]/td[2]/a")
