from ioffice.clients.opportunities.base import BaseOpportunitiesPage
from ioffice.base import *


class OpportunitiesPage(BaseOpportunitiesPage):
    def verify_opportunity_exists(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(OpportunitiesPage.Locators.TABLE_FIRST_ROW, "Mortgage"))

    def get_opportunity_type(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.Locators.OPPORTUNITY_TYPE)).text

    def click_open(self, opportunity_id):
        return self.click((By.CSS_SELECTOR, OpportunitiesPage.Locators._OPEN_LINK.format(opportunity_id)))

    class Locators(object):
        TABLE_FIRST_ROW = (By.CSS_SELECTOR, "#sidebar-container table tbody tr:not(.filter)")
        OPPORTUNITY_TYPE = (By.XPATH, "//*[@id='grid_OpportunitiesGrid']/tbody/tr/td[3]")
        _OPEN_LINK = "a[href*='ViewOpportunity/{0}']"
