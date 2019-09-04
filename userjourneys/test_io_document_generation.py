import pytest
from dsl.generate_document import GenerateDocument

pytestmark = [pytest.mark.documentdesigner, pytest.mark.io_all]


@pytest.mark.usefixtures("ui_clear_document_queue")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_create_client")
def test_generate_basic_pdf_document_for_client(config):
    """Test Description: Generating a PDF document from a pre-defined template for a client."""
    test = (GenerateDocument(config)
            .open_client_by_url()
            .using_generate_menu()
                .generate_pdf_basic_template()
            .assert_if_document_queue_open()
            .wait_until_document_completed()
            .assert_if_pdf_doc_generated()
            )


@pytest.mark.usefixtures("file_delete_system_based_template")
@pytest.mark.usefixtures("api_delete_client_relationship")
@pytest.mark.usefixtures("ui_clear_document_queue")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_create_joint_client")
def test_client_document_designer_fields(config):
    """Test Description: Generating a Word document from a pre-defined template for a client."""
    test = (GenerateDocument(config)
            .open_client_by_url()
            .using_generate_menu()
                .generate_portfolio_report_system_based_template_for_joint_client()
            .open_document_once_completed()
            .verify_joint_client_populated_on_first_page()
            .verify_published_date_equals_to_current_date()
            )


@pytest.mark.usefixtures("file_delete_system_based_template")
@pytest.mark.usefixtures("ui_clear_document_queue")
@pytest.mark.usefixtures("api_add_client_address")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_client_address_snippet(config):
    """Test Description: Generating a Word document using client address snippet on a pre-defined template."""
    test = (GenerateDocument(config)
            .open_client_by_url()
            .using_generate_menu()
                .generate_address_template_for_client()
            .open_document_once_completed()
            .verify_client_address_captured()
            )


@pytest.mark.usefixtures("ui_delete_funds_for_sub_plan")
@pytest.mark.usefixtures("ui_delete_plans_valuations")
@pytest.mark.usefixtures("ui_clear_document_queue")
@pytest.mark.usefixtures("api_delete_plans_contributions")
@pytest.mark.usefixtures("api_delete_plans_withdrawals")
@pytest.mark.usefixtures("api_delete_client_plans")
@pytest.mark.usefixtures("file_delete_system_based_template")
@pytest.mark.usefixtures("api_create_valuation_for_client_plans")
@pytest.mark.usefixtures("api_create_fund_for_sub_plan")
@pytest.mark.usefixtures("ui_add_plan_to_wrapper")
@pytest.mark.usefixtures("api_create_pre_existing_pension_plan")
@pytest.mark.usefixtures("ui_add_plan_report_note")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_create_withdrawal")
@pytest.mark.usefixtures("api_create_contribution")
@pytest.mark.usefixtures("api_create_pre_existing_wrap_plan")
@pytest.mark.usefixtures("api_create_client")
def test_wrap_plan_document_designer_fields(config):
    """Test Description: Generating a Word document from a pre-defined template for a client. Verify client
    s plans details are present in the doc."""
    test = (GenerateDocument(config)
            .open_client_by_url()
            .using_generate_menu()
                .generate_portfolio_report_system_based_template_with_wrap_investments()
            .open_document_once_completed()
            .verify_wrap_plan_details_captured()
            .verify_sub_plan_details_captured()
            )


@pytest.mark.usefixtures("ui_delete_funds")
@pytest.mark.usefixtures("ui_delete_plan_valuations")
@pytest.mark.usefixtures("ui_clear_document_queue")
@pytest.mark.usefixtures("api_delete_client_plans")
@pytest.mark.usefixtures("file_delete_system_based_template")
@pytest.mark.usefixtures("api_create_withdrawal")
@pytest.mark.usefixtures("api_create_contribution")
@pytest.mark.usefixtures("api_create_valuation_for_client_plans")
@pytest.mark.usefixtures("api_create_fund")
@pytest.mark.usefixtures("api_create_pre_existing_investment_plan")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_investment_plan_document_designer_fields(config):
    """Test Description: Generating a Word document from a pre-defined template for a client. Verify client
    s investment plan details are present in the doc."""
    test = (GenerateDocument(config)
            .open_client_by_url()
            .using_generate_menu()
                .generate_portfolio_report_system_based_template_with_investments()
            .open_document_once_completed()
            .verify_investment_plan_details_captured()
            )