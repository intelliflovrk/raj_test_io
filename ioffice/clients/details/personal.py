from ioffice.clients.details.base import BaseDetailsPage
from selenium.webdriver.common.by import By


class ViewPersonalPage(BaseDetailsPage):

    def get_gender(self):
        return self.get_drop_down_selected_value(ViewPersonalPage.Locators.GENDER_FIELD)

    def get_firstname(self):
        return self.get_text(ViewPersonalPage.Locators.FIRST_NAME_FIELD)

    def get_lastname(self):
        return self.get_text(ViewPersonalPage.Locators.LAST_NAME_FIELD)

    def get_ni_number(self):
        return self.get_text(ViewPersonalPage.Locators.NI_NUMBER_TEXT)

    def fill_in_ni_number(self, ni_number_text):
        return self.fill_in_field(ViewPersonalPage.Locators.NI_NUMBER_FIELD, ni_number_text)

    def get_dob(self):
        return self.get_text(ViewPersonalPage.Locators.DOB_FIELD)

    def fill_in_tags(self, data):
        return self.clear_and_fill_in_field(self.Locators.TAGS_FIELD, data)

    def click_cross_on_tag(self):
        return self.click(self.Locators.CROSS_BUTTON)

    def click_edit_button(self):
        return self.click(self.Locators.EDIT_BUTTON)

    def click_save_button(self):
        return self.click(self.Locators.SAVE_BUTTON)

    class Locators(object):
        GENDER_FIELD = (By.CSS_SELECTOR, "#id_Gender")
        FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#id_FirstName_ro")
        LAST_NAME_FIELD = (By.CSS_SELECTOR, "#id_LastName_ro")
        NI_NUMBER_TEXT = (By.ID, "id_NINumber_ro")
        NI_NUMBER_FIELD = (By.ID, "id_NINumber")
        DOB_FIELD = (By.CSS_SELECTOR, "#id_DOB_ro")
        TAGS_FIELD = (By.CSS_SELECTOR, ".select2-search__field")
        EDIT_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_5_3_2_5")
        SAVE_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_5_3_2_4")
        CROSS_BUTTON = (By.CSS_SELECTOR, "[role='presentation']")
