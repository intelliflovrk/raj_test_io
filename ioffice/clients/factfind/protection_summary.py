from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ioffice.clients.factfind.protection_tab import ProtectionTab
from pageobjects import EC


class SummaryProtectionSubTab(ProtectionTab):

    def get_life_cover_sum(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.Locators.LIFE_COVER_SUM_READONLY_FIELD)).get_attribute("value")

    def get_illness_cover_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.Locators.LIFE_COVER_SUM_READONLY_FIELD)).get_attribute("value")

    class Locators(object):
        LIFE_COVER_SUM_READONLY_FIELD = (By.ID, "PsExistingLife_ExistingLife_0")
        EXISTING_AMOUNT_OF_ILLNESS_COVER = (By.ID, "PsExistingIllness_ExistingLifeCriticalIllness_0")