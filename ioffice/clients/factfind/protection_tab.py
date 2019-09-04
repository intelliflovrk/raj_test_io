from selenium.webdriver.common.by import By

from ioffice.clients.factfind.base import BaseFactFindPage


class ProtectionTab(BaseFactFindPage):

    def click_life_critical_illness_tab(self):
        return self.click(ProtectionTab.Locators.LIFE_CRITICAL_ILLNESS_SUB_TAB)

    def click_income_protection_sub_tab(self):
        return self.click(ProtectionTab.Locators.INCOME_PROTECTION_SUB_TAB)

    def click_protection_summary_sub_tab(self):
        return self.click(ProtectionTab.Locators.PROTECTION_SUMMARY_TAB)

    def click_existing_provision_sub_tab(self):
        return self.click(ProtectionTab.Locators.EXISTING_PROVISION)

    def click_buildings_contents_tab(self):
        return self.click(ProtectionTab.Locators.BUILDINGS_CONTENTS_SUB_TAB)

    class Locators(object):
        DESELECT_EXISTING_PROTECTION_RADIO_BUTTON = (By.ID, "No_589_HasExistingProvision_0")
        BUILDINGS_CONTENTS_SUB_TAB = (By.ID, "buildingsandcontents")
        LIFE_CRITICAL_ILLNESS_SUB_TAB = (By.ID, "lifecoverandcic")
        INCOME_PROTECTION_SUB_TAB = (By.ID, "incomeprotection")
        EXISTING_PROVISION = (By.ID, "protectionprovision")
        PROTECTION_SUMMARY_TAB = (By.ID, "protectionsummary")
