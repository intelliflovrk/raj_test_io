import datetime
import utils
from dsl.client_document import DocumentProfile
from dsl.fee import Fee
from dsl.search import SearchPlan
from dsl.io_navigation import PlanNavigation
from ioffice.clients.client_dashboard import ClientDashboardPage, BaseClientPage
from ioffice.plans.base import BasePlanPage
from ioffice.plans.documents import PlanDocumentsPage
from ioffice.plans.upload_document_dialog import UploadDocumentDialog
from ioffice.plans.wrap_plan_summary import WrapPlanSummaryPage
from ioffice.plans.change_plan_status_dialog import ChangePlanStatusDialog
from ioffice.plans.activities import PlanActivitiesPage
from ioffice.plans.contributions import PlanContributionsPage
from ioffice.plans.delete_task_options_dialog import DeleteTaskOptionsDialog
from ioffice.plans.add_valuation_dialog import AddValuationDialog
from ioffice.plans.add_fund_dialog import AddFundDialog
from ioffice.plans.withdrawals import PlanWithdrawalsPage
from ioffice.plans.base_funds_holdings import BasePlanFundsHoldingsPage
from ioffice.plans.add_to_wrapper_dialog import AddToWrapperDialog
from ioffice.plans.valuations import PlanValuationsPage
from ioffice.plans.recommendations import PlanRecommendationsTabPage
from ioffice.plans.recommendation_view_dialog import RecommendationViewDialog
from utils import *
from fakedata import rand_text


