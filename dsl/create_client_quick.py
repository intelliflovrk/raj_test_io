from ioffice.userdashboard import UserDashboardPage
from ioffice.clients.base import BaseClientPage
from ioffice.add_client_quick import AddClientQuickPage
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.client_search import ClientSearch
from ioffice.clients.details.base import BaseDetailsPage
from ioffice.clients.details.personal import ViewPersonalPage
from ioffice.clients.details.addresses import Addresses
from ioffice.clients.details.contact import Contact
from ioffice.clients.details.notes import Notes
from dsl.search import Search
from fakedata import *
import time


class AddClientQuick:
    def __init__(self, config):
        self.config = config

    def navigate_to_details(self):
        BaseClientPage(self.config).level3_menu().click_details()
        return self

    def navigate_to_personal_tab(self):
        BaseDetailsPage(self.config).details_navigation_menu().click_personal_tab()
        return self

    def navigate_to_addresses_tab(self):
        BaseDetailsPage(self.config).details_navigation_menu().click_addresses_tab()
        return self

    def navigate_to_contact_tab(self):
        BaseDetailsPage(self.config).details_navigation_menu().click_contact_tab()
        return self

    def navigate_to_notes_tab(self):
        BaseDetailsPage(self.config).details_navigation_menu().click_notes_tab()
        return self

    def using_quick_add_client_form(self):
        UserDashboardPage(self.config).click_quick_add_client()
        return self

    def add_basic_client_details(self):
        data = utils.get_common_data(self.config)["test_data"]["add_basic_client_details"]
        self.firstname = rand_firstname(self, "first_name")
        self.lastname = rand_lastname(self, "last_name")
        AddClientQuickPage(self.config).fill_in_firstlife_firstname_field(self.firstname) \
            .fill_in_firstlife_lastname_field(self.lastname) \
            .fill_in_firstlife_dateofbirth_field(data["DATE_OF_BIRTH"]) \
            .select_firstlife_client_category(data["first_life_client_category"]) \
            .select_gender(data["FIRST_LIFE_GENDER_SELECT_BOX"]) \
            .fill_in_ni_number_field(
            utils.get_common_data(self.config)["test_data"]["add_ni_number"]["NI_NUMBER"])
        return self

    def add_client_address_details(self):
        AddClientQuickPage(self.config).fill_in_form(
            utils.get_common_data(self.config)["basic_data"]["special_basic_address"], AddClientQuickPage)
        return self

    def add_client_contact_details(self):
        AddClientQuickPage(self.config).fill_in_mobile_field(
            utils.get_common_data(self.config)["basic_data"]["basic_contact"]["BASIC_MOBILE_NUMBER"])
        return self

    def select_adviser(self):
        data = utils.get_common_data(self.config)["advisers"]
        adviser_dialog = AddClientQuickPage(self.config).open_adviser_dialog()
        adviser_dialog.clear_adviser_firstname_field() \
            .fill_in_adviser_firstname_field(data["default"]["firstname"]) \
            .click_search() \
            .click_first_result() \
            .close_io_dialog()
        return self

    def add_client_notes(self):
        AddClientQuickPage(self.config).fill_in_notes_field(
            utils.get_common_data(self.config)["basic_data"]["basic_text"]["BASIC_TEXT"])
        time.sleep(3)
        return self

    def save(self):
        AddClientQuickPage(self.config).click_save()
        return self

    def search_for_client(self):
        ClientDashboardPage(self.config).click_clients_tab()
        ClientSearch(self.config)\
            .select_search_option(utils.get_common_data(self.config)["test_data"]["client_search_data"]["full_search"])\
            .click_clear_button() \
            .fill_in_firstname(self.firstname) \
            .fill_in_lastname(self.lastname)
        Search(self.config).search_and_open_first_link()
        return self

    def verify_client_created(self):
        assert ClientDashboardPage(
            self.config).get_client_bar_info() == \
               self.firstname + " " + self.lastname, "Client not successfully created"
        return self

    def verify_client_personal_details_saved(self):
        data = utils.get_common_data(self.config)["test_data"]["add_basic_client_details"]
        personal_tab = ViewPersonalPage(self.config)
        assert personal_tab.get_firstname() == self.firstname, "First name has not been saved."
        assert personal_tab.get_lastname() == self.lastname, "Last name has not been saved."
        assert personal_tab.get_gender() == data[
            "FIRST_LIFE_GENDER_SELECT_BOX"], "Gender has not been saved."
        assert personal_tab.get_dob() == data["DATE_OF_BIRTH"], "DOB has not been saved."
        assert personal_tab.get_ni_number() == \
               utils.get_common_data(self.config)["test_data"]["add_ni_number"][
                   "NI_NUMBER"], "NI Number has not been saved."
        return self

    def verify_client_address_details_saved(self):
        data = utils.get_common_data(self.config)["basic_data"]["basic_address"]
        addresses_tab = Addresses(self.config)
        assert addresses_tab.get_address_line_1() == data[
            "BASIC_ADDRESS_LINE_1"], "Address line 1 has not been saved."
        assert addresses_tab.get_address_line_2() == data[
            "BASIC_ADDRESS_LINE_2"], "Address line 2 has not been saved."
        assert addresses_tab.get_address_line_3() == data[
            "BASIC_ADDRESS_LINE_3"], "Address line 3 has not been saved."
        assert addresses_tab.get_city_town() == data[
            "BASIC_CITY_TOWN"], "city/town has not been saved."
        assert addresses_tab.get_postcode() == data["BASIC_POST_CODE"], "postcode has not been saved."
        return self

    def verify_client_contact_details_saved(self):
        assert Contact(self.config).get_contact() == \
               utils.get_common_data(self.config)["basic_data"]["basic_contact"][
                   "BASIC_MOBILE_NUMBER"], "Mobile number has not been saved."
        return self

    def verify_client_note_details_saved(self):
        assert Notes(self.config).get_notes() == \
               utils.get_common_data(self.config)["basic_data"]["basic_text"][
                   "BASIC_TEXT"], "Note has not been saved."
        return self
