import utils
from dsl.fee_actions import FeeActions
from dsl.search import SearchFee
from dsl.fee import Fee
from ioffice.base import IOBasePage
from ioffice.income.cash_receipt_matching_dialog import CashReceiptMatchingDialog
from ioffice.income.cash_receipt_search import CashReceiptSearchPage
from ioffice.income.base import IncomeBasePage


class CashReceipts(Fee, FeeActions, SearchFee):

    def navigate_to_cash_receipts_search(self):
        IOBasePage(self.config).level1_menu()\
            .hover_over_navigation_menu().click_income()
        IncomeBasePage(self.config).level2_menu().click_cash_receipts()
        return self

    def create_fee_cash_receipt(self):
        client = utils.get_temp_data(self.config, "client")
        fee = utils.get_temp_data(self.config, "fee")
        CashReceiptSearchPage(self.config).click_select_category()\
            .select_fee_category()\
            .fill_in_amount(fee["net"]["amount"])\
            .fill_in_description(client["name"])\
            .click_create()
        return self

    def search_cash_receipt(self):
        client = utils.get_temp_data(self.config, "client")
        CashReceiptSearchPage(self.config).click_clear()\
            .fill_in_description_search(client["name"])\
            .click_search().wait_until_please_wait_spinner_present()
        return self

    def using_cash_receipt_matching_dialog(self):
        cash_receipt_search_page = CashReceiptSearchPage(self.config)
        cash_receipt_search_page.click_match()
        self.dialog = CashReceipts._CashReceiptMatchingDialog(cash_receipt_search_page, self)
        return self.dialog

    def delete_cash_receipt(self):
        CashReceiptSearchPage(self.config).select_first_search_result_record()\
            .click_delete().click_ok_in_browser_confirmation_dialog()
        return self

    class _CashReceiptMatchingDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = CashReceiptMatchingDialog(current_page)

        def match_fee(self):
            fee = utils.get_temp_data(self.config, "fee")
            self.dialog.click_clear()\
                .fill_in_io_ref(fee["sequentialRef"])\
                .click_search()\
                .wait_search_results_appear()\
                .select_first_search_result_record()\
                .click_match()\
                .close_io_dialog()
            return self.journey

        def match_fee_provider_statement(self):
            data = utils.get_common_data(self.config)["test_data"]["provider_statement_data"]
            self.dialog.select_provider_statement_match_search_type(data["provider_statement_match_search"])\
                .fill_high_amount(data["amount"])\
                .click_search() \
                .wait_search_results_appear() \
                .select_first_search_result_record() \
                .click_match()\
                .close_io_dialog()
            return self.journey

        def unmatch_fee(self):
            self.dialog.click_unmatch() \
                .close_io_dialog()
            return self.journey
