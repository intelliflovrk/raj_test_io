from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class ClientAddressDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def fill_in_address_line_1_field(self, address):
        self.page.fill_in_field(self.Locators.BASIC_ADDRESS_LINE_1, address)
        return self

    def fill_in_address_line_2_field(self, address):
        self.page.fill_in_field(self.Locators.BASIC_ADDRESS_LINE_2, address)
        return self

    def fill_in_address_line_3_field(self, address):
        self.page.fill_in_field(self.Locators.BASIC_ADDRESS_LINE_3, address)
        return self

    def fill_in_address_line_4_field(self, address):
        self.page.fill_in_field(self.Locators.BASIC_ADDRESS_LINE_4, address)
        return self

    def fill_in_city_town_field(self, address):
        self.page.fill_in_field(self.Locators.BASIC_CITY_TOWN, address)
        return self

    def fill_in_postcode_field(self, address):
        self.page.fill_in_field(self.Locators.BASIC_POST_CODE, address)
        return self

    def click_save_button(self):
        self.page.click(self.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.XPATH, "// iframe[contains( @ src, 'addressshared')]")
        BASIC_ADDRESS_LINE_1 = (By.CSS_SELECTOR, "#id_Address_AddressStore_AddressLine1")
        BASIC_ADDRESS_LINE_2 = (By.CSS_SELECTOR, "#id_Address_AddressStore_AddressLine2")
        BASIC_ADDRESS_LINE_3 = (By.CSS_SELECTOR, "#id_Address_AddressStore_AddressLine3")
        BASIC_ADDRESS_LINE_4 = (By.CSS_SELECTOR, "#id_Address_AddressStore_AddressLine4")
        BASIC_CITY_TOWN = (By.CSS_SELECTOR, "#id_Address_AddressStore_CityTown")
        BASIC_POST_CODE = (By.CSS_SELECTOR, "#AddressStorePostCode")
        SAVE_BUTTON = (By.ID, "ajaxMainAddressPanel_2_4")
