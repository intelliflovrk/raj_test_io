import pytest
from dsl.complete_factfind import CompleteFactFind
from dsl.set_up_needs_and_priorities_questions import SetupNeedsAndPrioritiesQuestions

pytestmark = [pytest.mark.factfind, pytest.mark.io_all]


@pytest.mark.factfind_pdf
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_basic_factfind(config):
    """ Test Description: Completing a basic factfind for a client """
    test = (CompleteFactFind(config)
                .open_client_by_url()
                .go_to_fact_find()
                     .add_profile_details()
                     .add_employment_details()
                     .add_assets_liability_details()
                     .add_budget_income_and_expenditure_details()
                     .add_summary_details()
                     .finish()
                .using_view_pdfs_dialog()
                     .add_document()
                     .close_dialog()
                .using_documents_section()
                     .verify_saved_documents()
                .navigate_to_dashboard_tab()
                .go_to_fact_find()
                    .navigate_to_budget()
                        .verify_budget_affordability_calculations()
            )


@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_estate_planning_factfind(config):
    """ Test Description: Completing factfind with filling up Estate Planning forms and verify its data """
    test = (CompleteFactFind(config)
            .open_client_by_url()
            .go_to_fact_find()
            .navigate_to_estate_planning_tab()
                .add_estate_planning_details()
            .verify_estate_planning_forms()
            )


@pytest.mark.factfind_pdf
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("file_delete_fact_find_pdf")
@pytest.mark.usefixtures("ui_remove_factfind_partner")
@pytest.mark.usefixtures("api_delete_client_relationship")
@pytest.mark.usefixtures("api_create_client_relationship")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_joint_fact_find_adding_partner(config):
    """ Test Description: Adding partner to factfind"""
    test = (CompleteFactFind(config)
                .open_client_by_url()
                .go_to_fact_find()
                .using_add_remove_partner_wizard()
                    .add_partner()
                .verify_client_and_partner_present_on_client_bar()
                .navigate_to_profile_personal_sub_tab()
                .verify_second_life_present_on_personal_tab()
                .navigate_to_employment_tab()
                .verify_second_life_present_on_employment_tab()
                .using_view_pdfs_dialog()
                    .add_document()
                    .download_the_pdf()
                    .close_dialog()
                .verify_pdf_contains_first_life_records()
            )


@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_mortgage_factfind(config):
    """ Test Description: Completing a mortgage-based factfind for a client and verifying an opportunity"""
    test = (CompleteFactFind(config)
                .open_client_by_url()
                .go_to_fact_find()
                     .navigate_to_mortgage()
                     .add_mortgage_details()
                .using_opportunities_section()
                     .verify_saved_opportunity()
            )


@pytest.mark.usefixtures("ui_delete_needs_priorities_question")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_adding_needs_and_priorities_questions(config):
    """ Test Description:
    Adding a a Needs & Priorities question and verifying that the question appears in factfind. """
    test = (SetupNeedsAndPrioritiesQuestions(config)
            .open_client_by_url()
            .navigate_to_needs_questions()
            .add_needs_question()
                .fill_needs_question_form()
            .open_client_by_url()
            .go_to_fact_find()
                .navigate_to_needs_and_priorities_tab()
            .verify_saved_needs_question_is_present()
            )


@pytest.mark.factfind_pdf
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("file_delete_fact_find_pdf")
@pytest.mark.usefixtures("ui_delete_needs_priorities_answer")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_answering_needs_and_priorities_questions(config):
    """ Test Description: Populating an answer and generating a PDF. """
    test = (SetupNeedsAndPrioritiesQuestions(config)
            .open_client_by_url()
            .go_to_fact_find()
                .navigate_to_needs_and_priorities_tab()
                .fill_need_and_priorities_details()
            .using_view_pdfs_dialog()
                .add_document()
                .download_the_pdf()
                .close_dialog()
            .verify_factfind_documents_downloaded()
            )


@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_protection_factfind_with_provision(config):
    """Test Description: Adds existing provision contracts"""
    test = (
        CompleteFactFind(config)
            .open_client_by_url()
            .go_to_fact_find()
            .navigate_to_existing_protection_provision_tab()
            .add_term_protection_plan()
            .add_income_protection_plan()
            .add_whole_of_life_plan()
            .add_family_income_benefit_plan()
            .verify_contracts_added()
            .verify_summary_screen()

    )


@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_protection_factfind_for_life_and_critical_illness_income_buildings_and_contents(config):
    """Test Description: Fills in Life Critical, Income Protection, Buildings Contents forms, saves it"""
    test = (
        CompleteFactFind(config)
            .open_client_by_url()
            .go_to_fact_find()
            .navigate_to_protection_tab()
            .add_life_critical_illness()
            .verify_life_critical_form()
            .add_income_protection()
            .verify_income_protection_form()
            .add_buildings_contents()
            .verify_buildings_contents_form_was_saved()
    )


@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_retirement_factfind(config):
    """ Test Description: Completing factfind with retirement data"""
    test = (CompleteFactFind(config)
            .open_client_by_url()
            .go_to_fact_find()
            .navigate_to_retirement_tab()
            .add_retirement_details()
            .verify_retirement_goals_added()
            )


@pytest.mark.usefixtures("ui_delete_risk_tolerance_data")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_risk_tolerance(config):
    """ Test Description: Preset risk tolerance and Verify risk warning messages in fact find risk"""
    test = (CompleteFactFind(config)
            .open_client_by_url()
            .go_to_fact_find()
                .navigate_to_risk_tab()
                    .fill_in_risk_question_category()
                    .verify_risk_warning_message()
                    .save_generated_risk_profile()
                    .verify_save_button_disabled()
                    .fill_in_risk_notes_and_save()
                    .verify_risk_notes_saved()
                .navigate_to_risk_replay_tab()
                    .verify_generated_risk_profile()
                    .click_risk_profile_radio_button_no()
                    .verify_chosen_risk_profile_presence()
                    .verify_save_button_disabled()
                    .fill_in_risk_replay_notes_and_save()
                    .verify_risk_replay_notes_saved()
            )
