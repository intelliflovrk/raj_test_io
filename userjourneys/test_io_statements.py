import pytest
from dsl.provider_statement import *

pytestmark = [pytest.mark.io_all, pytest.mark.statement, pytest.mark.last]


@pytest.mark.skip(reason="PRD Defect IP-55601")
@pytest.mark.fee
@pytest.mark.usefixtures("ui_delete_cash_receipt")
@pytest.mark.usefixtures("ui_delete_statements_on_first_page")
@pytest.mark.usefixtures("ui_move_fee_to_draft_status")
@pytest.mark.usefixtures("ui_delete_fee")
@pytest.mark.usefixtures("ui_create_client_plan_fee")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_income_statement_fees(config):
    """ Test Description: Adding a plan with fee to a client.
    Create statement and cash receipt, allocate to created fee and verify its status. """
    test = (ProviderStatement(config)
            .navigate_to_statement_search()
                .create_statement()
                .search_statement()
                .allocate_statement()
            .navigate_to_cash_receipts_search()
            .create_fee_cash_receipt()
                .search_cash_receipt()
            .using_cash_receipt_matching_dialog()
                .match_fee_provider_statement()
            .open_fee()
            .verify_if_fee_status_is_paid()
            )


@pytest.mark.usefixtures("ui_delete_live_statements")
@pytest.mark.usefixtures("file_reset_import_statement_file_2_name")
@pytest.mark.usefixtures("ui_login_logout")
def test_make_statement_live(config):
    """ Import completed provider statement template and make it live and verify"""
    test = (ElectronicImports(config)
            .navigate_to_electronic_imports()
                .import_completed_io_template("csv_file_2")
            .add_provider_to_statement()
            .make_statement_live()
            .verify_statement_removed_from_list()
            .navigate_to_statement_search()
            .search_for_live_statement()
            .verify_statement_presence_in_provider_statement()
            )


@pytest.mark.usefixtures("file_delete_import_statement")
@pytest.mark.usefixtures("ui_login_logout")
def test_download_provider_statement_template(config):
    """ Download import provider statement template and verify"""
    test = (ElectronicImports(config)
            .navigate_to_electronic_imports()
                .download_blank_io_template()
            .verify_documents_downloaded()
            )


@pytest.mark.usefixtures("file_reset_import_statement_file_1_name")
@pytest.mark.usefixtures("ui_delete_imported_statement")
@pytest.mark.usefixtures("ui_login_logout")
def test_import_provider_statement_template(config):
    """ Import completed provider statement template and verify data synced"""
    test = (ElectronicImports(config)
            .navigate_to_electronic_imports()
                .import_completed_io_template("csv_file_1")
            .verify_imported_statement_synced()
            )

