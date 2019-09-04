from selenium.webdriver.common.by import By

from ioffice.base import IOBasePage
from ioffice.adviser_search_dialog import AdviserSearchDialog


class AddClientQuickPage(IOBasePage):

    def is_title_matches(self):
        return "Adviser Workplace | Clients | Quick Add Client | Intelligent Office" == self.driver.title

    def fill_in_firstlife_firstname_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.FIRST_LIFE_FIRSTNAME, data)

    def fill_in_firstlife_lastname_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.FIRST_LIFE_LASTNAME, data)

    def fill_in_firstlife_dateofbirth_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.FIRST_LIFE_DATE_OF_BIRTH, data)

    def select_firstlife_client_category(self, data):
        return self.select_by_visible_text(
            AddClientQuickPage.Locators.FIRST_LIFE_CLIENT_CATEGORY_SELECT_BOX, data)

    def select_gender(self, data):
        return self.select_by_visible_text(
            AddClientQuickPage.Locators.GENDER_SELECT_BOX, data)

    def fill_in_ni_number_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.NI_NUMBER, data)

    def fill_in_address_line_1_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.BASIC_ADDRESS_LINE_1, data)

    def fill_in_address_line_2_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.BASIC_ADDRESS_LINE_2, data)

    def fill_in_address_line_3_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.BASIC_ADDRESS_LINE_3, data)

    def fill_in_city_town_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.BASIC_CITY_TOWN, data)

    def fill_in_postcode_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.BASIC_POST_CODE, data)

    def fill_in_mobile_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.MOBILE_FIELD, data)

    def fill_in_notes_field(self, data):
        return self.fill_in_field(AddClientQuickPage.Locators.NOTES_FIELD, data)

    def open_adviser_dialog(self):
        self.click(AddClientQuickPage.Locators.SELECT_ADVISER_BUTTON)
        return AdviserSearchDialog(self, None, "id_ServicingAdviserPartyId")

    def click_save(self):
        return self.click(AddClientQuickPage.Locators.SAVE_BUTTON)

    class Locators:
        FIRST_LIFE_FIRSTNAME = (By.ID, "id_ClientOne_FirstName")
        FIRST_LIFE_LASTNAME = (By.ID, "id_ClientOne_LastName")
        FIRST_LIFE_DATE_OF_BIRTH = (By.ID, "id_ClientOne_DateOfBirth")
        FIRST_LIFE_CLIENT_CATEGORY_SELECT_BOX = (By.ID, "ClientOne.ClientCategoryId")
        GENDER_SELECT_BOX = (By.ID, "ClientOne.Gender")
        NI_NUMBER = (By.ID, "id_ClientOne_NINumber")
        BASIC_ADDRESS_LINE_1 = (By.ID, "ClientOneAddressLine1")
        BASIC_ADDRESS_LINE_2 = (By.ID, "ClientOneAddressLine2")
        BASIC_ADDRESS_LINE_3 = (By.ID, "ClientOneAddressLine3")
        BASIC_CITY_TOWN = (By.ID, "ClientOneCityTown")
        BASIC_POST_CODE = (By.ID, "ClientOnePostCode")
        MOBILE_FIELD = (By.ID, "id_ClientOne_Mobile")
        NOTES_FIELD = (By.CSS_SELECTOR, "#id_Notes")
        SELECT_ADVISER_BUTTON = (
            By.XPATH,
            "//*[@id='__display_id_ServicingAdviserPartyId']//following-sibling::*/a[@class='hpick']")
        SAVE_BUTTON = (By.ID, "quickAddClient_11")
