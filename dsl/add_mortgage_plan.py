from dsl.create_client import CreateClient
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.add_plan_wizard import AddPlanWizard
from ioffice.plans.mortgage_plan_summary import *
from utils import get_common_data, get_temp_data, add_temp_data, update_temp_data


class AddMortgagePlan(CreateClient):

    def using_add_plan_wizard(self):
        ClientDashboardPage(self.config).client_actions_menu()\
            .hover_over_client_actions()\
            .add_plan()
        self.wizard = AddMortgagePlan._PlanWizard(self)
        return self.wizard

    def verify_if_plan_summary_opened(self):
        plan = MortgagePlanSummaryPage(self.config)
        assert plan.is_title_matches()
        return self

    def verify_plan_provider_and_type(self):
        plan = MortgagePlanSummaryPage(self.config)
        data = get_common_data(self.config)["test_data"]["mortgage_plan_data"]
        assert plan.get_bar_info() == data["PLAN_PROVIDER"] + " " + data["PLAN_TYPE"], "Incorrect plan provider or type"
        return self

    def verify_second_owner_name(self):
        second_client = get_temp_data(self.config, "client", 1)
        assert MortgagePlanSummaryPage(self.config).get_second_owner_name() == second_client["name"], \
            "Incorrect Second owner name."
        return self

    def verify_price_valuation_value(self):
        assert MortgagePlanSummaryPage(self.config).get_price_valuation() == get_common_data(self.config)["test_data"]["mortgage_plan_data"]["price_valuation"]
        return self

    def verify_equity_deposit_value(self):
        assert MortgagePlanSummaryPage(self.config).get_equity_deposit() == get_common_data(self.config)["test_data"]["mortgage_plan_data"]["deposit_equity"]
        return self

    def verify_if_mortgage_details_section_present(self):
        plan = MortgagePlanSummaryPage(self.config)
        assert plan.is_mortgage_details_section_present()
        return self

    class _PlanWizard:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddPlanWizard(self.config)

        def verify_if_mortgage_details_section_present(self):
            plan_stage = self.wizard.mortgage_plan_stage()
            assert plan_stage.is_mortgage_details_section_present()
            return self

        def add_mortgage_plan_with_basic_details(self):
            data = get_common_data(self.config)["test_data"]["mortgage_plan_data"]
            plan = self.wizard.mortgage_plan_stage()
            plan.goto_stage()
            assert plan.is_current_stage()
            adviser_dialog = plan.open_adviser_search_dialog()
            adviser_dialog.clear_adviser_firstname_field()
            adviser_dialog.fill_in_adviser_firstname_field(data["ADVISER_FIRST_NAME"])
            adviser_dialog.click_search()
            adviser_dialog.click_first_result()
            adviser_dialog.close_io_dialog()
            provider = plan.open_provider_search_dialog()
            provider.select(data["PLAN_PROVIDER"])
            provider.click_ok_button()
            provider.close_io_dialog()
            plantype = plan.open_producttype_search_dialog()
            plantype.select(data["PLAN_TYPE"])
            plantype.click_ok_button()
            plantype.close_io_dialog()
            plan.page.wait_until_please_wait_spinner_present()
            plan.select_advicetype(data["ADVICE_TYPE"])
            return self

        def add_mortgage_plan_details(self):
            data = get_common_data(self.config)["test_data"]["mortgage_plan_data"]
            second_client = get_temp_data(self.config, "client", 1)
            self.wizard.mortgage_plan_stage().select_second_owner(second_client["name"])\
                .fill_in_price_valuation(data["price_valuation"])\
                .fill_in_deposit_equity(data["deposit_equity"])
            return self

        def finish(self):
            self.wizard.click_finish_button()
            plan_id = BasePlanPage(self.config).get_plan_id()
            add_temp_data(self.config, "plan", {"id": plan_id})
            plan_ref = BasePlanPage(self.config).get_plan_ref()
            update_temp_data(self.config, "plan", 0, "reference", plan_ref)
            return self.journey
