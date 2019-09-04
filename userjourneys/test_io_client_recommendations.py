import pytest
from dsl.advice_planning import PlanningOpportunities
from dsl.rebalance import StartRebalanceCommunication, ViewRebalance
import sys

pytestmark = [pytest.mark.recommendation, pytest.mark.model_portfolio, pytest.mark.io_all]


@pytest.mark.usefixtures("ui_delete_recommendations")
@pytest.mark.usefixtures("api_add_delete_client_goal")
@pytest.mark.usefixtures("ui_delete_service_case")
@pytest.mark.usefixtures("ui_delete_funds")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_add_delete_opportunity")
@pytest.mark.usefixtures("api_create_fund")
@pytest.mark.usefixtures("api_create_pre_existing_investment_plan")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_imps_add_manual_recommendation(config):
    """Test Description: Adding manual Switch recommendation with iMPS model portfolio.
    Verifying Transaction details"""
    test = (PlanningOpportunities(config)
        .open_client_by_url()
        .using_planning_opportunities()
            .open_recommendations()
            .using_add_manual_rec_dialog()
                .add_switch_recommendation_details()
                .add_model_portfolio("Automation Test iMPS Model")
                .save_recommendation()
            .open_transaction_details()
                .verify_existing_and_new_funds_present()
                .close_dialog())


@pytest.mark.usefixtures("ui_delete_recommendations")
@pytest.mark.usefixtures("ui_delete_service_case")
@pytest.mark.usefixtures("api_delete_fund_proposal_for_all_plans")
@pytest.mark.usefixtures("ui_delete_funds")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_add_imps_manual_recommendation")
@pytest.mark.usefixtures("api_add_delete_client_goal")
@pytest.mark.usefixtures("ui_add_delete_opportunity")
@pytest.mark.usefixtures("api_create_fund")
@pytest.mark.usefixtures("api_create_pre_existing_investment_plan")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_imps_accept_switch_manual_recommendation(config):
    """Test Description: Accepting manual Switch recommendation with iMPS model portfolio.
    Verifying plan's Fund Proposal."""
    test = (PlanningOpportunities(config)
            .open_client_by_url()
            .using_planning_opportunities()
                .open_recommendations()
                    .accept_manual_recommendation()
                    .open_plan()
            .navigate_to_funds_holdings_tab()
                .verify_fund_proposal_updated())


@pytest.mark.skipif('prd-10' == pytest.config.option.env, reason='IP-58047 ')
@pytest.mark.skipif('recommendation' not in sys.argv,
                    reason='A test excluded from io_all run. '
                           'To run the test please add recommendation marker explicitly.')
@pytest.mark.usefixtures("api_delete_fund_proposal_for_all_plans")
@pytest.mark.usefixtures("ui_delete_funds")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_delete_service_case")
@pytest.mark.usefixtures("api_deactivate_portfolio_model")
@pytest.mark.usefixtures("api_add_imps_model_to_fund_proposal_for_all_plans")
@pytest.mark.usefixtures("api_create_fund")
@pytest.mark.usefixtures("api_create_pre_existing_investment_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("api_create_active_imps_model")
@pytest.mark.usefixtures("ui_login_logout")
def test_imps_start_rebalance_communication_process(config):
    """Test Description: Verify that a recommendation is created against a plan
    once a rebalance communication process has been started."""
    test = (StartRebalanceCommunication(config)
            .using_rebalance_communication_options_dialog()
                .start_rebalance_communication()
            .open_plan()
            .navigate_to_recommendations_tab()
                .verify_recommendation_created("Rebalance")
                .open_recommendation_details()
                    .verify_rebalance_recommendation_details()
                    .close_dialog())


@pytest.mark.skip(reason="IP-57910")
@pytest.mark.skipif('prd-10' == pytest.config.option.env, reason='IP-58047 ')
@pytest.mark.skipif('recommendation' not in sys.argv,
                    reason='A test excluded from io_all run. '
                           'To run the test please add recommendation marker explicitly.')
@pytest.mark.usefixtures("api_delete_fund_proposal_for_all_plans")
@pytest.mark.usefixtures("ui_delete_funds_for_all_plans")
@pytest.mark.usefixtures("api_delete_clients_plans")
@pytest.mark.usefixtures("ui_delete_service_case_for_all_clients")
@pytest.mark.usefixtures("api_deactivate_portfolio_model")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("ui_pfp_accept_recommendation")
@pytest.mark.usefixtures("ui_start_rebalance_communication_process")
@pytest.mark.usefixtures("api_add_imps_model_to_fund_proposal_for_all_plans")
@pytest.mark.usefixtures("api_create_fund_for_all_plans")
@pytest.mark.usefixtures("api_create_pre_existing_investment_plan_for_all_clients")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("api_search_pfp_imps_client_and_save_details")
@pytest.mark.usefixtures("api_create_active_imps_model")
@pytest.mark.usefixtures("ui_login")
def test_imps_rebalance_report(config):
    """Test Description: Verify that a recommendation status is updated in Rebalance Report
    if the recommendation has been accepted in PFP."""
    test = (ViewRebalance(config)
            .download_rebalance_report()
                .verify_recommendation_status_for_clients())
