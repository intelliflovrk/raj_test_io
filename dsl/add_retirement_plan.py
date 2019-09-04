import datetime
from dsl.client_relationship import AddRelationship
from dsl.plan_actions import PlanActions
from ioffice.clients.client_dashboard import ClientDashboardPage
from dsl.search import SearchClient, SearchPlan
from ioffice.clients.add_plan_wizard import AddPlanWizard
from ioffice.plans.retirement_plan_summary import *
from ioffice.plans.add_sub_plan_wizard import *
from ioffice.plans.sub_plans import *
from utils import *


class AddRetirementPlan(AddRelationship, SearchClient, PlanActions, SearchPlan):

    def __init__(self, config):
        super().__init__(config)
        self.plan_wizard = {}

    def using_add_plan_wizard(self):
        ClientDashboardPage(self.config) \
            .client_actions_menu() \
            .hover_over_client_actions() \
            .add_plan()
        self.plan_wizard = AddRetirementPlan._PlanWizard(self)
        return self.plan_wizard

    def verify_if_plan_summary_opened(self):
        assert RetirementPlanSummaryPage(self.config).is_title_matches(), "Plan Summary Page Title is not matching"
        return self

    def verify_plan_provider_and_type(self):
        data = get_common_data(self.config)["test_data"]["retirement_plan_data"]
        assert RetirementPlanSummaryPage(self.config).get_bar_info() == data["PLAN_PROVIDER"] + " " + \
            self.plan_wizard.plan_type, "Plan Provider and Plan Type is not matching "
        return self

    def verify_current_regular_contribution_value(self):
        assert RetirementPlanSummaryPage(self.config).get_current_regular_contribution_value() == get_common_data(self.config)["test_data"]["retirement_plan_data"][
            "REGULAR_CONTRIBUTION_AMOUNT"], "Regular Contribution Amount is not as expected"
        return self

    def using_add_sub_plan_wizard(self):
        RetirementPlanSummaryPage(self.config) \
            .plan_actions() \
            .hover_over_plan_actions() \
            .add_sub_plan()
        return AddRetirementPlan._AddSubPlanWizard(self)

    def verify_if_sub_plan_added(self):
        assert PlanSubPlanPage(self.config).get_plan_type_value() == get_common_data(self.config)["test_data"]["retirement_plan_data"][
            "SUB_PLAN_TYPE"], "Plan type value not matched"
        self.save_sub_plan_id()
        return self

    def save_sub_plan_id(self):
        PlanSubPlanPage(self.config).click_open_sub_plan()
        self.config.sub_plan_id = BasePlanSummaryPage(self.config).get_plan_id()
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

        def add_retirement_plan_basic_details(self, plan_type):
            data = get_common_data(self.config)["test_data"]["retirement_plan_data"]
            plan = self.wizard.retirement_plan_stage()
            plan.goto_stage()
            plan.open_adviser_search_dialog() \
                .clear_adviser_firstname_field() \
                .fill_in_adviser_firstname_field(data["ADVISER_FIRST_NAME"]) \
                .click_search() \
                .click_first_result() \
                .close_io_dialog()
            plan.open_provider_search_dialog() \
                .select(data["PLAN_PROVIDER"]) \
                .click_ok_button() \
                .close_io_dialog()
            plan.open_producttype_search_dialog() \
                .select(plan_type) \
                .click_ok_button() \
                .close_io_dialog()
            self.plan_type = plan_type
            plan.page.wait_until_please_wait_spinner_present()
            plan.select_advicetype(data["ADVICE_TYPE"])
            return self

        def add_retirement_plan_details(self):
            self.wizard.retirement_plan_stage() \
                .fill_in_lump_sum(get_common_data(self.config)["test_data"]["retirement_plan_data"]["LUMP_SUM_AMOUNT"])\
                .fill_in_effective_date(datetime.datetime.today().strftime('%d/%m/%Y'))
            return self

        def finish(self):
            self.wizard.click_finish_button()
            self.journey.save_plan_id_and_ref()
            return self.journey

    class _AddSubPlanWizard:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddSubPlanWizard(self.config)
            assert self.wizard.is_title_matches(), "Title does not match the Add Sub Plan Wizard"

        def add_sub_plan_basic_details(self):
            plan = self.wizard.plan_stage()
            plan.goto_stage()
            plan.open_adviser_search_dialog() \
                .clear_adviser_firstname_field() \
                .fill_in_adviser_firstname_field(get_common_data(self.config)["test_data"]["retirement_plan_data"]["ADVISER_FIRST_NAME"]) \
                .click_search() \
                .click_first_result() \
                .close_io_dialog()
            plan.open_producttype_search_dialog() \
                .select(get_common_data(self.config)["test_data"]["retirement_plan_data"]["SUB_PLAN_TYPE"]) \
                .click_ok_button() \
                .close_io_dialog()
            plan.page.wait_until_please_wait_spinner_present()
            plan.select_advicetype(get_common_data(self.config)["test_data"]["retirement_plan_data"]["SUB_PLAN_ADVICE_TYPE"])
            return self

        def finish(self):
            self.wizard.click_finish_button()
            return self.journey
