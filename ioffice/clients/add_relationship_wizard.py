from ioffice.wizard import *
from ioffice.adviser_search_dialog import *


class AddRelationshipWizard(BaseWizardPage):

    def __init__(self, config):
        super().__init__(config, "Add Relationship")
        self.frame_locator = AddRelationshipWizard.Locators.FRAME

    def select_type_stage(self):
        return AddRelationshipWizard.SelectTypeStage(self)

    def search_contact_stage(self):
        return AddRelationshipWizard.SearchContactStage(self)

    def select_contact_stage(self):
        return AddRelationshipWizard.SelectContactStage(self)

    def finish_stage(self):
        return AddRelationshipWizard.FinishStage(self)

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='AddRelationship']")

    class SelectTypeStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Select Type")

        def select_radio_button_person(self):
            self.page.click(self.Locators.PERSON_RADIO_BUTTON)
            return self

        class Locators(object):
            PERSON_RADIO_BUTTON = (By.ID, "id_step1ClientType_ClientType_3")

    class SearchContactStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Search Contact")

        def fill_in_firstname(self, data):
            self.page.clear_and_fill_in_field(self.Locators.FIRSTNAME_FIELD, data)
            return self

        def fill_in_lastname(self, data):
            self.page.clear_and_fill_in_field(self.Locators.LASTNAME_FIELD, data)
            return self

        class Locators(object):
            FIRSTNAME_FIELD = (By.ID, "id_step2SearchCustomer_FirstName")
            LASTNAME_FIELD = (By.ID, "id_step2SearchCustomer_LastName")

    class SelectContactStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Select Contact")

        def select_contact_radio_button(self):
            self.page.click(self.Locators.FIRST_CONTACT_RADIO_BUTTON)
            return self

        class Locators(object):
            FIRST_CONTACT_RADIO_BUTTON = (By.CSS_SELECTOR, "tbody > tr:nth-child(1) .rowselect.first [name='__s']")

    class FinishStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Finish")

        def select_relationship(self, data):
            self.page.select_by_visible_text(self.Locators.RELATIONSHIP_DROP_DOWN, data)
            return self

        def click_complete_button(self):
            self.page.click(self.Locators.COMPLETE_BUTTON)
            return self

        class Locators(object):
            COMPLETE_BUTTON = (By.XPATH, "//*[text()[contains(.,'Complete')]]")
            RELATIONSHIP_DROP_DOWN = (By.ID, "id_step4DefineRelationshipAndFinish_RelationshipTypeDTO")
