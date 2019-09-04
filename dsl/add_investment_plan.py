import datetime
from dsl.create_client import CreateClient
from dsl.plan_actions import PlanActions
from dsl.search import SearchPlan
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.add_plan_wizard import AddPlanWizard
from ioffice.clients.client_plans_list import ClientListPlansPage
from ioffice.plans.investment_plan_summary import *
from ioffice.plans.valuations import *
from ioffice.plans.investment_plan_funds_holdings import *
from utils import *


class AddInvestmentPlan(CreateClient, PlanActions, SearchPlan):
    def __init__(self, config):
        super().__init__(config)

    def using_add_plan_wizard(self):
        ClientDashboardPage(self.config).level3_menu().click_plans()
        ClientListPlansPage(self.config).client_actions_menu()\
            .hover_over_client_actions()\
            .add_plan()
        self.wizard = AddInvestmentPlan._PlanWizard(self)
        return self.wizard

    def save_plan_id_and_ref(self):
        plan_id = BasePlanPage(self.config).get_plan_id()
        add_temp_data(self.config, "plan", {"id": plan_id})
        plan_ref = BasePlanPage(self.config).get_plan_ref()
        update_temp_data(self.config, "plan", 0, "reference", plan_ref)
        return self

    def verify_if_plan_summary_opened(self):
        assert InvestmentPlanSummaryPage(self.config).is_title_matches(), \
            "Title does not match the Plan Summary Page title."
        return self

    def verify_plan_provider_and_type(self):
        data = get_common_data(self.config)["test_data"]["investment_plan_data"]
        assert InvestmentPlanSummaryPage(self.config).get_bar_info() == data["PLAN_PROVIDER"] + " " + data["PLAN_TYPE"]\
            ,"Plan Provider and Plan Type do not match the expected values."
        return self

    def verify_current_regular_contribution_value(self):
        assert InvestmentPlanSummaryPage(self.config).get_current_regular_contribution_value() == "£" \
               + get_common_data(self.config)["test_data"]["investment_plan_data"]["REGULAR_CONTRIBUTION_AMOUNT"], \
            "Regular Contribution Amount is not as expected"
        return self

    def verify_total_lumpsum_value(self):
        data = get_common_data(self.config)["test_data"]["investment_plan_data"]
        assert InvestmentPlanSummaryPage(self.config).get_total_lumpsum_value() == "£" \
               + data["LUMP_SUM_AMOUNT"],\
            "Lump Sum Amount is not as expected"
        return self

    def verify_plan_value(self):
        data = get_common_data(self.config)["test_data"]["valuation_data"]
        valuation = PlanValuationsPage(self.config)
        valuation.is_title_matches()
        assert valuation.get_valuation_value() == "£" + data["plan_value"]
        return self

    def show_all_holdings(self):
        InvestmentsPlanFundsHoldingsPage(self.config).click_pick_holdings_filter().click_all_holdings()
        return self

    def verify_number_of_units_holdings_value(self):
        data = get_common_data(self.config)["test_data"]["fund_data"]
        fundsholdings = InvestmentsPlanFundsHoldingsPage(self.config)
        fundsholdings.is_title_matches()
        unitsholdingsnumber = fundsholdings.get_units_holdings_value()
        assert unitsholdingsnumber == data["no_of_units"], \
        f"Units/Holdings number is incorrect: expected value {data['no_of_units']} actual value {unitsholdingsnumber}"
        return self

    class _PlanWizard:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddPlanWizard(self.config)

        def add_investment_plan_basic_details(self):
            data = get_common_data(self.config)["test_data"]["investment_plan_data"]
            plan = self.wizard.investment_plan_stage()
            plan.goto_stage()
            adviser_dialog = plan.open_adviser_search_dialog()
            adviser_dialog.clear_adviser_firstname_field()\
                .fill_in_adviser_firstname_field(data["ADVISER_FIRST_NAME"])\
                .click_search()\
                .click_first_result()\
                .close_io_dialog()
            provider_dialog = plan.open_provider_search_dialog()
            provider_dialog.select(data["PLAN_PROVIDER"])\
                .click_ok_button()\
                .close_io_dialog()
            plantype_dialog = plan.open_producttype_search_dialog()
            plantype_dialog.select(data["PLAN_TYPE"])\
                .click_ok_button()\
                .close_io_dialog()
            plan.page.wait_until_please_wait_spinner_present()
            plan.select_advicetype(data["ADVICE_TYPE"])
            return self

        def add_investment_plan_details(self):
            self.wizard.investment_plan_stage().fill_in_lump_sum_amount(
                get_common_data(self.config)["test_data"]["investment_plan_data"]["LUMP_SUM_AMOUNT"])
            self.wizard.investment_plan_stage().fill_in_effective_date(
                datetime.datetime.today().strftime('%d/%m/%Y'))
            return self

        def finish(self):
            self.wizard.click_finish_button()
            self.journey.save_plan_id_and_ref()
            return self.journey
