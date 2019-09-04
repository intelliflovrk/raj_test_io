import pytest
from dsl.get_client_quote import GetClientQuote
from dsl.source_mortgage import MortgageBrainAnywhere
from dsl.advice_planning import PlanningOpportunities

pytestmark = [pytest.mark.quote, pytest.mark.io_all]


@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='AssureWeb needs to be set up in tst environments')
@pytest.mark.skipif('tst-04' == pytest.config.option.env, reason='AssureWeb needs to be set up in tst environments')
@pytest.mark.skipif('uat-10' == pytest.config.option.env, reason='AssureWeb credentials need to be added to the UAT environment (Blocked by IP-45915')
@pytest.mark.assureweb
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_delete_quote")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_get_assureweb_quote(config):
    """ Test Description: Obtains a term  protection quote from AssureWeb and creates a plan from the quote. """
    test = (GetClientQuote(config)
            .open_client_by_url()
            .using_get_new_quote_window()
                .select_quote_product_area('Term Protection')
                .verify_quote_app_exists('Assureweb')
                .open_quote_app('Assureweb')
                .get_assureweb_quote()
            .navigate_to_quotes_and_apps()
                .wait_until_quote_completed()
                .verify_quote_status_is("Complete")
                .verify_quote_product_type_is_term()
            .open_quote()
                .create_plan_from_quote()
            .navigate_to_quotes_apps_tab()
                .verify_plan_created_from_quote()
            .open_plan_and_save_details()
            )


@pytest.mark.skip(reason="IP-50819 it needs to review the journey")
@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='Mortgage Brain needs to be set up in tst environments')
@pytest.mark.skipif('uat-10' == pytest.config.option.env, reason='Mortgate Brain credentials need to be added to the UAT environment (Blocked by IP-45915)')
@pytest.mark.mortgage_brain
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_source_mortgage(config):
    """Create quote using mortgage brain and verify it in IO"""
    test = (MortgageBrainAnywhere(config)
            .open_client_by_url()
            .using_source_mortgage_dialog()
                .open_mortgage_brain_anywhere()
            .verify_mortgage_brain_anywhere_status_code()
            .switch_to_io_window()
            )


@pytest.mark.skipif('tst-05' == pytest.config.option.env, reason='Unable to setup app in tst-05')
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_launch_get_new_illustration(config):
    """ Test Description: Verify that an app appears in the Get New Illustration dialog to simulate a real
    quote app"""
    test = (GetClientQuote(config)
            .open_client_by_url()
            .using_get_new_illustration_window()
                .select_illustration_product_area('Collective Investments')
                .verify_illustration_app_exists('Test Quote App')
                .close_get_new_ilustration_window()
            )


@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='IP-59229')
@pytest.mark.usefixtures("file_delete_quote_document_pdf")
@pytest.mark.usefixtures("api_upload_documents_to_quote")
@pytest.mark.usefixtures("api_set_quote_status_to_complete")
@pytest.mark.usefixtures("api_create_client_quote")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_get_quote(config):
    """ Test Description: Obtains a quote and verifies that the quote was successful and contains documents """
    test = (GetClientQuote(config)
            .open_client_by_url()
            .navigate_to_quotes_and_illustrations()
                .wait_until_quote_illustration_completed()
                .verify_quote_illustration_status_is("Complete")
                .verify_quote_illustration_product_type_is("Investment")
                .verify_provider_is_app_name()
                .verify_quote_reference()
                .open_quote_by_reference()
                .navigate_to_quote_documents_tab()
                .verify_document_has_been_uploaded_for_quote()
                .download_quote_document()
                .verify_quote_document_downloaded()
            )


