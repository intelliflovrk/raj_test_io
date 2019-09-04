from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ioffice.clients.factfind.protection_tab import ProtectionTab
from pageobjects import EC


class IncomeProtectionTab(ProtectionTab):

    def click_unable_to_work_illness_yes_radio_button(self):
        return self.click(IncomeProtectionTab.Locators.UNABLE_TO_WORK_ILLNESS_YES_RADIO_BUTTON)

    def click_unable_to_work_illness_no_radio_button(self):
        return self.click(IncomeProtectionTab.Locators.UNABLE_TO_WORK_ILLNESS_NO_RADIO_BUTTON)

    def click_unable_to_work_illness_not_applicable_radio_button(self):
        return self.click(IncomeProtectionTab.Locators.UNABLE_TO_WORK_ILLNESS_NOT_APPLICABLE_RADIO_BUTTON)

    def click_unable_to_work_unemployment_yes_radio_button(self):
        return self.click(IncomeProtectionTab.Locators.UNABLE_TO_WORK_UNEMPLOYMENT_YES_RADIO_BUTTON)

    def click_unable_to_work_unemployment_no_radio_button(self):
        return self.click(IncomeProtectionTab.Locators.UNABLE_TO_WORK_UNEMPLOYMENT_NO_RADIO_BUTTON)

    def click_unable_to_work_unemployment_not_applicable_radio_button(self):
        return self.click(IncomeProtectionTab.Locators.UNABLE_TO_WORK_UNEMPLOYMENT_NOT_APPLICABLE_RADIO_BUTTON)

    def get_impact_on_customer_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(IncomeProtectionTab.Locators.IMPACT_ON_CUSTOMER)).text

    def get_impact_on_dependants_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(IncomeProtectionTab.Locators.IMPACT_ON_DEPENDANTS)).text

    def get_address_this_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(IncomeProtectionTab.Locators.ADDRESS_THIS_TEXTFIELD)).text

    def get_not_reviewing_reason_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(IncomeProtectionTab.Locators.REASON_NOT_REVIEW)).text

    def get_unable_to_work_illness_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                IncomeProtectionTab.Locators.UNABLE_TO_WORK_ILLNESS_YES_RADIO_BUTTON)).is_selected()

    def get_unable_to_work_illness_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                IncomeProtectionTab.Locators.UNABLE_TO_WORK_ILLNESS_NO_RADIO_BUTTON)).is_selected()

    def get_unable_to_work_illness_not_applicable_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                IncomeProtectionTab.Locators.UNABLE_TO_WORK_ILLNESS_NOT_APPLICABLE_RADIO_BUTTON)).is_selected()

    def get_unable_to_work_unemployment_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                IncomeProtectionTab.Locators.UNABLE_TO_WORK_UNEMPLOYMENT_YES_RADIO_BUTTON)).is_selected()

    def get_unable_to_work_unemployment_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                IncomeProtectionTab.Locators.UNABLE_TO_WORK_UNEMPLOYMENT_NO_RADIO_BUTTON)).is_selected()

    def get_unable_to_work_unemployment_not_applicable_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                IncomeProtectionTab.Locators.UNABLE_TO_WORK_UNEMPLOYMENT_NOT_APPLICABLE_RADIO_BUTTON)).is_selected()

    class Locators(object):
        UNABLE_TO_WORK_ILLNESS_YES_RADIO_BUTTON = (By.ID, "Yes_IsDebtMaintainable_IsDebtMaintainable_0")
        UNABLE_TO_WORK_ILLNESS_NO_RADIO_BUTTON = (By.ID, "No_IsDebtMaintainable_IsDebtMaintainable_0")
        UNABLE_TO_WORK_ILLNESS_NOT_APPLICABLE_RADIO_BUTTON = (By.ID, "NA_IsDebtMaintainable_IsDebtMaintainable_0")
        UNABLE_TO_WORK_UNEMPLOYMENT_YES_RADIO_BUTTON = (By.ID, "Yes_IsLifestyleMaintainable_IsLifestyleMaintainable_0")
        UNABLE_TO_WORK_UNEMPLOYMENT_NO_RADIO_BUTTON = (By.ID, "No_IsLifestyleMaintainable_IsLifestyleMaintainable_0")
        UNABLE_TO_WORK_UNEMPLOYMENT_NOT_APPLICABLE_RADIO_BUTTON = (
        By.ID, "NA_IsLifestyleMaintainable_IsLifestyleMaintainable_0")
        IMPACT_ON_CUSTOMER = (By.ID, "IPImpactOnYou_ImpactOnYou_0")
        IMPACT_ON_DEPENDANTS = (By.ID, "IPImpactOnDependants_ImpactOnDependants_0")
        ADDRESS_THIS_TEXTFIELD = (By.ID, "IPHowToAddress_HowToAddress_0")
        REASON_NOT_REVIEW = (By.ID, "IPNotReviewingReason_NotReviewingReason_0")