class PlanActions:
    def __init__(self, config):
        self.config = config
        self.navigate_to = PlanNavigation(self.config)

    def open_plan(self):
        SearchPlan(self.config).open_plan_by_url()
        return self

    def open_change_plan_status_dialog(self):
        page = BasePlanPage(self.config)
        page.plan_actions().hover_over_plan_actions().change_plan_status()
        return PlanActions._ChangePlanStatusDialog(page, self)

    def open_change_sub_plan_status_dialog(self):
        page = BasePlanPage(self.config)
        page.plan_actions().hover_over_plan_actions().change_plan_status()
        return PlanActions._ChangePlanStatusDialog(page, self)

    def open_add_valuation_dialog(self):
        client = get_temp_data(self.config, "client")
        plan = get_temp_data(self.config, "plan")
        plan_page = BasePlanPage(self.config)
        plan_page.plan_actions()\
            .hover_over_plan_actions()\
            .add_valuation()
        return PlanActions._ValuationDialog(client["id"], plan["id"], plan_page, self)

    def delete_valuations(self):
        BasePlanPage(self.config).click_valuations()
        PlanValuationsPage(self.config).check_select_all_valuations()\
            .click_delete()\
            .click_ok_in_browser_confirmation_dialog()
        return self

    def open_add_fund_dialog(self):
        plan_page = BasePlanPage(self.config)
        plan_page.plan_actions()\
            .hover_over_plan_actions()\
            .add_fund()
        return PlanActions._FundDialog(plan_page, self)

    def delete_funds(self):
        BasePlanPage(self.config).click_funds_holdings()
        funds_holdings_page = BasePlanFundsHoldingsPage(self.config)
        funds_holdings_page.check_select_all_funds()\
            .click_delete()\
            .click_ok_in_browser_confirmation_dialog()
        funds_holdings_page.wait_until_please_wait_spinner_present()
        return self

    def delete_plan_tasks(self):
        client = get_temp_data(self.config, "client")
        plan = get_temp_data(self.config, "plan")
        BasePlanPage(self.config).click_activities()
        activitiespage = PlanActivitiesPage(self.config)
        activitiespage.check_select_all_tasks()\
            .click_delete()
        DeleteTaskOptionsDialog(client["id"], plan["id"], activitiespage).click_ok()\
            .wait_until_please_wait_spinner_present()\
            .close_io_dialog()
        return self

    def open_add_fee_from_plan_action(self):
        BasePlanPage(self.config).plan_actions() \
            .hover_over_plan_actions() \
            .add_fee()
        self.dialog = Fee._AddFeeDialog(ClientDashboardPage(self.config), self)
        return self.dialog

    def go_to_contributions(self):
        BasePlanPage(self.config).click_contributions()
        contribution_id = PlanContributionsPage(self.config).get_contribution_id()
        add_temp_data(self.config, "contribution", {"id": contribution_id})
        plan = get_temp_data(self.config, "plan")
        update_temp_data(self.config, "contribution", 0, "plan", {"id": plan["id"]})
        return self

    def verify_contributions_data(self):
        data = get_common_data(self.config)["test_data"]["investment_plan_data"]
        assert PlanContributionsPage(self.config).get_amount() == "£" + data[
            "LUMP_SUM_AMOUNT"], "Lump Sum Amount is not as expected"
        assert PlanContributionsPage(self.config).get_start_date() == datetime.datetime.today().strftime(
            '%d/%m/%Y'), "Start Date is not as matching"
        return self

    def go_to_withdrawals(self):
        BasePlanPage(self.config).click_withdrawals()
        return self

    def create_withdrawals(self):
        PlanWithdrawalsPage(self.config).select_type("Lump Sum")\
            .wait_until_please_wait_spinner_present()\
            .fill_in_amount(get_common_data(self.config)["test_data"]["investment_plan_data"]["LUMP_SUM_AMOUNT"])\
            .fill_in_effective_date(datetime.datetime.today().strftime('%d/%m/%Y'))\
            .click_create().wait_until_please_wait_spinner_present()
        return self

    def verify_withdrawals_data(self):
        withdrawal_id = PlanWithdrawalsPage(self.config).get_withdrawal_id()
        add_temp_data(self.config, "withdrawal", {"id": withdrawal_id})
        plan = get_temp_data(self.config, "plan")
        update_temp_data(self.config, "withdrawal", 0, "plan", {"id": plan["id"]})
        data = get_common_data(self.config)["test_data"]["investment_plan_data"]
        assert PlanWithdrawalsPage(self.config).get_amount() == data["LUMP_SUM_AMOUNT"], \
            "Lump Sum Amount is not as expected"
        assert PlanWithdrawalsPage(self.config).get_effective_date() == datetime.datetime.today().strftime('%d/%m/%Y'), \
            "Start Date is not as matching"
        return self

    def using_add_to_wrapper_dialog(self):
        plan_page = BasePlanPage(self.config)
        plan_page.plan_actions()\
            .hover_over_plan_actions()\
            .add_to_wrapper()
        return PlanActions._AddToWrapperDialog(plan_page, self)

    def using_upload_document_dialog(self):
        plan_page = BasePlanPage(self.config)
        plan_page.plan_actions() \
            .hover_over_plan_actions() \
            .click_upload_document()
        return PlanActions._UploadDocumentDialog(plan_page, self)

    def add_wrap_report_notes(self):
        self.config.plan_report_note = rand_text()
        BasePlanPage(self.config).click_summary()
        WrapPlanSummaryPage(self.config).fill_in_report_notes(self.config.plan_report_note)\
            .click_save()\
            .wait_until_please_wait_spinner_present()
        return self

    def navigate_to_funds_holdings_tab(self):
        BasePlanPage(self.config).click_funds_holdings()
        return PlanFundsHoldings(self.config)

    def open_document_details(self):
        PlanDocumentsPage(self.config).click_first_profile_link()
        return DocumentProfile(self.config)

    def navigate_to_recommendations_tab(self):
        self.navigate_to.more_tabs()\
            .recommendations_tab()
        return PlanRecommendations(self.config)
        
    class _ChangePlanStatusDialog:
        def __init__(self, plan_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ChangePlanStatusDialog(plan_page)
            self.data = get_common_data(self.config)["test_data"]["change_plan_status_data"]

        def change_plan_status_to(self, status):
            self.dialog.select_status(status) \
                .wait_until_please_wait_spinner_present() \
                .click_save() \
                .close_io_dialog()
            return self.journey

        def verify_info_message(self):
            client_fullname = get_temp_data(self.config, "client")["person"]["firstName"] + " " + get_temp_data(self.config, "client")["person"]["lastName"]
            info_message = f"1. {client_fullname} must have valid Address Line 1, City/Town, Postcode (UK only) and Country."
            assert info_message in self.dialog.get_info_message(), \
                "Info message not matching or not present"
            self.dialog.click_close()
            return self

    class _ValuationDialog:
        def __init__(self, client_id, plan_id, plan_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddValuationDialog(client_id, plan_id, plan_page)
            self.journey.valuation_data = get_common_data(self.config)["test_data"]["valuation_data"]

        def add_manual_valuation(self):
            self.dialog.valuation_type_step()\
                .select_manual_valuation_type()\
                .click_next_button()
            self.dialog.manual_valuation_step()\
                .clear_plan_value()\
                .fill_in_plan_value(self.journey.valuation_data["plan_value"])\
                .click_add_button()\
                .close_io_dialog()
            return self.journey

    class _FundDialog:
        def __init__(self, plan_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddFundDialog(plan_page)
            self.journey.fund_data = get_common_data(self.config)["test_data"]["fund_data"]

        def add_fund(self):
            search_fund_dialog = self.dialog.open_fund_search_dialog()
            search_fund_dialog\
                .clear_and_fill_in_fund_name_field(self.journey.fund_data["fund_name"])\
                .click_search()\
                .click_first_result()\
                .close_io_dialog()
            self.dialog.clear_gross_purchase_price()\
                .fill_in_gross_purchase_price(self.journey.fund_data["gross_purchase"])\
                .clear_number_of_units_holdings()\
                .fill_in_number_of_units_holdings(self.journey.fund_data["no_of_units"])\
                .click_save()\
                .close_io_dialog()
            return self.journey

    class _AddToWrapperDialog:
        def __init__(self, plan_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddToWrapperDialog(plan_page)

        def add_plan_to_wrapper(self):
            self.dialog.click_first_radio_button()\
                .click_link_button()\
                .close_io_dialog()
            return self.journey

    class _UploadDocumentDialog:
        def __init__(self, plan_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = UploadDocumentDialog(plan_page)

        def upload_pdf_document(self):
            utils.add_temp_data(self.config, "document", {"category": utils.get_common_data(
                self.config)["test_data"]["document_data"]["document_category"]})
            utils.update_temp_data(self.config, "document", 0, "subcategory", utils.get_common_data(
                self.config)["test_data"]["document_data"]["document_subcategory"])
            data = utils.get_temp_data(self.config, "document")
            self.dialog \
                .click_file_type() \
                .select_document_category(data["category"]) \
                .select_document_subcategory(data['subcategory']) \
                .send_file_url() \
                .click_upload_button()
            return self.journey


class PlanFundsHoldings:
    def __init__(self, config):
        self.config = config
        self.page = BasePlanFundsHoldingsPage(self.config)

    def verify_current_model_portfolio_is(self, model_portfolio_name):
        observed_model_portfolio = self.page.get_current_model_portfolio()
        assert model_portfolio_name == observed_model_portfolio, \
            f"Expected model portfolio is {model_portfolio_name}. Observed model portfolio is {observed_model_portfolio}"
        return self

    def verify_latest_version_available_is(self, model_portfolio_name):
        observed_model_portfolio = self.page.get_latest_version_available()
        assert model_portfolio_name == observed_model_portfolio, \
            f"Expected model portfolio is {model_portfolio_name}. Observed model portfolio is {observed_model_portfolio}"
        return self

    def verify_assigned_model_portfolio_is(self, model_portfolio_name):
        observed_model_portfolio = self.page.get_assigned_model_portfolio()
        assert f"Model Portfolio: {model_portfolio_name}" == observed_model_portfolio, \
            f"Expected model portfolio is {model_portfolio_name}. Observed model portfolio is {observed_model_portfolio}"
        return self

    def verify_funds_in_fund_proposal(self):
        observed_fund_names_list = get_str_list_from_list_of_webelements(self.page.get_fund_proposal_fund_names())
        expected_fund_list = json.loads(get_api_test_data(self.config, "create_basic_imps_model"))["funds"]
        expected_fund_names_list = [fund["name"] for fund in expected_fund_list]
        assert set(observed_fund_names_list) == set(expected_fund_names_list), \
            f"Expected funds are {expected_fund_names_list}. Observed funds are {observed_fund_names_list}"
        return self

    def verify_fund_proposal_updated(self):
        expected_model_portfolio_name = json.loads(get_api_test_data(self.config, "create_basic_imps_model"))["name"]
        self.verify_current_model_portfolio_is(expected_model_portfolio_name)
        self.verify_latest_version_available_is(expected_model_portfolio_name)
        self.verify_assigned_model_portfolio_is(expected_model_portfolio_name)
        self.verify_funds_in_fund_proposal()
        return self


class PlanRecommendations(PlanActions):

    def __init__(self, config):
        super().__init__(config)
        self.page = PlanRecommendationsTabPage(self.config)

    def verify_recommendation_created(self, rec_type):
        recommendations = get_str_list_from_list_of_webelements(self.page.get_recommendations_table_rows())
        assert rec_type in recommendations[0], \
            f"Expected Recommendation Type is {rec_type}. Observed Recommendation Details are {recommendations}"
        return self

    def open_recommendation_details(self):
        self.page.click_details()
        return PlanRecommendations._RecommendationDialog(self.page, self)

    class _RecommendationDialog:

        def __init__(self, plan_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = RecommendationViewDialog(plan_page)

        def verify_rebalance_recommendation_details(self):
            observed_commentary = self.dialog.get_firm_commentary()
            expected_commentary = get_temp_data(self.config, "rebalance_recommendation")["rebalance"]["commentary"]
            assert observed_commentary == expected_commentary, \
                f"Expected Firm Commentary is {expected_commentary}. Observed Firm Commentary is {observed_commentary}."
            self.verify_current_and_target_fund()
            return self

        def verify_current_and_target_fund(self):
            observed_funds_details_list = [fund.split("\n") for fund in get_str_list_from_list_of_webelements(
                self.dialog.get_rebalance_table_rows())]
            observed_target_fund_allocation = [fund[2] for fund in observed_funds_details_list]
            observed_difference = [fund[-1] for fund in observed_funds_details_list]
            expected_target_fund_allocation = [str("%.2f" % fund["allocation"]) for fund in get_temp_data(self.config, "imps_model")["funds"]]
            expected_difference = expected_target_fund_allocation[:]
            expected_target_fund_allocation.insert(0, '0.00')
            expected_difference.insert(0, '100.00')
            assert observed_target_fund_allocation == expected_target_fund_allocation, \
                f"Expected Target Fund Allocation is {expected_target_fund_allocation}. Observed Target Fund Allocation {observed_target_fund_allocation}."
            assert observed_difference == expected_difference, \
                f"Expected Difference is {expected_difference}. Observed Difference {observed_difference}."
            return self

        def close_dialog(self):
            self.dialog.click_close()\
                .close_io_dialog()
            return self.journey
