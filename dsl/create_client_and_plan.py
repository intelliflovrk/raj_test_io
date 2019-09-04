from dsl.create_client import CreateClient
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.base import BaseClientPage
from ioffice.clients.details.notes import Notes
from ioffice.clients.details.summary import BaseDetailsPage, ViewSummaryPage
from ioffice.clients.opportunities.opportunities import OpportunitiesPage
from ioffice.clients.service_case.service_cases import ServiceCasePage
from ioffice.userdashboard import UserDashboardPage
from ioffice.add_client_and_plan_wizard import AddClientAndPlanWizard
from ioffice.plans.base_summary import *
from fakedata import *
from datetime import date
from utils import *


class CreateClientAndPreExistingPlan(CreateClient):

    def using_add_client_and_plan_wizard(self):
        dashboard = UserDashboardPage(self.config)
        dashboard.click_add_client_and_plan()
        self.wizard = CreateClientAndPreExistingPlan._ClientAndPlanWizard(self)
        return self.wizard

    def navigate_to_summary_tab(self):
        ClientDashboardPage(self.config).level3_menu().click_details()
        BaseDetailsPage(self.config).details_navigation_menu().click_summary_tab()
        return self

    def verify_first_life_name(self):
        assert ClientDashboardPage(self.config).get_client_bar_info() == \
               self.wizard.firstname + ' ' + self.wizard.lastname, "First life name not matching"
        return self

    def verify_first_life_summary_data(self):
        assert ViewSummaryPage(self.config).get_client_relationship_status() == \
               get_common_data(self.config)["basic_data"]["relationship_status"], "Relationship not matching"
        assert get_common_data(self.config)["basic_data"]["basic_address"]["BASIC_POST_CODE"] in ViewSummaryPage(
            self.config).get_city_or_town_and_postcode(), "Postcode is not matching"
        assert ViewSummaryPage(self.config).get_mobile_number() == get_common_data(
            self.config)["basic_data"]["basic_contact"]["BASIC_MOBILE_NUMBER"], "Mobile number not matching"
        assert ViewSummaryPage(self.config).get_campaign_type() == get_common_data(
            self.config)["basic_data"]["basic_campaign_type"], "Campaign Type is not matching"
        assert ViewSummaryPage(self.config).get_service_status() == get_common_data(
            self.config)["basic_data"]["basic_service_status"], "Service status not matching"
        assert ViewSummaryPage(self.config).get_fee_model() == get_common_data(
            self.config)["basic_data"]["basic_fee_model"], "Fee model is not matching"
        return self

    def navigate_to_notes_tab(self):
        ClientDashboardPage(self.config).level3_menu().click_details()
        BaseDetailsPage(self.config).details_navigation_menu().click_notes_tab()
        return self

    def verify_first_life_notes(self):
        assert Notes(self.config).get_notes() == self.config.random_text, "Notes not matching"
        return self

    def navigate_to_service_case_page(self):
        ClientDashboardPage(self.config).level3_menu().click_service_case()
        return self

    def verify_service_case_data(self):
        assert ServiceCasePage(self.config).get_service_case_name() == get_common_data(
            self.config)["basic_data"]["basic_service_case"], "Service case not matching"
        return self

    def navigate_to_opportunity_page(self):
        ClientDashboardPage(self.config).level3_menu().click_opportunities()
        return self

    def verify_opportunity_data(self):
        assert OpportunitiesPage(self.config).get_opportunity_type() == get_common_data(self.config)["basic_data"][
            "basic_opportunity_type"], "Opportunity type not matching"
        return self

    def switch_to_second_life(self):
        ViewSummaryPage(self.config).click_second_life()
        return self

    def verify_second_life_name(self):
        assert ClientDashboardPage(self.config).get_client_bar_info() == self.config.second_life_firstname + " " + \
               self.config.second_life_lastname, "Second life name not matching"
        return self

    def verify_second_life_summary_data(self):
        self.verify_first_life_summary_data()
        return self

    def verify_if_plan_summary_opened(self):
        assert BasePlanSummaryPage(self.config).is_title_matches(), "Plan Summary Page title is not matching"
        return self

    def verify_plan_provider_and_type(self):
        assert BasePlanSummaryPage(
            self.config).get_bar_info() == self.wizard.plan_provider + " " + self.wizard.plan_type,\
            "Plan Provider and Type is not matching"
        return self

    def save_plan_id_and_ref(self):
        plan_id = BasePlanPage(self.config).get_plan_id()
        add_temp_data(self.config, "plan", {"id": plan_id})
        plan_ref = BasePlanPage(self.config).get_plan_ref()
        update_temp_data(self.config, "plan", 0, "reference", plan_ref)
        return self

    def save_client_id(self):
        client_id = BaseClientPage(self.config).get_client_id()
        add_temp_data(self.config, "client", {"id": client_id})
        return self

    class _ClientAndPlanWizard:

        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddClientAndPlanWizard(self.config)
            self.plan_provider = utils.get_common_data(self.config)["test_data"]["plan_provider"]
            self.plan_type = utils.get_common_data(self.config)["test_data"]["plan_type"]
            self.firstname = rand_firstname(self, "first_name")
            self.lastname = rand_lastname(self, "last_name")

        def add_basic_client_details(self):
            self.wizard.basic_details_stage() \
                .goto_stage() \
                .fill_in_form(get_common_data(self.config)["test_data"]["add_basic_client_details"], self.wizard.basic_details_stage()) \
                .fill_in_firstname_field(self.firstname)\
                .fill_in_lastname_field(self.lastname)\
                .open_adviser_dialog() \
                .clear_adviser_firstname_field() \
                .fill_in_adviser_firstname_field(utils.get_common_data(self.config)["advisers"]["default"]["firstname"]) \
                .click_search() \
                .click_first_result() \
                .close_io_dialog()
            return self

        def add_partner_details_and_plan(self):
            self.add_basic_client_partner_details()\
                .add_address_to_both_life()\
                .add_contact_to_both_life()\
                .add_opportunity_to_both_life()\
                .add_dpa_to_both_life()\
                .add_marketing_preferences()\
                .add_notes()\
                .add_pre_existing_basic_investment_plan()
            return self

        def add_basic_client_partner_details(self):
            self.config.second_life_firstname = rand_firstname(self, "first_name")
            self.config.second_life_lastname = rand_lastname(self, "last_name")
            self.wizard.basic_details_stage()\
                .select_joint_client_application()\
                .fill_in_second_life_firstname(self.config.second_life_firstname)\
                .fill_in_second_life_lastname(self.config.second_life_lastname)
            return self

        def add_address_to_both_life(self):
            self.wizard.address_stage()\
                .goto_stage()\
                .fill_in_form(utils.get_common_data(self.config)["basic_data"]["basic_address"], self.wizard.address_stage())
            assert self.wizard.address_stage().get_address_detail_same_for_joint_applicant_check_box_state(), \
                "Check box not ticked"
            return self

        def add_contact_to_both_life(self):
            self.wizard.contact_stage().goto_stage()\
                .fill_in_form(
                 utils.get_common_data(self.config)["basic_data"]["basic_contact"], self.wizard.contact_stage())\
                .click_copy_contacts()\
                .select_campaign_type_first_life("Advertisement")\
                .select_campaign_type_second_life("Advertisement")
            return self

        def add_opportunity_to_both_life(self):
            self.config.service_case_ref = fakedata.rand_text(6)
            self.wizard.opportunity_stage().goto_stage().select_by_visible_text_opportunity(
                 get_common_data(self.config)["basic_data"]["basic_opportunity_type"])\
                .select_service_status_first_life("Test Automation Service Status")\
                .page.wait_until_please_wait_spinner_present()
            self.wizard.opportunity_stage().select_service_status_second_life("Test Automation Service Status")\
                .page.wait_until_please_wait_spinner_present()
            self.wizard.opportunity_stage().select_fee_model_first_life("Test Automation Fee Model")\
                .select_fee_model_second_life("Test Automation Fee Model")\
                .add_service_case_name("Test Automation Service Case")\
                .add_service_case_ref(self.config.service_case_ref)
            return self

        def add_dpa_to_both_life(self):
            self.wizard.dpa_stage()\
                .goto_stage()\
                .tick_all_agreement_statements()\
                .fill_in_agreement_date_field(date.today().strftime('%d/%m/%Y'))\
                .tick_all_agreement_statements_second_life()\
                .fill_in_agreement_date_field_second_life(date.today().strftime('%d/%m/%Y'))
            return self

        def add_marketing_preferences(self):
            self.wizard.marketing_stage()\
                .goto_stage()\
                .fill_in_consent_date_field(date.today().strftime('%d/%m/%Y'))
            return self

        def add_notes(self):
            self.config.random_text = rand_text()
            self.wizard.notes_stage()\
                .goto_stage()\
                .fill_in_notes(self.config.random_text)
            return self

        def add_pre_existing_basic_investment_plan(self):
            plan = self.wizard.plan_stage()
            plan.goto_stage().tick_is_preexisting_plan_checkbox()
            plan.page.wait_until_please_wait_spinner_present()
            plan.open_adviser_search_dialog()\
                .clear_adviser_firstname_field()\
                .fill_in_adviser_firstname_field(utils.get_common_data(self.config)["advisers"]["default"]["firstname"])\
                .click_search()\
                .click_first_result()\
                .close_io_dialog()
            plan.open_provider_search_dialog()\
                .select(self.plan_provider)\
                .click_ok_button()\
                .close_io_dialog()
            plan.open_producttype_search_dialog()\
                .select(self.plan_type)\
                .click_ok_button()\
                .close_io_dialog()
            return self

        def finish(self):
            self.wizard.click_finish_button()
            self.journey.save_plan_id_and_ref()
            self.journey.save_client_id()
            return self.journey
