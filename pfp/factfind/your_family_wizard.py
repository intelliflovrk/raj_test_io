from pfp.wizard import BaseWizardPage, BaseWizardStage
from selenium.webdriver.common.by import By
from pageobjects import BasePageSection
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class YourFamilyWizard(BaseWizardPage):

    def your_family_member_stage(self):
        return self.YourFamilyMembersStage(self)

    def relationship_type_stage(self):
        return self.RelationshipTypeStage(self)

    def name_stage(self):
        return self.NameStage(self)

    def date_of_birth_stage(self):
        return self.DateOfBirthStage(self)

    def living_with_you_stage(self):
        return self.LivingWithYouStage(self)

    def review_stage(self):
        return self.ReviewStage(self)

    class YourFamilyMembersStage(BasePageSection):
        def __init__(self, parent_page):
            super().__init__(parent_page)

        def click_add_family_member(self):
            self.page.click(self.Locators.ADD_FAMILY_MEMBER_BUTTON)
            return self

        def click_yes_button(self):
            self.wait_until_load_spinner_disappears()
            self.page.click(self.Locators.YES_BUTTON)
            return self

        def click_no_button(self):
            self.page.click(self.Locators.NO_BUTTON)
            return self

        def click_save_and_close_button(self):
            self.page.click(self.Locators.SAVE_AND_CLOSE_BUTTON)
            return self

        def wait_until_load_spinner_disappears(self):
            WebDriverWait(self.driver, 10)\
                .until(EC.invisibility_of_element_located(self.Locators.LOAD_SPINNER))
            return self

        class Locators(object):
            ADD_FAMILY_MEMBER_BUTTON = (By.CSS_SELECTOR, "button[title='Add Family Member']")
            SAVE_AND_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[title='Save & Close']")
            YES_BUTTON = (By.CSS_SELECTOR, "label[for='yes']")
            NO_BUTTON = (By.CSS_SELECTOR, "label[for='no']")
            LOAD_SPINNER = (By.ID, "no-freeze-spinner")

    class RelationshipTypeStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Relationship type", parent_page)

        def click_relationship_type_option(self, data):
            self.page.click((By.CSS_SELECTOR, self.Locators.RELATIONSHIP_TYPE_LABEL.format(data)))
            return self

        class Locators(object):
            RELATIONSHIP_TYPE_LABEL = "label[for='{}']"

    class NameStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Name", parent_page)

        def fill_in_name_field(self, data):
            self.page.fill_in_field(self.Locators.NAME_FIELD, data)
            return self

        class Locators(object):
            NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='Name']")

    class DateOfBirthStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Date of birth", parent_page)

    class LivingWithYouStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Living with you", parent_page)

    class ReviewStage(BasePageSection):
        def __init__(self, parent_page):
            super().__init__(parent_page)

        def click_save_and_close_button(self):
            self.page.click(self.Locators.SAVE_AND_CLOSE_BUTTON)
            return self

        class Locators(object):
            SAVE_AND_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[title='Save & Close']")