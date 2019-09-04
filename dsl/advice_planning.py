from dsl.search import SearchClient
from dsl.plan_actions import PlanActions
from ioffice.clients.advice.view_planning_opportunities import ViewPlanningOpportunitiesPage, BaseClientPage
from ioffice.clients.advice.service_case import ServiceCaseBasePage
from ioffice.clients.advice.view_recommendations import ViewRecommendationsPage
from ioffice.clients.advice.research_tools import ResearchToolsPage
from ioffice.clients.quotes.get_quote_for_client import GetNewQuoteDialog
from ioffice.clients.advice.add_manual_recommendation_dialog import AddManualRecommendationDialog
from ioffice.clients.advice.add_fund_dialog import AddFundDialog
from ioffice.clients.advice.recommendation_transaction_details_dialog import RecommendationTransactionDetailsDialog
from ioffice.clients.advice.delete_recommendations_dialog import DeleteRecommendationsDialog
from ioffice.clients.advice.update_plan_dialog import UpdatePlanDialog
import utils
import json
import fakedata


class PlanningOpportunities(SearchClient):

    def using_planning_opportunities(self):
        BaseClientPage(self.config)\
            .level3_menu()\
            .click_advice()
        ViewPlanningOpportunitiesPage(self.config)\
            .fill_in_sequential_ref(utils.get_temp_data(self.config, "opportunity")["reference"])\
            .click_filter()\
            .wait_until_please_wait_spinner_present()\
            .click_first_enter_planning_button()\
            .wait_until_please_wait_spinner_present()
        return PlanningOpportunities._AdvicePlanning(self)

    class _AdvicePlanning:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey

        def open_research_tools(self):
            ServiceCaseBasePage(self.config)\
                .planning_tabs\
                .click_fact_find()\
                .click_research_tools()
            return PlanningOpportunities._AdvicePlanning._ResearchTools(self)

        def open_recommendations(self):
            ServiceCaseBasePage(self.config)\
                .planning_tabs\
                .click_fact_find()\
                .click_recommendations()
            return PlanningOpportunities._AdvicePlanning._Recommendations(self)

        class _ResearchTools:
            def __init__(self, journey):
                self.config = journey.config
                self.journey = journey
                self.page = ResearchToolsPage(self.config)

            def open_get_new_quote_wizard_using_get_quote_tool(self):
                self.page.click_get_new_quote()
                return PlanningOpportunities._AdvicePlanning._ResearchTools._GetNewQuote(self.journey)

            class _GetNewQuote:
                def __init__(self, journey):
                    self.config = journey.config
                    self.journey = journey
                    self.dialog = GetNewQuoteDialog(ResearchToolsPage(self.config))

                def select_product_area(self, product_area):
                    self.dialog.click_product_area(product_area)\
                        .wait_until_please_wait_spinner_present()
                    return self

                def verify_quote_portal_present(self, portal_name):
                    portals = self.dialog.get_portals()
                    portal_list = []
                    for portal in portals:
                        portal_list.append(portal.text)
                    assert portal_name in portal_list, f"{portal_name} not found. Existing portals are {portal_list}"
                    return self

                def close_get_new_quote_wizard(self):
                    self.dialog.click_cancel()\
                        .close_dialog()
                    return self.journey

        class _Recommendations:
            def __init__(self, journey):
                self.config = journey.config
                self.journey = journey
                self.page = ViewRecommendationsPage(self.config)

            def using_add_manual_rec_dialog(self):
                self.page.hover_over_recommendations_actions()\
                    .click_add_manual_rec()
                return PlanningOpportunities._AdvicePlanning._AddManualRec(self.page, self.journey)

            def open_transaction_details(self):
                self.page.click_first_transaction_details_button()
                return PlanningOpportunities._AdvicePlanning._RecommendationTransactionDetails(self.page, self.journey)

            def using_delete_recommendations_dialog(self):
                self.page.hover_over_recommendations_actions()\
                    .click_delete_recommendations()
                return PlanningOpportunities._AdvicePlanning._DeleteRecommendations(self.page, self.journey)

            def accept_manual_recommendation(self):
                self.page.click_first_select_radio_button()\
                    .click_first_accept_button()
                UpdatePlanDialog(self.page).click_update()\
                    .close_dialog()
                return self

            def open_plan(self):
                self.page.click_first_sequential_ref_link()
                return PlanActions(self.config)

        class _AddManualRec:
            def __init__(self, parent_page, journey):
                self.config = journey.config
                self.journey = journey
                self.dialog = AddManualRecommendationDialog(parent_page)

            def add_switch_recommendation_details(self):
                rec_name = fakedata.rand_intsuffix('Automation Test Recommendation ')
                utils.add_temp_data(self.config, "recommendation", {"name": rec_name})
                self.dialog.wait_until_please_wait_spinner_present()\
                    .fill_in_recommendation_name(rec_name)\
                    .select_existing_plan(str(utils.get_temp_data(self.config, "plan")["id"]))\
                    .wait_until_please_wait_spinner_present()
                return self

            def add_model_portfolio(self, model_portfolio_name):
                self.using_add_fund_dialog()\
                    .select_model_portfolio(model_portfolio_name)
                return self

            def save_recommendation(self):
                self.dialog.click_save()\
                    .wait_until_please_wait_spinner_present()\
                    .close_dialog()
                return PlanningOpportunities._AdvicePlanning._Recommendations(self.journey)

            def using_add_fund_dialog(self):
                self.dialog.click_model_portfolio()\
                    .wait_until_please_wait_spinner_present()\
                    .click_add()
                return PlanningOpportunities._AdvicePlanning._AddFundDialog(self.dialog, self.journey)

        class _AddFundDialog:
            def __init__(self, current_dialog, journey):
                self.config = journey.config
                self.journey = journey
                self.dialog = AddFundDialog(current_dialog.page, current_dialog.frame_locator)

            def select_model_portfolio(self, model_portfolio_name):
                self.dialog.select_model_portfolio(model_portfolio_name)\
                    .click_return_chosen_funds()\
                    .close_dialog()\
                    .wait_until_please_wait_spinner_present()
                return self.journey

        class _RecommendationTransactionDetails:
            def __init__(self, parent_page, journey):
                self.config = journey.config
                self.journey = journey
                self.dialog = RecommendationTransactionDetailsDialog(parent_page)

            def verify_existing_and_new_funds_present(self):
                current_fund_names_list = utils.get_str_list_from_list_of_webelements(self.dialog.get_funds_names())
                expected_fund_list = json.loads(utils.get_api_test_data(self.config, "create_basic_imps_model"))["funds"]
                expected_fund_list.append(utils.get_temp_data(self.config, "fund_holding")["fund"])
                expected_fund_names_list = [fund["name"] for fund in expected_fund_list]
                assert set(current_fund_names_list) == set(expected_fund_names_list), \
                    f"Expected funds are {expected_fund_names_list}. Observed funds are {current_fund_names_list}"
                return self

            def close_dialog(self):
                self.dialog.click_close()\
                    .close_dialog()
                return self.journey

        class _DeleteRecommendations:
            def __init__(self, parent_page, journey):
                self.config = journey.config
                self.journey = journey
                self.dialog = DeleteRecommendationsDialog(parent_page)

            def delete_all_recommendations(self):
                self.dialog.tick_select_all().click_delete()
                utils.switch_and_accept_alert(self.dialog)
                self.dialog.close_dialog()
                return self.journey
