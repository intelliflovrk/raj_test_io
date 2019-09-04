import datetime
import os
import time
import utils
from dsl.fee import Fee
from dsl.io_navigation import MyDashboardNavigation
from dsl.search import SearchClient
from ioffice.import_statement_dialog import ImportProviderStatementDialog
from ioffice.income.electronic_import import ElectronicImportsPage
from ioffice.income.statement_search import StatementSearchPage
from ioffice.plans.base import BasePlanPage


class ProviderStatement:

    def __init__(self, config):
        self.config = config

    def add_plan_and_plan_fee(self):
        data = utils.get_common_data(self.config)["test_data"]["change_plan_status_data"]
        SearchClient(self.config).open_client_by_url() \
            .using_add_plan_wizard() \
            .add_mortgage_plan_with_basic_details()\
            .finish() \
            .open_change_plan_status_dialog() \
            .change_plan_status_to(data["submitted_to_provider"]) \
            .open_change_plan_status_dialog() \
            .change_plan_status_to(data["inforce"]) \
            .open_add_fee_from_plan_action() \
            .add_initial_fee_with_basic_details(
            utils.get_common_data(self.config)["test_data"]["fee_data"]["payment_type_by_provider"])
        BasePlanPage(self.config).click_open_first_plan_fee()
        Fee(self.config).save_fee_details() \
            .open_change_fee_status_dialog() \
            .change_fee_status_to(data["due"])
        return self

    def navigate_to_statement_search(self):
        MyDashboardNavigation(self.config).income().provider_statements_tab().statement_search_tab()
        return self

    def create_statement(self):
        data = utils.get_common_data(self.config)["test_data"]["fee_data"]
        StatementSearchPage(self.config) \
            .click_clear() \
            .fill_in_amount(data["fee_amount"]) \
            .open_provider_search_dialog() \
            .select(data["plan_fee_provider"]) \
            .click_ok()
        StatementSearchPage(self.config) \
            .click_create() \
            .wait_until_please_wait_spinner_present()
        return self

    def search_statement(self):
        data = utils.get_common_data(self.config)["test_data"]
        StatementSearchPage(self.config) \
            .select_statement_search_type(data["provider_statement_data"]["provider_statement_advanced_search"]) \
            .click_clear() \
            .fill_in_high_state_amount(data["fee_data"]["fee_amount"])\
            .select_matched(data["provider_statement_data"]["not_matched"])\
            .click_search()
        return self

    def allocate_statement(self):
        data =utils.get_common_data(self.config)["test_data"]["provider_statement_data"]
        client = utils.get_temp_data(self.config, "client")
        StatementSearchPage(self.config) \
            .click_open() \
            .select_fee_type(data["int_fee"]) \
            .fill_in_client_name(client["name"]) \
            .fill_in_fee_amount(data["amount"]) \
            .click_create()\
            .wait_until_please_wait_spinner_present()\
            .click_save()\
            .click_allocate()\
            .click_clear()\
            .fill_in_first_name(client["person"]["firstName"]) \
            .click_search() \
            .select_first_line_item() \
            .click_allocate() \
            .select_first_link_to_fee() \
            .click_allocate_to_fee() \
            .wait_until_please_wait_spinner_present()
        StatementSearchPage(self.config).click_close()
        return self

    def delete_statements(self):
        StatementSearchPage(self.config).click_search().select_first_statement()\
            .click_delete()
        utils.switch_and_accept_alert(self.config)
        return self


class ElectronicImports(ProviderStatement):

    def navigate_to_electronic_imports(self):
        MyDashboardNavigation(self.config).income().provider_statements_tab().electronic_imports_tab()
        return self

    def download_blank_io_template(self):
        ElectronicImportsPage(self.config).click_download_blank_io_template()
        return self

    def import_completed_io_template(self, file_name):
        ElectronicImportsPage(self.config) \
            .click_import_completed_io_template()
        ElectronicImports._ImportProviderStatement(self) \
            .send_unique_file(file_name) \
            .import_statement()
        return self

    def verify_documents_downloaded(self):
        time.sleep(30)
        utils.verify_file_is_downloaded(utils.get_download_folder(self.config),
                                        utils.get_common_data(self.config)["test_data"]["provider_statement_data"][
                                            "xls_name"])
        return self

    def verify_imported_statement_synced(self):
        assert ElectronicImportsPage(self.config).get_import_amount_value() == \
               utils.get_common_data(self.config)["test_data"]["provider_statement_data"][
                   "import_amount"], "Import not successfull"
        assert ElectronicImportsPage(self.config).get_import_date_value() == datetime.datetime.today().strftime(
            '%d/%m/%Y'), \
            "Import not successfull"
        return self

    def reset_import_statement_file_name(self, file_name):
        os.renames(self.config.unique_file_url, utils.get_test_documents_file_url(
            utils.get_common_data(self.config)["test_data"]["provider_statement_data"][file_name]))
        return self

    def delete_imported_statement(self):
        ElectronicImportsPage(self.config) \
            .click_first_import_statement_radio_button() \
            .click_first_import_statement_delete_button()
        utils.switch_and_accept_alert(self.config)
        ElectronicImportsPage(self.config).wait_until_please_wait_spinner_present()
        return self

    def add_provider_to_statement(self):
        data = utils.get_common_data(self.config)["test_data"]["fee_data"]
        ElectronicImportsPage(self.config) \
            .click_edit_button()
        StatementSearchPage(self.config) \
            .open_provider_search_dialog() \
            .select(data["plan_fee_provider"]) \
            .click_ok()
        ElectronicImportsPage(self.config).click_update_button() \
            .wait_until_please_wait_spinner_present()
        return self

    def make_statement_live(self):
        ElectronicImportsPage(self.config) \
            .click_first_radio_button() \
            .click_make_live_button()
        utils.switch_and_accept_alert(self.config)
        ElectronicImportsPage(self.config).wait_until_please_wait_spinner_present()
        return self

    def verify_statement_removed_from_list(self):
        assert ElectronicImportsPage(self.config).is_abacus_mortgages_statement_present() == False,\
            "Statement removal not successfull"
        return self

    def verify_statement_presence_in_provider_statement(self):
        assert ElectronicImportsPage(self.config).get_live_statement_date_value() == datetime.datetime.today().strftime(
            '%d %b %Y'), \
            "Statement not found"
        return self

    def search_for_live_statement(self):
        data = utils.get_common_data(self.config)["test_data"]["provider_statement_data"]
        StatementSearchPage(self.config) \
            .select_statement_search_type(data["provider_statement_advanced_search"]) \
            .click_clear() \
            .fill_in_low_state_amount(data["live_statement_amount"]) \
            .click_search()
        return self

    def delete_live_statements(self):
        self.navigate_to_statement_search() \
            .search_for_live_statement()
        StatementSearchPage(self.config) \
            .select_first_statement() \
            .click_delete()
        utils.switch_and_accept_alert(self.config)
        ElectronicImportsPage(self.config).wait_until_please_wait_spinner_present()
        return self

    class _ImportProviderStatement:

        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ImportProviderStatementDialog(self.config)

        def send_unique_file(self, file_name):
            self.config.file_name = file_name
            self.dialog.send_unique_file(
                utils.make_file_name_unique(
                    utils.get_common_data(self.config)["test_data"]["provider_statement_data"][file_name]))
            return self

        def import_statement(self):
            self.dialog.click_run_button()
            ElectronicImportsPage(self.config).close_import_provider_statement_dialog()
            return self.journey
