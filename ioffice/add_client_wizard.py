from ioffice.wizard import *
from ioffice.adviser_search_dialog import *


class AddClientWizard(BaseWizardPage, IOBasePage):
    def __init__(self, config, title="Add Client"):
        super().__init__(config, title)
        self.frame_locator = AddClientWizard.Locators.FRAME

    def basic_details_stage(self):
        return AddClientWizard.BasicDetailsStage(self)

    def duplicate_clients_stage(self):
        return AddClientWizard.DuplicateClientsStage(self)

    def address_stage(self):
        return AddClientWizard.AddressStage(self)

    def contact_stage(self):
        return AddClientWizard.ContactStage(self)

    def opportunity_stage(self):
        return AddClientWizard.OpportunityStage(self)

    def dpa_stage(self):
        return AddClientWizard.DpaStage(self)

    def marketing_stage(self):
        return AddClientWizard.MarketingStage(self)

    def notes_stage(self):
        return AddClientWizard.NotesStage(self)

    class Locators(object):
        FRAME = (By.XPATH, "//iframe[@src='/nio/clientactions/addclient']")

    class BasicDetailsStage(BaseWizardStage, BasePage):

        def __init__(self, parent_page):
            super().__init__(parent_page, "Basic Details")

        def fill_in_firstname_field(self, data):
            return self.fill_in_field(AddClientWizard.BasicDetailsStage.Locators.FIRST_NAME, data)

        def fill_in_lastname_field(self, data):
            return self.fill_in_field(AddClientWizard.BasicDetailsStage.Locators.LAST_NAME, data)

        def fill_in_second_life_firstname(self, data):
            return self.fill_in_field(AddClientWizard.BasicDetailsStage.Locators.SECOND_LIFE_FIRSTNAME, data)

        def fill_in_second_life_lastname(self, data):
            return self.fill_in_field(AddClientWizard.BasicDetailsStage.Locators.SECOND_LIFE_LASTNAME, data)

        def open_adviser_dialog(self):
            self.page.click(AddClientWizard.BasicDetailsStage.Locators.SELECT_ADVISER_BUTTON)
            return AdviserSearchDialog(self.page, self.page.frame_locator, "id_BasicDetailsStep_AdviserPartyId")

        def select_joint_client_application(self):
            self.page.click(AddClientWizard.BasicDetailsStage.Locators.JOINT_CLIENT_APPLICATION)
            return self

        def select_client_type(self, data):
            self.select_by_visible_text(self.Locators.CLIENT_TYPE, data)
            return self

        def fill_in_corporate_name_field(self, data):
            self.fill_in_field(self.Locators.CORPORATE_NAME, data)
            return self

        class Locators(object):
            FIRST_LIFE_TITLE_SELECT_BOX = (By.ID, "Life1Title")
            FIRST_LIFE_GENDER_SELECT_BOX = (By.ID, "id_BasicDetailsStep_FirstLife_Gender")
            JOINT_CLIENT_APPLICATION = (By.ID, "ChkJointApplication")
            SECOND_LIFE_RELATIONSHIP = (By.ID, "Life2Relation")
            SECOND_LIFE_FIRSTNAME = (By.ID, "Life2FirstName")
            SECOND_LIFE_LASTNAME = (By.ID, "Life2LastName")
            SELECT_ADVISER_BUTTON = (By.XPATH,
                "//*[@id='__display_id_BasicDetailsStep_AdviserPartyId']//following-sibling::*/a[@class='hpick']")
            DATE_OF_BIRTH = (By.ID, "id_BasicDetailsStep_FirstLife_DateOfBirth")
            FIRST_NAME = (By.ID, "Life1FirstName")
            LAST_NAME = (By.ID, "Life1LastName")
            CLIENT_TYPE = (By.ID, "ClientType")
            CORPORATE_NAME = (By.ID, "CorporateName")

    class DuplicateClientsStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Duplicate Clients")

        class Locators(object):
            pass

    class AddressStage(BaseWizardStage):

        def __init__(self, parent_page):
            super().__init__(parent_page, "Address")

        def get_address_detail_same_for_joint_applicant_check_box_state(self):
            return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Locators.ADDRESS_DETAILS_FOR_JOINT_APPLICANT_CHECK_BOX)).is_selected()

        class Locators(object):
            BASIC_ADDRESS_LINE_1 = (By.ID, "FrstLifeLine1")
            BASIC_ADDRESS_LINE_2 = (By.ID, "FrstLifeLine2")
            BASIC_ADDRESS_LINE_3 = (By.ID, "FrstLifeLine3")
            BASIC_ADDRESS_LINE_4 = (By.ID, "FrstLifeLine4")
            BASIC_CITY_TOWN = (By.ID, "FrstLifeCityTwn")
            BASIC_POST_CODE = (By.ID, "FrstLifePCode")
            ADDRESS_DETAILS_FOR_JOINT_APPLICANT_CHECK_BOX = (By.ID, "ChkCopyAddressToJoint")

    class ContactStage(BaseWizardStage):

        def __init__(self, parent_page):
            super().__init__(parent_page, "Contact")

        def click_copy_contacts(self):
            self.page.click(AddClientWizard.ContactStage.Locators.COPY_CONTACT_DETAILS)
            return self

        def select_campaign_type_first_life(self, data):
            return self.page.select_by_visible_text(AddClientWizard.ContactStage.Locators.CAMPAIGN_TYPE_FIRST_LIFE, data)

        def select_campaign_type_second_life(self, data):
            return self.page.select_by_visible_text(AddClientWizard.ContactStage.Locators.CAMPAIGN_TYPE_SECOND_LIFE, data)

        class Locators(object):
            BASIC_MOBILE_NUMBER = (By.ID, "FrstLifeMob")
            BASIC_FAX_NUMBER = (By.ID, "FrstLifeFax")
            COPY_CONTACT_DETAILS = (By.ID, "btnCopyContactDetails")
            CAMPAIGN_TYPE_FIRST_LIFE = (By.ID, "id_ContactDetailsStep_CampaignType")
            CAMPAIGN_TYPE_SECOND_LIFE = (By.ID, "id_ContactDetailsStep_SecondCampaignType")

    class OpportunityStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Opportunity")

        def select(self, opportunity_type_text):
            return self.page.select_by_visible_text(
                AddClientWizard.OpportunityStage.Locators.OPPORTUNITY_TYPE_SELECT_BOX, opportunity_type_text)

        def select_by_visible_text_opportunity(self, data):
            return self.page.select_by_visible_text(AddClientWizard.OpportunityStage.Locators.OPPORTUNITY_TYPE_SELECT_BOX,
                                               data)

        def select_service_status_first_life(self, data):
            return self.page.select_by_visible_text(AddClientWizard.OpportunityStage.Locators.FIRST_LIFE_SERVICE_STATUS, data)

        def select_service_status_second_life(self, data):
            return self.page.select_by_visible_text(AddClientWizard.OpportunityStage.Locators.SECOND_LIFE_SERVICE_STATUS, data)

        def select_fee_model_first_life(self, data):
            return self.page.select_by_visible_text(AddClientWizard.OpportunityStage.Locators.FIRST_LIFE_FEE_MODEL, data)

        def select_fee_model_second_life(self, data):
            return self.page.select_by_visible_text(AddClientWizard.OpportunityStage.Locators.SECOND_LIFE_FEE_MODEL, data)

        def add_service_case_name(self, data):
            return self.page.clear_and_fill_in_field(self.Locators.SERVICE_CASE_NAME, data)

        def add_service_case_ref(self, data):
            return self.page.clear_and_fill_in_field(self.Locators.SERVICE_CASE_REF, data)

        class Locators(object):
            OPPORTUNITY_TYPE_SELECT_BOX = (By.ID, "id_OpportunityStep_OpportunityType")
            FIRST_LIFE_SERVICE_STATUS = (By.ID, "OpportunityStep.FirstServiceStatusId")
            SECOND_LIFE_SERVICE_STATUS = (By.ID, "OpportunityStep.SecondServiceStatusId")
            FIRST_LIFE_FEE_MODEL = (By.ID, "OpportunityStep.FirstLifeFeeModelId")
            SECOND_LIFE_FEE_MODEL = (By.ID, "OpportunityStep.SecondLifeFeeModelId")
            SERVICE_CASE_NAME = (By.ID, "id_AdviceCaseDetails_CaseName")
            SERVICE_CASE_REF = (By.ID, "id_AdviceCaseDetails_CaseReference")

    class DpaStage(BaseWizardStage):

        def __init__(self, parent_page):
            super().__init__(parent_page, "DPA")

        def fill_in_agreement_date_field(self, data):
            self.page.fill_in_field(AddClientWizard.DpaStage.Locators.FIRST_LIFE_DPA_AGREEMENT_DATE, data)
            return self

        def fill_in_agreement_date_field_second_life(self, data):
            self.page.fill_in_field(AddClientWizard.DpaStage.Locators.SECOND_LIFE_DPA_AGREEMENT_DATE, data)
            return self

        def tick_all_agreement_statements(self):
            dpa_statements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    AddClientWizard.DpaStage.Locators.FIRST_LIFE_DPA_AGREEMENT_STATEMENT))
            for i in range(1, len(dpa_statements) + 1):
                self.driver.find_element(
                    By.ID, AddClientWizard.DpaStage.Locators._FIRST_LIFE_DPA_AGREEMENT_STATEMENT_CHECKBOX.format(i)) \
                    .click()
            return self

        def tick_all_agreement_statements_second_life(self):
            dpa_statements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    AddClientWizard.DpaStage.Locators.SECOND_LIFE_DPA_AGREEMENT_STATEMENT))
            for i in range(1, len(dpa_statements) + 1):
                self.driver.find_element(
                    By.ID, AddClientWizard.DpaStage.Locators._SECOND_LIFE_DPA_AGREEMENT_STATEMENT_CHECKBOX.format(i)) \
                    .click()
            return self

        class Locators(object):
            FIRST_LIFE_DPA_AGREEMENT_STATEMENT = (By.XPATH, "//div[@id='dpa-form']//div[@class='ux-ctl-form-row row ']")
            _FIRST_LIFE_DPA_AGREEMENT_STATEMENT_CHECKBOX = "id_DataProtectionActStep_AgreementStatement{0}"
            FIRST_LIFE_DPA_AGREEMENT_DATE = (By.ID, "id_DataProtectionActStep_AgreementDate")
            SECOND_LIFE_DPA_AGREEMENT_STATEMENT = (
                By.XPATH, "//div[@id='dpa-form2']//div[@class='ux-ctl-form-row row ']")
            _SECOND_LIFE_DPA_AGREEMENT_STATEMENT_CHECKBOX = "id_SecondLifeDataProtectionActStep_AgreementStatement{0}"
            SECOND_LIFE_DPA_AGREEMENT_DATE = (By.ID, "id_SecondLifeDataProtectionActStep_AgreementDate")

    class MarketingStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Marketing")

        def fill_in_consent_date_field(self, data):
            return self.page.fill_in_field(AddClientWizard.MarketingStage.Locators.CONSENT_DATE, data)

        class Locators(object):
            CONSENT_DATE = (By.ID, "id_MarketingStep_ConsentDate")

    class NotesStage(BaseWizardStage):

        def __init__(self, parent_page):
            super().__init__(parent_page, "Notes")

        def fill_in_notes(self, data):
            return self.page.fill_in_field(AddClientWizard.NotesStage.Locators.NOTES, data)

        class Locators(object):
            NOTES = (By.ID, "id_NotesStep_Notes")
