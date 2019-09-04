import pytest
from dsl.add_investment_plan import *
from dsl.add_retirement_plan import AddRetirementPlan

pytestmark = [pytest.mark.plan, pytest.mark.io_all]


@pytest.mark.valuation
@pytest.mark.usefixtures("ui_delete_plan_valuations")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_create_investment_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_valuation_to_investment_plan(config):
    """ Test Description: Adding a valuation to a investment plan. Verifying that the data is saved."""
    test = (AddInvestmentPlan(config)
            .open_plan_by_url()
            .open_add_valuation_dialog()
                .add_manual_valuation()
            .verify_plan_value()
            )


@pytest.mark.fund
@pytest.mark.usefixtures("ui_delete_funds")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_create_investment_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_fund_to_investment_plan(config):
    """Test Description: Adding a fund to a investment plan. Verifying that the data is saved."""
    test = (AddInvestmentPlan(config)
            .open_plan_by_url()
            .open_add_fund_dialog()
                .add_fund()
            .show_all_holdings()
            .verify_number_of_units_holdings_value()
            )


@pytest.mark.withdrawal
@pytest.mark.usefixtures("api_delete_plans_withdrawals")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_create_investment_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_withdrawal_to_investment_plan(config):
    """Test Description: Adding a withdrawal to a investment plan. Verifying that the data is saved."""
    test = (AddInvestmentPlan(config)
            .open_plan_by_url()
            .go_to_withdrawals()
                .create_withdrawals()
                .verify_withdrawals_data()
            )


@pytest.mark.subplan
@pytest.mark.usefixtures("api_delete_sub_plan")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_create_sipp_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_sub_plan_to_retirement_plan(config):
    """  Adding a basic a sub-plan to a retirement plan. Verifying that the data is saved."""
    test = (AddRetirementPlan(config)
            .open_plan_by_url()
            .using_add_sub_plan_wizard()
                .add_sub_plan_basic_details()
                .finish()
            .verify_if_sub_plan_added()
            )


@pytest.mark.withdrawal
@pytest.mark.usefixtures("api_delete_plans_withdrawals")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_create_sipp_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_withdrawal_to_retirement_plan(config):
    """Adding a withdrawal to a retirement plan. Verifying that the data is saved """
    test = (AddRetirementPlan(config)
            .open_plan_by_url()
            .go_to_withdrawals()
                .create_withdrawals()
                .verify_withdrawals_data()
            )


@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_create_investment_plan")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_plan_change_status_lifecycle(config):
    """ Test Description: open a client with preset lifecycle rule .
    Change the status of the plan and verify the expected message. """
    test = (AddInvestmentPlan(config)
            .open_plan_by_url()
            .open_change_plan_status_dialog()
                .verify_info_message()
            )


@pytest.mark.uploaddocument
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_create_investment_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_upload_plan_document(config):
    """ Test Description: Upload document to a plan and verify it"""
    test = (PlanActions(config)
            .open_plan()
            .using_upload_document_dialog()
                .upload_pdf_document()
            .open_document_details()
                .verify_uploaded_document()
            )
