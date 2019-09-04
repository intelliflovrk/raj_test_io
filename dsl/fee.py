import utils
from dsl.search import SearchClient
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.add_fee_dialog import BaseAddFeeDialog
from ioffice.clients.client_fee import BaseFeesPage


class Fee(SearchClient):
    def __init__(self, config):
        super().__init__(config)
        self.dialog = {}
        self.data = utils.get_common_data(self.config)["test_data"]["fee_data"]

    def using_add_fee_dialog(self):
        clientdashboardpage = ClientDashboardPage(self.config)
        clientdashboardpage.client_actions_menu() \
            .hover_over_client_actions() \
            .add_fee()
        self.dialog = Fee._AddFeeDialog(clientdashboardpage, self)
        return self.dialog

    def verify_if_fee_details_opened(self):
        assert BaseFeesPage(self.config).is_title_matches(), "Fee Details Page Title is not matching."
        return self

    def save_fee_details(self):
        fee_id = BaseFeesPage(self.config).get_fee_id()
        utils.add_temp_data(self.config, "fee", {"id": fee_id})
        fee_ref = BaseFeesPage(self.config).get_fee_ref()
        utils.update_temp_data(self.config, "fee", 0, "sequentialRef", fee_ref)
        fee_total_amount = BaseFeesPage(self.config).get_total_amount()
        utils.update_temp_data(self.config, "fee", 0, "net", {"amount": fee_total_amount})
        return self

    def verify_fee_category(self):
        assert BaseFeesPage(self.config).get_fee_category() == self.data["fee_category"], \
            "Incorrect Fee Category"
        return self

    def verify_fee_charging_type(self):
        assert BaseFeesPage(self.config).get_fee_charging_type() == self.data["fee_charging_type"], \
            "Incorrect Fee Charging Type"
        return self

    def verify_if_fee_status_is_paid(self):
        assert BaseFeesPage(self.config).get_fee_status() == utils.get_common_data(self.config)["test_data"]["fee_data"]["fee_paid_status"], \
            "Incorrect Fee Status"
        return self

    class _AddFeeDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = BaseAddFeeDialog(current_page)
            self.data = journey.data

        def add_initial_fee_with_basic_details(self, payment_type):
            data = utils.get_common_data(self.config)["advisers"]
            self.dialog.open_adviser_search_dialog().clear_adviser_firstname_field() \
                .fill_in_adviser_firstname_field(data["default"]["firstname"]) \
                .click_search() \
                .click_first_result() \
                .close_io_dialog()
            self.dialog.select_fee_type(self.data["fee_type"])\
                .select_payment_type(payment_type)\
                .select_fee_charging_type(self.data["fee_charging_type"])\
                .select_net_amount()\
                .select_advice_category(self.data["advice_category"])\
                .fill_in_initial_period(self.data["initial_period"])\
                .click_save()\
                .close_io_dialog()
            return self.journey
