from dsl.search import SearchClient
from ioffice.clients.base import BaseClientPage
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.add_plan_wizard import AddPlanWizard
from ioffice.plans.protection_plan_summary import ProtectionPlanSummaryPage, BasePlanSummaryPage, BasePlanPage
from datetime import date
from utils import *


class AddProtectionPlan(SearchClient):

    def __init__(self, config):
        super().__init__(config)
        self.wizard = {}
        self.page = {}

    def using_add_plan_wizard(self):
        ClientDashboardPage(self.config).client_actions_menu().hover_over_client_actions().add_plan()
        self.wizard = AddProtectionPlan._PlanWizard(self)
        return self.wizard

    def verify_if_plan_summary_opened(self):
        premium_id = ProtectionPlanSummaryPage(self.config).get_premium_id()
        add_temp_data(self.config, "contribution", {"id": premium_id})
        plan = get_temp_data(self.config, "plan")
        update_temp_data(self.config, "contribution", 0, "plan", {"id": plan["id"]})
        assert ProtectionPlanSummaryPage(self.config).is_title_matches(), "Title not matched"
        return self

    def verify_plan_provider_and_type(self):
        assert BasePlanPage(self.config).get_bar_info() == self.config.plan_provider + " " + self.config.plan_type, \
            "Plan provider and plan type is not matching"
        return self

    def verify_premium_amount(self):
        plan = ProtectionPlanSummaryPage(self.config)
        assert plan.get_premium_amount() == self.wizard.premium_amount
        return self

    def verify_premium_frequency(self):
        plan = ProtectionPlanSummaryPage(self.config)
        assert plan.get_premium_frequency() == self.wizard.premium_frequency
        return self

    def verify_premium_start_date(self):
        plan = ProtectionPlanSummaryPage(self.config)
        assert plan.get_premium_start_date() == self.wizard.premium_start_date
        return self

    def verify_life_cover_sum_assured_value(self):
        plan = ProtectionPlanSummaryPage(self.config)
        assert plan.get_life_cover_sum_assured_value() == self.wizard.life_cover_sum_assured
        return self

    def verify_life_cover_term(self):
        plan = ProtectionPlanSummaryPage(self.config)
        assert plan.get_life_cover_term_value() == self.wizard.life_cover_term
        return self

    def save_plan_id_and_ref(self):
        plan_id = BasePlanPage(self.config).get_plan_id()
        add_temp_data(self.config, "plan", {"id": plan_id})
        plan_ref = BasePlanPage(self.config).get_plan_ref()
        update_temp_data(self.config, "plan", 0, "reference", plan_ref)
        return self

    class _PlanWizard:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddPlanWizard(self.config)
            self.data = get_common_data(self.config)["test_data"]["protection_plan_data"]
            self.life_cover_sum_assured = self.data["protection_plan_details_form"]["LIFE_COVER_SUM_ASSURED"]
            self.life_cover_term = self.data["protection_plan_details_form"]["LIFE_COVER_TERM"]
            self.premium_amount = self.data["protection_plan_details_form"]["PREMIUM_AMOUNT"]
            self.premium_frequency = self.data["protection_plan_details_form"]["PREMIUM_FREQUENCY"]
            self.premium_start_date = date.today().strftime('%d/%m/%Y')
            assert self.wizard.is_title_matches(), "Title does not match the Add Plan Wizard"

        def add_protection_plan_basic_details(self, plan_type="Term Protection"):
            plan = self.wizard.protection_plan_stage()
            plan.goto_stage()
            assert plan.is_current_stage()
            adviser_dialog = plan.open_adviser_search_dialog()
            data = get_common_data(self.config)["test_data"]["protection_plan_data"]
            adviser_dialog.clear_adviser_firstname_field()
            adviser_dialog.fill_in_adviser_firstname_field(data["ADVISER_FIRST_NAME"])
            adviser_dialog.click_search()
            adviser_dialog.click_first_result()
            adviser_dialog.close_io_dialog()
            provider = plan.open_provider_search_dialog()
            provider.select(self.data["PLAN_PROVIDER"])
            provider.click_ok_button()
            provider.close_io_dialog()
            plantype = plan.open_producttype_search_dialog()
            plantype.select(plan_type)
            plantype.click_ok_button()
            plantype.close_io_dialog()
            plan.page.wait_until_please_wait_spinner_present()
            plan.select_advicetype(self.data["ADVICE_TYPE"])
            self.config.plan_provider = self.data["PLAN_PROVIDER"]
            self.config.plan_type = plan_type
            return self

        def add_protection_plan_details(self):
            plan = self.wizard.protection_plan_stage()
            plan.fill_in_life_cover_sum_assured(self.life_cover_sum_assured)\
                .fill_in_life_cover_term(self.life_cover_term)\
                .fill_in_premium_amount(self.premium_amount)\
                .fill_in_premium_start_date(self.premium_start_date)\
                .select_premium_frequency(self.premium_frequency)
            return self

        def finish(self):
            self.wizard.click_finish_button()
            self.journey.save_plan_id_and_ref()
            return self.journey
