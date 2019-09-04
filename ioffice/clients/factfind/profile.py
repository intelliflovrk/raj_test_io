from selenium.webdriver.common.by import By
from ioffice.clients.factfind.base import BaseFactFindPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects import EC
from fakedata import *


class ProfileStage(BaseFactFindPage):

    def click_advice_areas_subtab(self):
        return self.click(ProfileStage.Locators.ADVICE_AREAS_SUBTAB)

    def click_data_protection_subtab(self):
        return self.click(ProfileStage.Locators.DATA_PROTECTION_SUBTAB)

    def click_personal_subtab(self):
        return self.click(ProfileStage.Locators.PERSONAL_SUBTAB)

    def click_risk_subtab(self):
        return self.click(ProfileStage.Locators.RISK_SUBTAB)

    def click_risk_replay_subtab(self):
        return self.click(ProfileStage.Locators.RISK_REPAY_SUBTAB)

    def click_contact_details_subtab(self):
        return self.click(ProfileStage.Locators.CONTACT_DETAILS_SUBTAB)

    def click_dependants_subtab(self):
        return self.click(ProfileStage.Locators.DEPENDANTS_SUBTAB)

    def click_needs_and_priorities_subtab(self):
        return self.click(ProfileStage.Locators.NEEDS_AND_PRIORITIES_SUBTAB)

    def click_select_protection(self):
        return self.click(ProfileStage.Locators.PROTECTION_YES_RADIO_BUTTON)

    def click_select_retirement(self):
        return self.click(ProfileStage.Locators.RETIREMENT_RADIO_BUTTON_YES)

    def click_select_estate_planning(self):
        return self.click(ProfileStage.Locators.ESTATE_PLANNING_YES_RADIO_BUTTON)

    def click_select_mortgage(self):
        return self.click(ProfileStage.Locators.MORTGAGE_YES_RADIO_BUTTON)

    class Locators(object):
        PROTECTION_YES_RADIO_BUTTON = (By.ID, "Yes_ProtectionAdvice_ProtectionAdvice_0")
        PROTECTION_NO_RADIO_BUTTON = (By.ID, "No_ProtectionAdvice_ProtectionAdvice_0")
        ADVICE_AREAS_SUBTAB = (By.LINK_TEXT, "Advice Areas")
        DATA_PROTECTION_SUBTAB = (By.LINK_TEXT, "Data Protection")
        PERSONAL_SUBTAB = (By.ID, "personaldetails")
        CONTACT_DETAILS_SUBTAB = (By.LINK_TEXT, "Contact Details")
        DEPENDANTS_SUBTAB = (By.LINK_TEXT, "Dependants")
        NEEDS_AND_PRIORITIES_SUBTAB = (By.ID, "needsandprioritiesprofile")
        RETIREMENT_RADIO_BUTTON_YES = (By.ID, "Yes_RetirementAdvice_RetirementAdvice_0")
        ESTATE_PLANNING_YES_RADIO_BUTTON = (By.ID, "Yes_EstateAdvice_EstateAdvice_0")
        MORTGAGE_YES_RADIO_BUTTON = (By.ID, "Yes_MortgageAdvice_MortgageAdvice_0")
        RISK_SUBTAB = (By.ID, "profilerisk")
        RISK_REPAY_SUBTAB = (By.ID, "profileriskreplay")

    class AdviceAreas(BaseFactFindPage):

        def fill_in_date_issued(self, data):
            return self.clear_and_fill_in_field(self.Locators.DATE_ISSUED, data)

        def click_add_button(self):
            return self.click(ProfileStage.AdviceAreas.Locators.ADD_BUTTON)

        def click_save_button(self):
            return self.click(ProfileStage.AdviceAreas.Locators.SAVE_BUTTON)

        def select_document_type(self, data):
            return self.select_by_visible_text(ProfileStage.AdviceAreas.Locators.DOCUMENT_TYPE, data)

        class Locators(object):
            DATE_ISSUED = (By.ID, "DiscDocDate_IssueDate_0")
            ADD_BUTTON = (By.XPATH, "//*[@id='disclosure_grid_0']/a")
            SAVE_BUTTON = (By.ID, "ff-form-save")
            DOCUMENT_TYPE = (By.XPATH, "//*[@id='DocumentDisclosureTypeId_DocumentDisclosureTypeId_0']")

    class DataProtection(BaseFactFindPage):

        def click_add_button(self):
            return self.click(ProfileStage.DataProtection.Locators.ADD_BUTTON)

        def click_save_button(self):
            return self.click(ProfileStage.DataProtection.Locators.SAVE_BUTTON)

        def tick_all_agreement_statements(self):
            dpa_statements = WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.presence_of_all_elements_located(
                    ProfileStage.DataProtection.Locators.DPA_ALL_CHECKBOXES))
            for i in range(1, len(dpa_statements) + 1):
                self.driver.find_element(
                    By.ID, ProfileStage.DataProtection.Locators.FIRST_DPA_CHECKBOX.format(i)) \
                    .click()
            return self

        def fill_in_agreement_date(self, data):
            self.clear_and_fill_in_field(self.Locators.AGREEMENT_DATE_FIELD, data)
            return self

        class Locators(object):
            ADD_BUTTON = (By.XPATH, "//*[@id='policyagreement_grid_0']/div[2]/a")
            SAVE_BUTTON = (By.XPATH, "//*[@id='btnSave']")
            DPA_ALL_CHECKBOXES = (By.XPATH, "//*[@type='checkbox']")
            FIRST_DPA_CHECKBOX = "PolicyAgreementItems_Statement{0}AnswerValue"
            AGREEMENT_DATE_FIELD = (By.ID, "PolicyAgreementItems_AgreementDate")

    class Personal(BaseFactFindPage):

        def fill_in_national_insurance_number(self, data):
            return self.clear_and_fill_in_field(self.Locators.NI_NUMBER_FIELD, data)

        def select_uk_residency_checkbox(self):
            return self.click(ProfileStage.Personal.Locators.UK_RESIDENCY_RADIO_BUTTON)

        def select_marital_status(self, data):
            return self.select_by_visible_text(ProfileStage.Personal.Locators.MARITAL_STATUS, data)

        def get_first_life_full_name(self):
            return WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(ProfileStage.Personal.Locators.FIRST_LIFE_FULL_NAME)).text

        def get_second_life_full_name(self):
            return WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(ProfileStage.Personal.Locators.SECOND_LIFE_FULL_NAME)).text

        def get_title_value(self):
            return self.get_text(self.Locators.TITLE_SELECT_BOX)

        def get_gender_value(self):
            return self.get_text(self.Locators.GENDER_SELECT_BOX)

        def get_date_of_birth_value(self):
            return self.get_attribute(self.Locators.DATE_OF_BIRTH_DATE_PICKER, "value")

        def get_other_place_of_birth_value(self):
            return self.get_attribute(self.Locators.OTHER_PLACE_OF_BIRTH_FIELD, "value")

        def get_nationality_value(self):
            return self.get_text(self.Locators.NATIONALITY_SELECT_BOX)

        def is_uk_resident(self):
            return self.is_radio_button_selected(self.Locators.UK_RESIDENCY_RADIO_BUTTON)

        def are_you_in_good_health(self):
            return self.is_radio_button_selected(self.Locators.ARE_YOU_IN_GOOD_HEALTH_RADIO_BUTTON)

        def are_you_a_smoker(self):
            return self.is_radio_button_selected(self.Locators.ARE_YOU_A_SMOKER_RADIO_BUTTON)

        def do_you_have_a_valid_will(self):
            return self.is_radio_button_selected(self.Locators.DO_YOU_HAVE_A_VALID_WILL_RADIO_BUTTON)

        def fill_in_date_of_birth(self, data):
            self.clear_and_fill_in_field(self.Locators.DATE_OF_BIRTH_DATE_PICKER, data)
            return self

        def fill_in_middle_name(self, data):
            self.clear_and_fill_in_field(self.Locators.MIDDLE_NAME_FIELD, data)
            return self

        class Locators(object):
            MARITAL_STATUS = (By.ID, "MaritalStatus_MaritalStatus_0")
            UK_RESIDENCY_RADIO_BUTTON = (By.ID, "Yes_18_UKResident_0")
            FIRST_LIFE_FULL_NAME = (By.ID, "FullName_FullName_0")
            SECOND_LIFE_FULL_NAME = (By.ID, "FullName_FullName_1")
            NI_NUMBER_FIELD = (By.ID, "NINumber_NINumber_0")
            TITLE_SELECT_BOX = (By.CSS_SELECTOR, "#Title_Title_0 > option[selected='selected']")
            GENDER_SELECT_BOX = (By.CSS_SELECTOR, "#GenderType_GenderType_0 > option[selected='selected']")
            DATE_OF_BIRTH_DATE_PICKER = (By.CSS_SELECTOR, "input[class*='dob picker-single'][id='6_DOB_0']")
            OTHER_PLACE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, "#PlaceOfBirthOther_0 > #PlaceOfBirthOther_PlaceOfBirthOther_0")
            NATIONALITY_SELECT_BOX = (By.CSS_SELECTOR, "#Nationality_RefNationalityId_0 > option[selected='selected']")
            ARE_YOU_IN_GOOD_HEALTH_RADIO_BUTTON = (By.ID, "Yes_IsInGoodHealth_IsInGoodHealth_0")
            ARE_YOU_A_SMOKER_RADIO_BUTTON = (By.ID, "Yes_IsSmoker_IsSmoker_0")
            DO_YOU_HAVE_A_VALID_WILL_RADIO_BUTTON = (By.ID, "Yes_HasValidWill_HasValidWill_0")
            MIDDLE_NAME_FIELD = (By.ID, "MiddleName_MiddleName_0")

    class ContactDetails(BaseFactFindPage):

        def fill_in_contact_value_field(self, data):
            return self.fill_in_field(ProfileStage.ContactDetails.Locators.CONTACT_VALUE, data)

        def click_add_contact_button(self):
            return self.click(ProfileStage.ContactDetails.Locators.ADD_CONTACT_BUTTON)

        def click_add_professional_contact_button(self):
            return self.click(ProfileStage.ContactDetails.Locators.ADD_PROFESSIONAL_CONTACT_BUTTON)

        def click_save_button(self):
            return self.click(ProfileStage.ContactDetails.Locators.SAVE_BUTTON)

        class Locators(object):
            ADD_CONTACT_BUTTON = (By.XPATH, "//*[@id='18010_grid_0']/a")
            ADD_PROFESSIONAL_CONTACT_BUTTON = (By.XPATH, "//*[@id='_grid_0']/a")
            SAVE_BUTTON = (By.XPATH, "//*[@id='ff-form-save']")
            CONTACT_TYPE = (By.XPATH, "//*[@id='775_ContactType_0']")
            CONTACT_VALUE = (By.ID, "ContactValue_Value_0")
            CONTACT_NAME = (By.ID, "776_ContactName_0")
            ADDRESS_LINE1 = (By.ID, "PCLine1_AddressLine1_0")
            ADDRESS_LINE2 = (By.ID, "PCLine2_AddressLine2_0")
            ADDRESS_LINE3 = (By.ID, "PCLine3_AddressLine3_0")
            ADDRESS_LINE4 = (By.ID, "PCLine4_AddressLine4_0")

    class Dependants(BaseFactFindPage):

        def fill_in_full_name(self, data):
            return self.clear_and_fill_in_field(self.Locators.FULL_NAME_FIELD, data)

        def fill_in_date_of_birth(self, data):
            return self.clear_and_fill_in_field(self.Locators.DATE_OF_BIRTH_FIELD, data)

        def click_add_button(self):
            return self.click(ProfileStage.Dependants.Locators.ADD_BUTTON)

        def click_save_button(self):
            return self.click(ProfileStage.ContactDetails.Locators.SAVE_BUTTON)

        def get_full_name_value(self):
            fullname = self.get_text(self.Locators.FIRST_ROW_FULL_NAME_TEXT)
            return self.get_text(self.Locators.FIRST_ROW_FULL_NAME_TEXT)

        def get_relationship_value(self):
            return self.get_text(self.Locators.FIRST_ROW_RELATIONSHIP_TEXT)

        class Locators(object):
            ADD_BUTTON = (By.XPATH, "//*[@id='dependantdetails_grid_0']/a")
            SAVE_BUTTON = (By.XPATH, "//*[@id='ff-form-save']")
            FULL_NAME_FIELD = (By.ID, "53_Name_0")
            DATE_OF_BIRTH_FIELD = (By.ID, "54_DOB_0")
            FIRST_ROW_FULL_NAME_TEXT = (By.XPATH, "//*[@role='row']/td[1]")
            FIRST_ROW_RELATIONSHIP_TEXT = (By.XPATH, "//*[@role='row']/td[4]")

    class NeedsAndPriorities(BaseFactFindPage):

        def get_needs_and_priorities_question(self):
            return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable
                (ProfileStage.NeedsAndPriorities.Locators.FIRST_QUESTION)).text

        def clear_needs_and_priorities_answer(self):
            self.clear(ProfileStage.NeedsAndPriorities.Locators.FIRST_QUESTION_TEXT_BOX)
            return self

        def press_backspace_on_field(self):
            self.fill_in_field(ProfileStage.NeedsAndPriorities.Locators.FIRST_QUESTION_TEXT_BOX,
                               Keys.BACKSPACE)
            return self

        def complete_needs_and_priorities_answer(self):
            self.fill_in_field(ProfileStage.NeedsAndPriorities.Locators.FIRST_QUESTION_TEXT_BOX, utils.get_common_data(
                self.config)["basic_data"]["basic_text"]["BASIC_TEXT"])
            return self

        class Locators(object):
            FIRST_QUESTION = (By.CSS_SELECTOR, "div.ff-label > label")
            FIRST_QUESTION_TEXT_BOX = (By.XPATH, "//*[starts-with(@id, 'QAnswers')]")

    class Risk(BaseFactFindPage):

        def get_warning_message(self):
            return WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(self.Locators.WARNING_MESSAGE)).text

        def get_generated_risk_profile(self):
            return WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(self.Locators.GENERATED_RISK_PROFILE)).text

        def get_save_button_attribute(self):
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                ProfileStage.Risk.Locators.SAVE_BUTTON)).get_attribute("class")

        def fill_in_risk_notes_field(self):
            self.fill_in_field(self.Locators.NOTES, utils.get_common_data(self.config)["basic_data"]["basic_text"]["BASIC_TEXT"])
            return self

        def get_risk_notes_value(self):
            return self.get_text(ProfileStage.Risk.Locators.NOTES)

        class Locators(object):
            QUESTION_ONE = (
                By.XPATH, "//select[@name= 'ProfileRiskProfileItems.RiskRetirmentDtos[0].AtrDtos[0].AtrAnswerGuid']")
            QUESTION_TWO = (
                By.XPATH, "//select[@name= 'ProfileRiskProfileItems.RiskRetirmentDtos[0].AtrDtos[1].AtrAnswerGuid']")
            QUESTION_THREE = (
                By.XPATH, "//select[@name= 'ProfileRiskProfileItems.RiskRetirmentDtos[0].AtrDtos[2].AtrAnswerGuid']")
            QUESTION_FOUR = (
                By.XPATH, "//select[@name= 'ProfileRiskProfileItems.RiskRetirmentDtos[0].AtrDtos[3].AtrAnswerGuid']")
            QUESTION_FIVE = (
                By.XPATH, "//select[@name= 'ProfileRiskProfileItems.RiskRetirmentDtos[0].AtrDtos[4].AtrAnswerGuid']")
            WARNING_MESSAGE = (By.ID, "inconsistentMessage")
            SAVE_BUTTON = (By.ID, "ff-form-savebar")
            NOTES = (By.ID, "InconsistencyNotes_0")
            GENERATED_RISK_PROFILE = (By.CSS_SELECTOR, ".ff-value span")

    class RiskReplay(BaseFactFindPage):

        def get_chosen_risk_profile(self):
            return WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(self.Locators.CHOOSEN_RISK_PROFILE)).text

        def get_generated_risk_profile(self):
            return WebDriverWait(self.driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(self.Locators.GENERATED_RISK_PROFILE)).text

        def click_risk_profile_radio_button_no(self):
            return self.click(self.Locators.RISK_PROFILE_RADIO_BUTTON_NO)

        def click_risk_profile_radio_button_yes(self):
            return self.click(self.Locators.RISK_PROFILE_RADIO_BUTTON_YES)

        def fill_in_risk_replay_notes(self):
            self.fill_in_field(self.Locators.NOTES, utils.get_common_data(self.config)["basic_data"]["basic_text"]["BASIC_TEXT"])
            return self

        def get_risk_replay_notes_value(self):
            return self.get_text(ProfileStage.RiskReplay.Locators.NOTES)

        def clear_in_risk_replay_notes(self):
            self.clear(self.Locators.NOTES)
            return self

        class Locators(object):
            RISK_PROFILE_RADIO_BUTTON_NO = (By.XPATH, "//div[@class='ff-value']/input[2]")
            RISK_PROFILE_RADIO_BUTTON_YES = (By.XPATH, "//div[@class='ff-value']/input[1]")
            NOTES = (By.ID, "ClientNotesPrimary")
            GENERATED_RISK_PROFILE = (By.CSS_SELECTOR, ".ff-profile b")
            CHOOSEN_RISK_PROFILE = (By.CSS_SELECTOR, ".ff-label span")
