from ioffice.clients.base import BaseClientPage
from ioffice.clients.details.base import BaseDetailsPage
from dsl.search import SearchClient
from fakedata import *
from ioffice.clients.details.addresses import Addresses
from ioffice.clients.details.client_address_dialog import ClientAddressDialog
from ioffice.clients.details.summary import ViewSummaryPage
from ioffice.clients.details.personal import ViewPersonalPage
from utils import *


class ClientDetails(SearchClient):

    def navigate_to_details(self):
        BaseClientPage(self.config).level3_menu().click_details()
        return self

    def navigate_to_summary_tab(self):
        BaseDetailsPage(self.config)\
            .details_navigation_menu()\
            .click_summary_tab()
        return ClientDetails._Summary(self)

    def navigate_to_personal_tab(self):
        BaseDetailsPage(self.config)\
            .details_navigation_menu()\
            .click_personal_tab()
        return ClientDetails._Personal(self)

    def navigate_to_addresses_tab(self):
        BaseDetailsPage(self.config).details_navigation_menu().click_addresses_tab()
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

    def delete_client_address(self):
        Addresses(self.config).select_result_per_page("250").click_delete_link(utils.get_temp_data(self.config, 'address')['id']).click_ok_in_browser_confirmation_dialog()
        return self

    def verify_client_address_details_deleted(self):
        assert Addresses(self.config).is_address_id_present(utils.get_temp_data(self.config, 'address')['id']),\
            "Addresses not deleted successfully."
        return self

    def edit_client_address_line_1_and_postcode(self):
        Addresses(self.config).select_result_per_page("250") \
            .click_edit_link(utils.get_temp_data(self.config, 'address')['id'])\
            .clear_address_line_1() \
            .fill_in_address_line_1(utils.get_common_data(self.config)["basic_data"]["basic_address"]["BASIC_ADDRESS_LINE_1"])\
            .clear_postcode()\
            .fill_in_postcode(utils.get_common_data(self.config)["basic_data"]["basic_address"]["BASIC_POST_CODE"]) \
            .click_save_button().wait_until_please_wait_spinner_present()
        return self

    def verify_client_address_details_updated(self):
        assert Addresses(self.config).get_updated_address_line_1(utils.get_temp_data(self.config, 'address')['id']) ==\
            utils.get_common_data(self.config)["basic_data"]["basic_address"]["BASIC_ADDRESS_LINE_1"],\
            "Addresses Line 1 not updated successfully."
        assert Addresses(self.config).get_updated_postcode(utils.get_temp_data(self.config, 'address')['id']) ==\
            utils.get_common_data(self.config)["basic_data"]["basic_address"]["BASIC_POST_CODE"], \
            "Postcode not updated successfully."
        return self

    def using_add_address_dialog(self):
        Addresses(self.config).click_add_new()
        return ClientDetails._ClientAddressDialog(Addresses(self.config), self)

    class _ClientAddressDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ClientAddressDialog(current_page)

        def add_address_details(self):
            data = utils.get_common_data(self.config)["basic_data"]["basic_address"]
            self.dialog\
                .fill_in_address_line_1_field(data["BASIC_ADDRESS_LINE_1"])\
                .fill_in_address_line_2_field(data["BASIC_ADDRESS_LINE_2"])\
                .fill_in_address_line_3_field(data["BASIC_ADDRESS_LINE_3"])\
                .fill_in_address_line_4_field(data["BASIC_ADDRESS_LINE_4"])\
                .fill_in_city_town_field(data["BASIC_CITY_TOWN"])\
                .fill_in_postcode_field(data["BASIC_POST_CODE"])\
                .click_save_button()
            return self.journey

    class _Summary:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = ViewSummaryPage(self.config)

        def edit_servicing_details(self):
            self.page.click_edit()\
                .select_service_status(get_common_data(self.config)["basic_data"]["basic_service_status"])\
                .wait_until_please_wait_spinner_present()\
                .click_save()\
                .wait_until_please_wait_spinner_present()
            return self

        def verify_service_status(self):
            expected_service_status = get_common_data(self.config)["basic_data"]["basic_service_status"]
            current_service_status = ViewSummaryPage(self.config).get_service_status()
            assert current_service_status == expected_service_status, \
                f"Expected service status is {expected_service_status}. Observed service status is {current_service_status}"
            return self.journey

    class _Personal:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = ViewPersonalPage(self.config)

        def edit_personal_details(self):
            self.page.click_edit_button()\
                .fill_in_ni_number(get_common_data(self.config)["test_data"]["add_ni_number"]["NI_NUMBER"])\
                .click_save_button()
            return self

        def verify_ni_number(self):
            expected_ni_number = get_common_data(self.config)["test_data"]["add_ni_number"]["NI_NUMBER"]
            current_ni_number = ViewPersonalPage(self.config).get_ni_number()
            assert current_ni_number == expected_ni_number, \
                f"Expected NI number is {expected_ni_number}. Observed NI number is {current_ni_number}"
            return self.journey
