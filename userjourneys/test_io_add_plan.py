import pytest
from dsl.add_investment_plan import *
from dsl.add_mortgage_plan import AddMortgagePlan
from dsl.add_protection_plan import AddProtectionPlan
from dsl.add_retirement_plan import AddRetirementPlan
from dsl.complete_scheme import CompleteSchemes

pytestmark = [pytest.mark.plan, pytest.mark.io_all]


@pytest.mark.usefixtures("api_delete_plans_contributions")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_add_investment_plan_with_contribution(config):
    """ Test Description: Adding a basic investment plan with contribution. Verifying that the data is saved."""
    test = (AddInvestmentPlan(config)
            .open_client_by_url()
            .using_add_plan_wizard()
                .add_investment_plan_basic_details()
                .add_investment_plan_details()
                .finish()
            .verify_if_plan_summary_opened()
            .verify_plan_provider_and_type()
            .verify_current_regular_contribution_value()
            .go_to_contributions()
            .verify_contributions_data()
            )


@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_delete_client_relationship")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_create_client_relationship")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("api_create_client")
def test_add_joint_mortgage_plan_with_valuation_and_deposit(config):
    """ Adding a joint mortgage plan with valuation and deposit. Verifying that the data is saved."""
    test = (AddMortgagePlan(config)
            .open_client_by_url()
            .using_add_plan_wizard()
                .add_mortgage_plan_with_basic_details()
                .add_mortgage_plan_details()
                .finish()
            .verify_second_owner_name()
            .verify_price_valuation_value()
            .verify_equity_deposit_value()
            .verify_if_plan_summary_opened()
            .verify_plan_provider_and_type()
            .verify_if_mortgage_details_section_present())


@pytest.mark.usefixtures("api_delete_plans_contributions")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_add_protection_plan_with_premium_and_life_cover(config):
    """ Test Description: Adding a protection plan with premium and life cover.
    Verifying that the data is saved. """
    test = (AddProtectionPlan(config)
            .open_client_by_url()
            .using_add_plan_wizard()
                .add_protection_plan_basic_details()
                .add_protection_plan_details()
                .finish()
            .verify_if_plan_summary_opened()
            .verify_plan_provider_and_type()
            .verify_premium_amount()
            .verify_premium_frequency()
            .verify_life_cover_sum_assured_value()
            .verify_life_cover_term()
            )


@pytest.mark.usefixtures("api_delete_plans_contributions")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_add_retirement_plan_with_contribution(config):
    """ Adding a retirement plan with a contribution. Verifying that the data is saved. """
    test = (AddRetirementPlan(config)
            .open_client_by_url()
            .using_add_plan_wizard()
                .add_retirement_plan_basic_details(
        get_json_data_for_parameters("common_data")["test_data"]["retirement_plan_data"]["DEFAULT_PLAN_TYPE"])
                .add_retirement_plan_details()
                .finish()
            .verify_if_plan_summary_opened()
            .verify_plan_provider_and_type()
            .verify_current_regular_contribution_value()
            .go_to_contributions()
            .verify_contributions_data()
            )


@pytest.mark.parametrize('plan_type', get_json_data_for_parameters("common_data")["test_data"]["retirement_plan_data"]["PLAN_TYPES"])
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_add_types_of_retirement_plan(config, plan_type):
    """ Test Description: Adding types of retirement plans. Verifying that the data is saved. """
    test = (AddRetirementPlan(config)
            .open_client_by_url()
            .using_add_plan_wizard()
                .add_retirement_plan_basic_details(plan_type)
                .finish()
            .verify_if_plan_summary_opened()
            .verify_plan_provider_and_type()
            )


@pytest.mark.parametrize('plan_type', get_json_data_for_parameters("common_data")["test_data"]["protection_plan_data"]["PLAN_TYPES"])
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_add_types_of_protection_plan(config, plan_type):
    """ Test Description: Adding types of protection plans. Verifying that the data is saved. """
    test = (AddProtectionPlan(config)
            .open_client_by_url()
            .using_add_plan_wizard()
                .add_protection_plan_basic_details(plan_type)
                .finish()
            .verify_if_plan_summary_opened()
            .verify_plan_provider_and_type()
            )


@pytest.mark.scheme
@pytest.mark.usefixtures("api_delete_client_relationship")
@pytest.mark.usefixtures("api_delete_clients_plans")
@pytest.mark.usefixtures("api_create_employee_relationship")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("api_add_client_address")
@pytest.mark.usefixtures("api_create_corporate_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_scheme_to_corporate_relationship(config):
        """ Test Description: Add scheme to corporate client relationship and verify"""
        test = (CompleteSchemes(config)
            .open_client_by_url()
            .using_add_scheme_wizard()
                .add_scheme_basic_details()
                .add_scheme_category_details()
                .finish()
            .change_scheme_status_to_in_force()
            .select_schemes_member()
            .using_add_to_scheme_dialog()
                .add_schemes_member()
                .open_first_schemes()
            .navigate_to_plans_tab()
                .verify_plan_added_in_plan_list()
            )
