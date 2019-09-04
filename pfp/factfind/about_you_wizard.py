from pfp.wizard import BaseWizardPage, BaseWizardStage
from selenium.webdriver.common.by import By
from pageobjects import BasePageSection
import utils
import time


class AboutYouWizard(BaseWizardPage):

    def title_and_gender_stage(self):
        return AboutYouWizard.TitleAndGenderStage(self)

    def date_of_birth_stage(self):
        return AboutYouWizard.DateOfBirthStage(self)

    def place_of_birth_stage(self):
        return AboutYouWizard.PlaceOfBirthStage(self)

    def nationality_stage(self):
        return AboutYouWizard.NationalityStage(self)

    def residence_stage(self):
        return AboutYouWizard.ResidenceStage(self)

    def health_stage(self):
        return AboutYouWizard.HealthStage(self)

    def will_stage(self):
        return AboutYouWizard.WillStage(self)

    def photo_stage(self):
        return AboutYouWizard.PhotoStage(self)

    def review_stage(self):
        return AboutYouWizard.ReviewStage(self)

    def click_review_button(self):
        self.click(self.Locators.REVIEW_BUTTON)
        return AboutYouWizard.ReviewStage(self)

    class Locators(object):
        REVIEW_BUTTON = (By.XPATH, "//div[normalize-space(text())= 'Review']//ancestor::button[@class='nav-link']")

    class TitleAndGenderStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Title & gender", parent_page)

        def click_title_option(self, data):
            self.page.click((By.CSS_SELECTOR, self.Locators.TITLE_LABEL.format(data)))
            return self

        def click_gender_option(self, data):
            self.page.click((By.CSS_SELECTOR, self.Locators.GENDER_LABEL.format(data)))
            return self

        class Locators(object):
            TITLE_LABEL = "label[for='{}']"
            GENDER_LABEL = "label[for='{}']"

    class DateOfBirthStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Date of birth", parent_page)

        def fill_in_date_of_birth_fields(self):
            data = utils.get_common_data(self.config)["test_data"]["gff_client_data"]
            self.page.clear_and_fill_in_field(self.Locators.DATE_FIELD, data["DOB_DATE"])
            self.page.clear_and_fill_in_field(self.Locators.MONTH_FIELD, data["DOB_MONTH"])
            self.page.clear_and_fill_in_field(self.Locators.YEAR_FIELD, data["DOB_YEAR"])
            return self

        class Locators(object):
            DATE_FIELD = (By.CSS_SELECTOR, "input[placeholder='DD']")
            MONTH_FIELD = (By.CSS_SELECTOR, "input[placeholder='Month']")
            YEAR_FIELD = (By.CSS_SELECTOR, "input[placeholder='YYYY']")

    class PlaceOfBirthStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Place of birth", parent_page)

        def fill_in_place_of_birth(self, data):
            self.page.clear_and_fill_in_field(self.Locators.PLACE_OF_BIRTH_FIELD, data)
            return self

        class Locators(object):
            PLACE_OF_BIRTH_FIELD = (By.CSS_SELECTOR, "input[placeholder='Place of birth']")

    class NationalityStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Nationality", parent_page)

        def delete_nationality(self):
            self.page.select_text_and_delete(self.Locators.NATIONALITY_FIELD)
            return self

        def fill_in_nationality_field(self, data):
            self.page.fill_in_field(self.Locators.NATIONALITY_FIELD, data)
            self.page.click(self.Locators.DROPDOWN_VALUE_ENGLISH)
            time.sleep(1)
            return self

        class Locators(object):
            NATIONALITY_FIELD = (By.XPATH, "//div[contains(@class, 'dropdown mb-15')]//input")
            DROPDOWN_VALUE_ENGLISH =\
                (By.XPATH, "//div[contains(@class, 'dropdown mb-15')]//span[normalize-space(text())= 'English']")

    class ResidenceStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Residence", parent_page)

        def click_residence_option(self, data):
            self.page.click((By.CSS_SELECTOR, self.Locators. RESIDENCE_BUTTON.format(data)))
            return self

        class Locators(object):
            RESIDENCE_BUTTON = "input[name='choice__80'] + label[for='{}']"

    class HealthStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Health", parent_page)

        def click_are_in_good_health_option(self, data):
            self.page.click((By.CSS_SELECTOR, self.Locators.HEALTH_STATUS_BUTTON.format(data)))
            return self

        def click_have_you_smoked_option(self, data):
            self.page.click((By.CSS_SELECTOR, self.Locators.ATTITUDE_TO_SMOKING_BUTTON.format(data)))
            return self

        class Locators(object):
            HEALTH_STATUS_BUTTON = "input[name='choice__100'] + label[for='{}']"
            ATTITUDE_TO_SMOKING_BUTTON = "input[name='choice__103'] + label[for='{}']"

    class WillStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Will", parent_page)

        def click_will_status_option(self, data):
            self.page.click((By.CSS_SELECTOR, self.Locators.WILL_STATUS_BUTTON.format(data)))
            return self

        class Locators(object):
            WILL_STATUS_BUTTON = "input[name='choice__108'] + label[for='{}']"

    class PhotoStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__("Photo", parent_page)

    class ReviewStage(BasePageSection):
        def __init__(self, parent_page):
            super().__init__(parent_page)

        def click_save_and_close_button(self):
            self.page.click(self.Locators.SAVE_AND_CLOSE_BUTTON)
            return self

        def get_middle_name_value(self):
            return self.page.get_attribute(self.Locators.MIDDLE_NAME_FIELD, 'value')

        def get_marital_status_value(self):
            return self.page.get_attribute(self.Locators.MARITAL_STATUS_FIELD, 'value')

        class Locators(object):
            SAVE_AND_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[title='Save & Close']")
            MIDDLE_NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='Middle name']")
            MARITAL_STATUS_FIELD =\
                (By.XPATH, "//label[normalize-space(text())= 'Marital status']/following-sibling::*//input")
