from ioffice.wizard import *
from ioffice.adviser_search_dialog import *


class AddLeadWizard(BaseWizardPage):

    def __init__(self, config, title="Add Lead"):
        super().__init__(config, title)
        self.frame_locator = AddLeadWizard.Locators.FRAME

    def basic_details_stage(self):
        return AddLeadWizard.BasicDetailsStage(self)

    def address_stage(self):
        return AddLeadWizard.AddressStage(self)

    def contact_stage(self):
        return AddLeadWizard.ContactStage(self)

    class Locators(object):
        FRAME = (By.XPATH, "//iframe[@src='/nio/leads/AddLead']")

    class BasicDetailsStage(BaseWizardStage):

        def __init__(self, parent_page):
            super().__init__(parent_page, "Basic Details")

        def fill_in_first_name_field(self, data):
            return self.page.fill_in_field(AddLeadWizard.BasicDetailsStage.Locators.FIRST_NAME, data)

        def fill_in_last_name_field(self, data):
            return self.page.fill_in_field(AddLeadWizard.BasicDetailsStage.Locators.LAST_NAME, data)

        class Locators(object):
            FIRST_LIFE_TITLE_SELECT_BOX = (By.ID, "Life1Title")
            FIRST_LIFE_GENDER_SELECT_BOX = (By.ID, "id_BasicDetailsStep_FirstLife_Gender")
            FIRST_NAME = (By.ID, "Life1FirstName")
            LAST_NAME = (By.ID, "Life1LastName")
            DATE_OF_BIRTH = (By.ID, "id_BasicDetailsStep_FirstLife_DateOfBirth")
            EXTERNAL_REF = (By.ID, "id_BasicDetailsStep_FirstLife_PersonExternalReference")

    class AddressStage(BaseWizardStage):

        def __init__(self, parent_page):
            super().__init__(parent_page, "Address")

        class Locators(object):
            BASIC_ADDRESS_LINE_1 = (By.ID, "FrstLifeLine1")
            BASIC_ADDRESS_LINE_2 = (By.ID, "FrstLifeLine2")
            BASIC_ADDRESS_LINE_3 = (By.ID, "FrstLifeLine3")
            BASIC_ADDRESS_LINE_4 = (By.ID, "FrstLifeLine4")
            BASIC_CITY_TOWN = (By.ID, "FrstLifeCityTwn")
            BASIC_POST_CODE = (By.ID, "FrstLifePCode")

    class ContactStage(BaseWizardStage):

        def __init__(self, parent_page):
            super().__init__(parent_page, "Contact")

        def fill_in_phone_number_field(self, data):
            return self.page.fill_in_field(AddLeadWizard.ContactStage.Locators.BASIC_PHONE_NUMBER, data)

        class Locators(object):
            BASIC_PHONE_NUMBER = (By.ID, "FrstLifePhone")

