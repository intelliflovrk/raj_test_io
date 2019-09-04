from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ioffice.clients.factfind.protection_tab import ProtectionTab
from pageobjects import EC


class LifeCriticalTab(ProtectionTab):

    def click_mortgage_and_debt_yes_radio_button(self):
        return self.click(LifeCriticalTab.Locators.MORTGAGE_AND_DEBT_CLEARED_YES_RADIO_BUTTON)

    def click_mortgage_and_debt_no_radio_button(self):
        return self.click(LifeCriticalTab.Locators.MORTGAGE_AND_DEBT_CLEARED_NO_RADIO_BUTTON)

    def click_mortgage_and_debt_not_applicable_radio_button(self):
        return self.click(LifeCriticalTab.Locators.MORTGAGE_AND_DEBT_CLEARED_NOT_APPLICABLE_RADIO_BUTTON)

    def click_life_standards_critical_illness_yes_radio_button(self):
        return self.click(LifeCriticalTab.Locators.LIFE_STANDARDS_CRITICAL_ILLNESS_YES_RADIO_BUTTON)

    def click_life_standards_critical_illness_no_radio_button(self):
        return self.click(LifeCriticalTab.Locators.LIFE_STANDARDS_CRITICAL_ILLNESS_NO_RADIO_BUTTON)

    def click_life_standards_death_yes_radio_button(self):
        return self.click(LifeCriticalTab.Locators.LIFE_STANDARDS_DEATH_YES_RADIO_BUTTON)

    def click_life_standards_death_no_radio_button(self):
        return self.click(LifeCriticalTab.Locators.LIFE_STANDARDS_DEATH_NO_RADIO_BUTTON)

    def click_life_standards_death_not_applicable_radio_button(self):
        return self.click(LifeCriticalTab.Locators.LIFE_STANDARDS_DEATH_NOT_APPLICABLE_RADIO_BUTTON)

    def click_cost_of_protection_yes_radio_button(self):
        return self.click(LifeCriticalTab.Locators.COST_OF_PROTECTION_YES_RADIO_BUTTON)

    def click_cost_of_protection_no_radio_button(self):
        return self.click(LifeCriticalTab.Locators.COST_OF_PROTECTION_NO_RADIO_BUTTON)

    def get_is_mortgage_debt_cleared_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                LifeCriticalTab.Locators.MORTGAGE_AND_DEBT_CLEARED_YES_RADIO_BUTTON)).is_selected()

    def get_is_mortgage_debt_cleared_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                LifeCriticalTab.Locators.MORTGAGE_AND_DEBT_CLEARED_NO_RADIO_BUTTON)).is_selected()

    def get_is_mortgage_debt_cleared_not_applicable_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                LifeCriticalTab.Locators.MORTGAGE_AND_DEBT_CLEARED_NOT_APPLICABLE_RADIO_BUTTON)).is_selected()

    def get_life_standards_critical_illness_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                LifeCriticalTab.Locators.LIFE_STANDARDS_CRITICAL_ILLNESS_YES_RADIO_BUTTON)).is_selected()

    def get_life_standards_critical_illness_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                LifeCriticalTab.Locators.LIFE_STANDARDS_CRITICAL_ILLNESS_NO_RADIO_BUTTON)).is_selected()

    def get_life_standards_death_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LifeCriticalTab.Locators.LIFE_STANDARDS_DEATH_YES_RADIO_BUTTON)).is_selected()

    def get_life_standards_death_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LifeCriticalTab.Locators.LIFE_STANDARDS_DEATH_NO_RADIO_BUTTON)).is_selected()

    def get_life_standards_death_not_applicable_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                LifeCriticalTab.Locators.LIFE_STANDARDS_DEATH_NOT_APPLICABLE_RADIO_BUTTON)).is_selected()

    def get_cost_of_protection_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LifeCriticalTab.Locators.COST_OF_PROTECTION_YES_RADIO_BUTTON)).is_selected()

    def get_cost_of_protection_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LifeCriticalTab.Locators.COST_OF_PROTECTION_NO_RADIO_BUTTON)).is_selected()

    def get_impact_on_customer_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LifeCriticalTab.Locators.IMPACT_ON_CUSTOMER)).text

    def get_impact_on_dependants_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LifeCriticalTab.Locators.IMPACT_ON_DEPENDANTS)).text

    def get_address_this_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LifeCriticalTab.Locators.ADDRESS_THIS_TEXTFIELD)).text

    def get_reason_to_not_review_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LifeCriticalTab.Locators.REASON_TO_REVIEW)).text

    class Locators(object):
        MORTGAGE_AND_DEBT_CLEARED_YES_RADIO_BUTTON = (By.ID, "Yes_IsDebtCleared_IsDebtCleared_0")
        MORTGAGE_AND_DEBT_CLEARED_NO_RADIO_BUTTON = (By.ID, "No_IsDebtCleared_IsDebtCleared_0")
        MORTGAGE_AND_DEBT_CLEARED_NOT_APPLICABLE_RADIO_BUTTON = (By.ID, "NA_IsDebtCleared_IsDebtCleared_0")
        LIFE_STANDARDS_CRITICAL_ILLNESS_YES_RADIO_BUTTON = (By.ID, "Yes_IsCicMaintainable_IsCicMaintainable_0")
        LIFE_STANDARDS_CRITICAL_ILLNESS_NO_RADIO_BUTTON = (By.ID, "No_IsCicMaintainable_IsCicMaintainable_0")
        LIFE_STANDARDS_DEATH_YES_RADIO_BUTTON = (By.ID, "Yes_IsLifeMaintainable_IsLifeMaintainable_0")
        LIFE_STANDARDS_DEATH_NO_RADIO_BUTTON = (By.ID, "No_IsLifeMaintainable_IsLifeMaintainable_0")
        LIFE_STANDARDS_DEATH_NOT_APPLICABLE_RADIO_BUTTON = (By.ID, "NA_IsLifeMaintainable_IsLifeMaintainable_0")
        COST_OF_PROTECTION_YES_RADIO_BUTTON = (By.ID, "Yes_IsFixedProtectionPremium_IsFixedProtectionPremium_0")
        COST_OF_PROTECTION_NO_RADIO_BUTTON = (By.ID, "No_IsFixedProtectionPremium_IsFixedProtectionPremium_0")
        IMPACT_ON_CUSTOMER = (By.ID, "ImpactOnYou_ImpactOnYou_0")
        IMPACT_ON_DEPENDANTS = (By.ID, "ImpactOnDependants_ImpactOnDependants_0")
        ADDRESS_THIS_TEXTFIELD = (By.ID, "HowToAddress_HowToAddress_0")
        REASON_TO_REVIEW = (By.ID, "NotReviewingReason_NotReviewingReason_0")
