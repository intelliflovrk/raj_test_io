import pytest
from dsl.cash_receipts import CashReceipts

pytestmark = [pytest.mark.cash_receipt, pytest.mark.io_all, pytest.mark.fee]


@pytest.mark.usefixtures("ui_delete_cash_receipt")
@pytest.mark.usefixtures("ui_move_fee_to_cancelled_status")
@pytest.mark.usefixtures("ui_delete_fee")
@pytest.mark.usefixtures("ui_move_fee_to_due_status")
@pytest.mark.usefixtures("api_create_client_fee")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_fee_cash_receipts(config):
    """Adding fee to cash receipt and verify its status"""
    test = (CashReceipts(config)
            .navigate_to_cash_receipts_search()
            .create_fee_cash_receipt()
            .search_cash_receipt()
            .using_cash_receipt_matching_dialog()
                .match_fee()
            .open_fee()
            .verify_if_fee_status_is_paid()
            )
