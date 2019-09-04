from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ioffice.clients.factfind.protection_tab import ProtectionTab
from pageobjects import EC


class BuildingsContentsTab(ProtectionTab):

    def click_existing_building_yes_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.EXISTING_BUILDING_INSURANCE_YES_RADIO_BUTTON)

    def click_existing_building_no_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.EXISTING_BUILDING_INSURANCE_NO_RADIO_BUTTON)

    def click_existing_content_insurance_yes_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.EXISTING_CONTENT_INSURANCE_YES_RADIO_BUTTON)

    def click_existing_content_insurance_no_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.EXISTING_CONTENT_INSURANCE_NO_RADIO_BUTTON)

    def click_buy_to_let_yes_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.BUY_TO_LET_YES_RADIO_BUTTON)

    def click_buy_to_let_no_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.BUY_TO_LET_NO_RADIO_BUTTON)

    def click_sufficient_insurance_yes_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.SUFFICIENT_INSURANCE_YES_RADIO_BUTTON)

    def click_sufficient_insurance_no_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.SUFFICIENT_INSURANCE_NO_RADIO_BUTTON)

    def click_sufficient_protection_yes_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.SUFFICIENT_PROTECTION_YES_RADIO_BUTTON)

    def click_sufficient_protection_no_radio_button(self):
        return self.click(BuildingsContentsTab.Locators.SUFFICIENT_PROTECTION_NO_RADIO_BUTTON)

    def get_existing_building_insurance_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                BuildingsContentsTab.Locators.SUFFICIENT_INSURANCE_YES_RADIO_BUTTON)).is_selected()

    def get_existing_building_insurance_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                BuildingsContentsTab.Locators.SUFFICIENT_INSURANCE_NO_RADIO_BUTTON)).is_selected()

    def get_existing_contents_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                BuildingsContentsTab.Locators.EXISTING_CONTENT_INSURANCE_YES_RADIO_BUTTON)).is_selected()

    def get_existing_contents_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                BuildingsContentsTab.Locators.EXISTING_CONTENT_INSURANCE_YES_RADIO_BUTTON)).is_selected()

    def get_buy_to_let_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BuildingsContentsTab.Locators.BUY_TO_LET_YES_RADIO_BUTTON)).is_selected()

    def get_buy_to_let_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BuildingsContentsTab.Locators.BUY_TO_LET_NO_RADIO_BUTTON)).is_selected()

    def get_sufficient_building_insurance_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                BuildingsContentsTab.Locators.SUFFICIENT_INSURANCE_YES_RADIO_BUTTON)).is_selected()

    def get_sufficient_building_insurance_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                BuildingsContentsTab.Locators.SUFFICIENT_INSURANCE_NO_RADIO_BUTTON)).is_selected()

    def get_sufficient_protection_yes_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                BuildingsContentsTab.Locators.SUFFICIENT_PROTECTION_YES_RADIO_BUTTON)).is_selected()

    def get_sufficient_protection_no_radio_button_state(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                BuildingsContentsTab.Locators.SUFFICIENT_PROTECTION_NO_RADIO_BUTTON)).is_selected()

    def get_how_to_address_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BuildingsContentsTab.Locators.ADDRESS_THIS_TEXTFIELD)).text

    def get_when_do_you_want_to_review_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BuildingsContentsTab.Locators.WHEN_DO_YOU_WANT_TO_REVIEW)).text

    def get_reason_if_no_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(BuildingsContentsTab.Locators.REASON_FOR_REVIEW)).text

    class Locators(object):
        EXISTING_BUILDING_INSURANCE_YES_RADIO_BUTTON = (
            By.ID, "Yes_AnyExistingBuildingProvision_AnyExistingBuildingProvision_0")
        EXISTING_BUILDING_INSURANCE_NO_RADIO_BUTTON = (
            By.ID, "No_AnyExistingBuildingProvision_AnyExistingBuildingProvision_0")
        EXISTING_CONTENT_INSURANCE_YES_RADIO_BUTTON = (
            By.ID, "Yes_AnyExistingContentsProvision_AnyExistingContentsProvision_0")
        EXISTING_CONTENT_INSURANCE_NO_RADIO_BUTTON = (
            By.ID, "No_AnyExistingContentsProvision_AnyExistingContentsProvision_0")
        BUY_TO_LET_YES_RADIO_BUTTON = (By.ID, "Yes_AnyBuyToLet_AnyBuyToLet_0")
        BUY_TO_LET_NO_RADIO_BUTTON = (By.ID, "No_AnyBuyToLet_AnyBuyToLet_0")
        SUFFICIENT_PROTECTION_YES_RADIO_BUTTON = (By.ID, "Yes_IsCoverSufficient_IsCoverSufficient_0")
        SUFFICIENT_PROTECTION_NO_RADIO_BUTTON = (By.ID, "No_IsCoverSufficient_IsCoverSufficient_0")
        SUFFICIENT_INSURANCE_YES_RADIO_BUTTON = (By.ID, "Yes_IsBtlCoverSufficient_IsBtlCoverSufficient_0")
        SUFFICIENT_INSURANCE_NO_RADIO_BUTTON = (By.ID, "No_IsBtlCoverSufficient_IsBtlCoverSufficient_0")
        ADDRESS_THIS_TEXTFIELD = (By.ID, "BCHowToAddress_HowToAddress_0")
        WHEN_DO_YOU_WANT_TO_REVIEW = (By.ID, "BCWhenToReview_WhenToReview_0")
        REASON_FOR_REVIEW = (By.ID, "BCNotReviewingReason_NotReviewingReason_0")