@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='IP-59229')
@pytest.mark.usefixtures("file_delete_quote_result_document_pdf")
@pytest.mark.usefixtures("api_upload_documents_to_quote_result")
@pytest.mark.usefixtures("api_create_client_quote_result")
@pytest.mark.usefixtures("api_set_quote_status_to_complete")
@pytest.mark.usefixtures("api_create_client_quote")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_get_quote_and_verify_quote_result(config):
    """ Test Description: Obtains a quote and verifies that the quote contains quote results and documents """
    test = (GetClientQuote(config)
            .open_client_by_url()
            .navigate_to_quotes_apps_tab()
            .navigate_to_quotes_and_illustrations()
                .wait_until_quote_illustration_completed()
                .verify_quote_illustration_status_is("Complete")
                .verify_quote_illustration_product_type_is("Investment")
                .verify_provider_is_app_name()
                .verify_quote_reference()
            .open_quote_by_reference()
            .verify_columns_are_present_for_protection_quote_results()
            .verify_contribution_amounts_are_correct()
            .using_quote_result_details_dialog()
                .verify_columns_for_investment_quote_are_correct()
                .verify_contributions_are_correct_for_investment_quote()
                .close_dialog()
            .using_quote_result_document_dialog()
                .verify_document_has_been_uploaded_for_quote_result()
                .download_quote_result_document()
                .verify_quote_result_document_downloaded()
                .close_dialog()
            )


@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='IP-59229')
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("api_delete_client_relationship")
@pytest.mark.usefixtures("api_upload_quote_documents_to_joint_client")
@pytest.mark.usefixtures("api_set_quote_status_to_complete")
@pytest.mark.usefixtures("api_create_joint_client_quote")
@pytest.mark.usefixtures("ui_login_logout")
def test_create_joint_quote_and_documents(config):
    """ Test Description: create joint quote and documents. Verify quote and document access to both life """
    test = (GetClientQuote(config)
            .open_client_by_url()
            .navigate_to_quotes_and_illustrations()
            .open_quote_by_reference()
                .verify_quote_id()
            .navigate_to_client_document()
                .verify_quote_document_present()
            .open_second_life()
            .navigate_to_quotes_and_illustrations()
            .open_quote_by_reference()
                .verify_quote_id()
            .navigate_to_client_document()
                .verify_quote_document_present()
            )


@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='IP-59229')
@pytest.mark.usefixtures("api_delete_second_life_documents")
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("api_delete_client_relationship")
@pytest.mark.usefixtures("api_upload_quote_result_documents_to_joint_client")
@pytest.mark.usefixtures("api_create_client_joint_quote_result")
@pytest.mark.usefixtures("api_set_quote_status_to_complete")
@pytest.mark.usefixtures("api_create_joint_client_quote")
@pytest.mark.usefixtures("ui_login_logout")
def test_create_joint_quote_results_and_documents(config):
    """ Test Description: create joint quote results and documents.
    Verify quote results and documents access to both life """
    test = (GetClientQuote(config)
            .open_client_by_url()
            .open_quote()
                .verify_joint_quote_result_created()
            .using_quote_result_document_dialog()
                .verify_document_has_been_uploaded_for_quote_result()
                .close_dialog()
            .navigate_to_client_document()
                .verify_quote_result_document_present()
            .open_second_life()
            .open_quote()
                .verify_joint_quote_result_created()
            .using_quote_result_document_dialog()
                .verify_document_has_been_uploaded_for_quote_result()
                .close_dialog()
            .navigate_to_client_document()
                .verify_quote_result_document_present()
            )


@pytest.mark.usefixtures("ui_delete_service_case")
@pytest.mark.usefixtures("ui_add_delete_opportunity")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_launch_get_new_quote_from_research_tools(config):
    """ Test Description: Verify that it is possible to launch Get New Quote wizard by using Get Quote tool."""
    test = (PlanningOpportunities(config)
            .open_client_by_url()
            .using_planning_opportunities()
                .open_research_tools()
                    .open_get_new_quote_wizard_using_get_quote_tool()
                        .select_product_area('Term Protection')
                        .verify_quote_portal_present('Assureweb')
                        .close_get_new_quote_wizard()
            )