import pytest
from dsl.fee import *
from utils import get_common_data

pytestmark = [pytest.mark.fee, pytest.mark.io_all]


@pytest.mark.usefixtures("ui_delete_fee")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_add_basic_initial_fee(config):
    """ Test Description: Adding a fee to a client.
    Verifying that the data is saved. """
    test = (Fee(config)
            .open_client_by_url()
            .using_add_fee_dialog()
                .add_initial_fee_with_basic_details(get_common_data(config)["test_data"]["fee_data"]["payment_type_cheque"])
            .save_fee_details()
            .verify_if_fee_details_opened()
            .verify_fee_category()
            .verify_fee_charging_type()
            )
