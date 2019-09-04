import pytest
from dsl.create_client_and_plan import CreateClientAndPreExistingPlan

pytestmark = [pytest.mark.client, pytest.mark.plan, pytest.mark.io_all]


@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_client_and_pre_existing_plan(config):
    """ Test Description: Adding a client and a pre-existing plan by using Add Client And Plan Wizard.
        Verifying that the data is saved. """
    test = (CreateClientAndPreExistingPlan(config)
            .using_add_client_and_plan_wizard()
                .add_basic_client_details()
                .add_pre_existing_basic_investment_plan()
                .finish()
            .verify_if_plan_summary_opened()
            .verify_plan_provider_and_type()
            )


@pytest.mark.skip(reason="PRD Defect IP-49917")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_joint_client_and_plan(config):
    """ Test Description: Adding a joint client and plan.
        Verifying that the data is saved. """
    test = (CreateClientAndPreExistingPlan(config)
            .using_add_client_and_plan_wizard()
                .add_basic_client_details()
                .add_partner_details_and_plan()
                .finish()
            .navigate_to_summary_tab()
                .verify_first_life_name()
                .verify_first_life_summary_data()
            .navigate_to_notes_tab()
                .verify_first_life_notes()
            .navigate_to_service_case_page()
                .verify_service_case_data()
            .navigate_to_opportunity_page()
                .verify_opportunity_data()
            .navigate_to_summary_tab()
                .switch_to_second_life()
                .verify_second_life_name()
                .verify_second_life_summary_data()
            .navigate_to_notes_tab()
                .verify_first_life_notes()
            )
