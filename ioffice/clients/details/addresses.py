from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ioffice.clients.details.base import BaseDetailsPage
from selenium.webdriver.common.by import By


class Addresses(BaseDetailsPage):

    def get_address_line_1(self):
        return self.get_text(Addresses.Locators.BASIC_ADDRESS_LINE_1)

    def get_address_line_2(self):
        return self.get_text(Addresses.Locators.BASIC_ADDRESS_LINE_2)

    def get_address_line_3(self):
        return self.get_text(Addresses.Locators.BASIC_ADDRESS_LINE_3)

    def get_city_town(self):
        return self.get_text(Addresses.Locators.BASIC_CITY_TOWN)

    def get_postcode(self):
        return self.get_text(Addresses.Locators.BASIC_POST_CODE)

    def get_updated_address_line_1(self, address_id):
        return self.get_text((By.XPATH, Addresses.Locators.UPDATED_ADDRESS_LINE_1.format(address_id)))

    def get_updated_postcode(self, address_id):
        return self.get_text((By.XPATH, Addresses.Locators.UPDATED_POST_CODE.format(address_id)))

    def click_add_new(self):
        return self.click(Addresses.Locators.ADD_NEW_BUTTON)

    def click_delete_link(self, address_id):
        self.click((By.CSS_SELECTOR, Addresses.Locators.DELETE_LINK.format(address_id)))
        return self

    def click_edit_link(self, address_id):
        self.click((By.CSS_SELECTOR, Addresses.Locators.EDIT_LINK.format(address_id)))
        return self

    def clear_address_line_1(self):
        return self.clear(Addresses.Locators.ADDRESS_LINE_1_FIELD)

    def fill_in_address_line_1(self, data):
        return self.fill_in_field(Addresses.Locators.ADDRESS_LINE_1_FIELD, data)

    def clear_postcode(self):
        return self.clear(Addresses.Locators.POSTCODE_FIELD)

    def fill_in_postcode(self, data):
        return self.fill_in_field(Addresses.Locators.POSTCODE_FIELD, data)

    def click_save_button(self):
        return self.click(Addresses.Locators.SAVE_BUTTON)

    def select_result_per_page(self, data):
        self.select_by_visible_text(self.Locators.RESULT_PER_PAGE_SELECT_BOX, data)
        return self

    def is_address_id_present(self, address_id):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.invisibility_of_element_located((
            By.ID, self.Locators.ADDRESS_ID.format(address_id))))

    class Locators(object):
        BASIC_ADDRESS_LINE_1 = (By.XPATH, "//*[starts-with(@id, 'ClientDetailsAddressGrid')]/td[1]")
        BASIC_ADDRESS_LINE_2 = (By.XPATH, "//*[starts-with(@id, 'ClientDetailsAddressGrid')]/td[2]")
        BASIC_ADDRESS_LINE_3 = (By.XPATH, "//*[starts-with(@id, 'ClientDetailsAddressGrid')]/td[3]")
        BASIC_CITY_TOWN = (By.XPATH, "//*[starts-with(@id, 'ClientDetailsAddressGrid')]/td[5]")
        BASIC_POST_CODE = (By.XPATH, "//*[starts-with(@id, 'ClientDetailsAddressGrid')]/td[8]")
        ADD_NEW_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_5_7_3_3")
        DELETE_LINK = "a[href*='deleteaddress/{0}']"
        EDIT_LINK = "a[href*='EditAddress/{0}']"
        ADDRESS_ID = "ClientDetailsAddressGrid__{0}"
        RESULT_PER_PAGE_SELECT_BOX = (By.CSS_SELECTOR, "select[onchange*='ioUiGridNumResultsChange']")
        ADDRESS_LINE_1_FIELD = (By.ID, "id_AddressLine1")
        POSTCODE_FIELD = (By.ID, "AddressStorePostCode")
        SAVE_BUTTON = (By.ID, "ajaxMainAddressPanel_2_3")
        UPDATED_ADDRESS_LINE_1 = "//*[@id='ClientDetailsAddressGrid__{0}']/td[1]"
        UPDATED_POST_CODE = "//*[@id='ClientDetailsAddressGrid__{0}']/td[8]"
