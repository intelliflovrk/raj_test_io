from selenium.webdriver.common.by import By
from ioffice.plans.base import BasePlanPage


class PlanDocumentsPage(BasePlanPage):

    def click_first_profile_link(self):
        return self.click(self.Locators.FIRST_PROFILE_LINK)

    class Locators(object):
        FIRST_PROFILE_LINK = (By.CSS_SELECTOR, "a[href*='DocumentProfile']")
