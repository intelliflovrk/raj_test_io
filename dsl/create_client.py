from dsl.search import SearchClient
from ioffice.clients.base import BaseClientPage
from ioffice.base import IOBasePage
from ioffice.clients.details.base import BaseDetailsPage
from ioffice.clients.details.summary import ViewSummaryPage
from ioffice.userdashboard import UserDashboardPage
from ioffice.add_client_wizard import AddClientWizard
from ioffice.clients.client_dashboard import ClientDashboardPage
from fakedata import *
from utils import *


class CreateClient(SearchClient):

    def using_add_client_wizard(self):
        self.page = IOBasePage(self.config)
        self.page.level1_menu().click_home()
        self.page = UserDashboardPage(self.config)
        self.page.click_add_client()
        self.wizard = CreateClient._ClientWizard(self)
        return self.wizard

    def navigate_to_home(self):
        IOBasePage(self.config).level1_menu().click_home()
        return self

    def navigate_to_summary_tab(self):
        ClientDashboardPage(self.config).level3_menu().click_details()
        BaseDetailsPage(self.config).details_navigation_menu().click_summary_tab()
        return self

    def navigate_to_addresses_tab(self):
        ClientDashboardPage(self.config).level3_menu().click_details()
        BaseDetailsPage(self.config).details_navigation_menu().click_addresses_tab()
        return self

    def verify_address_and_contacts_added(self):
        expected_address = list(utils.get_common_data(self.config)["basic_data"]["basic_address"].values())
        expected_contact = list(utils.get_common_data(self.config)["basic_data"]["basic_contact"].values())
        assert ViewSummaryPage(self.config).get_address_line_1() in expected_address, "Address Line 1 not matching"
        assert ViewSummaryPage(self.config).get_address_line_2() in expected_address, "Address Line 2 not matching"
        assert ViewSummaryPage(self.config).get_address_line_3() in expected_address, "Address Line 3 not matching"
        assert ViewSummaryPage(self.config).get_address_line_4() in expected_address, "Address Line 4 not matching"
        assert ViewSummaryPage(self.config).get_city_or_town_and_postcode() == expected_address[-2] + " " + expected_address[-1], "City/Postcode not matching"
        assert ViewSummaryPage(self.config).get_mobile_number() in expected_contact, "Mobile number not matching"
        assert ViewSummaryPage(self.config).get_fax_number() in expected_contact, "Fax Number not matching"
        return self

    def save_client_id(self):
        client_id = BaseClientPage(self.config).get_client_id()
        update_temp_data(self.config, "client", 0, "id", client_id)
        return self

    def save_corporate_client_id_and_name(self):
        client_id = BaseClientPage(self.config).get_client_id()
        client_name = BaseClientPage(self.config).get_client_bar_info()
        add_temp_data(self.config, "client", {"id": client_id, "corporate": {"name": client_name}})
        return self

    class _ClientWizard:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddClientWizard(self.config)
            self.corporate_name = get_common_data(self.config)["test_data"]["add_basic_client_details"]["corporate_name"] + fakedata.rand_text()
            assert self.wizard.is_title_matches(), "Title does not match the Add Client Wizard"

        def add_basic_corporate_client(self):
            self.select_client_type_corporate()\
                .fill_in_corporate_basic_details_form()\
                .select_adviser()\
                .add_address()\
                .add_contact()\
                .add_notes()
            return self

        def select_client_type_corporate(self):
            self.wizard.basic_details_stage().select_client_type(
                get_common_data(self.config)["test_data"]["add_basic_client_details"]["client_type"])
            return self

        def add_basic_client_details(self):
            self.fill_in_add_basic_client_form()
            self.select_adviser()
            return self

        def fill_in_add_basic_client_form(self):
            utils.add_temp_data(self.config, "client", {"person": {"firstName": rand_firstname(
                self, "first_name"), "lastName": rand_lastname(self, "last_name")}})
            basic_details = self.wizard.basic_details_stage()
            basic_details.goto_stage()
            data = get_common_data(self.config)["test_data"]["add_basic_client_details"]
            basic_details.fill_in_form(data, basic_details)
            basic_details.fill_in_firstname_field(utils.get_temp_data(self.config, "client")["person"]["firstName"])
            basic_details.fill_in_lastname_field(utils.get_temp_data(self.config, "client")["person"]["lastName"])
            assert basic_details.is_current_stage()
            return self

        def fill_in_corporate_basic_details_form(self):
            basic_details = self.wizard.basic_details_stage()
            basic_details.goto_stage()
            basic_details.fill_in_corporate_name_field(self.corporate_name)
            assert basic_details.is_current_stage()
            return self

        def select_adviser(self):
            basic_details = self.wizard.basic_details_stage()
            adviser_dialog = basic_details.open_adviser_dialog()
            data = utils.get_common_data(self.config)["advisers"]
            adviser_dialog.clear_adviser_firstname_field()
            adviser_dialog.fill_in_adviser_firstname_field(data["default"]["firstname"])
            adviser_dialog.click_search()
            adviser_dialog.click_first_result()
            adviser_dialog.close_io_dialog()
            return self

        def add_client_partner_details(self):
            basic_details = self.wizard.basic_details_stage()
            basic_details.select_joint_client_application()
            self.secondlife_lastname = rand_firstname(self, "first_name")
            self.secondlife_firstname = rand_lastname(self, "last_name")
            basic_details.fill_in_second_life_firstname(self.secondlife_firstname)
            basic_details.fill_in_second_life_lastname(self.secondlife_lastname)
            return self

        def add_address(self):
            address = self.wizard.address_stage()
            address.goto_stage()
            assert address.is_current_stage()
            data = utils.get_common_data(self.config)["basic_data"]
            address.page.fill_in_form(data["basic_address"], address)
            return self

        def add_contact(self):
            contact = self.wizard.contact_stage()
            contact.goto_stage()
            assert contact.is_current_stage()
            data = utils.get_common_data(self.config)["basic_data"]
            contact.page.fill_in_form(data["basic_contact"], contact)
            return self

        def add_dpa(self):
            dpa = self.wizard.dpa_stage()
            dpa.goto_stage()
            assert dpa.is_current_stage()
            return self

        def add_marketing_preferences(self):
            marketing = self.wizard.marketing_stage()
            marketing.goto_stage()
            assert marketing.is_current_stage()
            return self

        def add_opportunity(self):
            opportunity = self.wizard.opportunity_stage()
            opportunity.goto_stage()
            assert opportunity.is_current_stage()
            return self

        def add_notes(self):
            notes = self.wizard.notes_stage()
            notes.goto_stage()
            assert notes.is_current_stage()
            return self

        def finish(self):
            self.wizard.click_finish_button(False)
            CreateClient(self.config).save_client_id()
            return self.journey

        def finish_corporate(self):
            self.wizard.click_finish_button(False)
            self.journey.save_corporate_client_id_and_name()
            return self.journey
