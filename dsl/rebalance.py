from dsl.io_navigation import MyDashboardNavigation
from dsl.plan_actions import PlanActions
from dsl.io_navigation import RebalanceNavigation
from ioffice.adviser_workplace.fund_analysis.rebalance import ViewRebalancePage
from ioffice.adviser_workplace.fund_analysis.rebalance_communication_options_dialog import RebalanceCommunicationOptionsDialog
import utils
import fakedata
from datetime import datetime


class StartRebalanceCommunication(PlanActions):

    def using_rebalance_communication_options_dialog(self):
        MyDashboardNavigation(self.config)\
            .adviser_workplace()\
            .fund_analysis_tab()\
            .rebalance_tab()
        ViewRebalancePage(self.config).click_start_rebalance_communication()
        return StartRebalanceCommunication._RebalanceCommunicationOptionsDialog(self)

    class _RebalanceCommunicationOptionsDialog:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = RebalanceCommunicationOptionsDialog(ViewRebalancePage(self.config))

        def start_rebalance_communication(self):
            rebalance_recommendation_commentary = "Rebalance Recommendation Commentary " + fakedata.rand_text()
            model_update_recommendation_commentary = "Model Update Recommendation Commentary " + fakedata.rand_text()
            no_action_recommendation_commentary = "No Action Recommendation Commentary " + fakedata.rand_text()
            utils.add_temp_data(self.config, "rebalance_recommendation",
                                {"rebalance": {"commentary": rebalance_recommendation_commentary}})
            utils.add_temp_data(self.config, "rebalance_recommendation",
                                {"rebalance": {"commentary": model_update_recommendation_commentary}})
            utils.add_temp_data(self.config, "rebalance_recommendation",
                                {"rebalance": {"commentary": no_action_recommendation_commentary}})
            self.dialog.fill_in_rebalance_recommendation_commentary(rebalance_recommendation_commentary)\
                .fill_in_model_update_recommendation_commentary(model_update_recommendation_commentary)\
                .fill_in_no_action_recommendation_commentary(no_action_recommendation_commentary)
            utils.execute_click_for_all_webelements(self.dialog.get_models_that_apply_checkbox_elements())
            self.dialog.click_model_that_apply(utils.get_temp_data(self.config, "imps_model")["name"])\
                .click_proceed()\
                .close_io_dialog()
            return self.journey


class ViewRebalance:

    def __init__(self, config):
        self.config = config
        self.navigate_to = RebalanceNavigation(self.config)

    def download_rebalance_report(self):
        MyDashboardNavigation(self.config)\
            .adviser_workplace()\
            .fund_analysis_tab()\
            .rebalance_tab()
        ViewRebalancePage(self.config).click_first_report_link()
        return self

    def _get_rebalance_event_report_data(self):
        return utils.read_csv_file(utils.open_downloaded_file(
            self, "Rebalance Event {0}.csv".format(datetime.now().strftime("%d%m%y")), "rt"))

    def _get_recommendation_status_for_client(self, client_name):
        report = self._get_rebalance_event_report_data()
        return set([row[-1] for row in report if client_name in row])

    def verify_recommendation_status_for_clients(self):
        client1_rec = self._get_recommendation_status_for_client(utils.get_temp_data(self.config, 'client')["name"])
        assert 'Accepted' in client1_rec and len(client1_rec) == 1, \
            f"Expected status is Accepted. Observed status is {client1_rec}"
        client2_rec = self._get_recommendation_status_for_client(utils.get_temp_data(self.config, 'client', 1)["name"])
        assert 'New' in client2_rec and len(client2_rec) == 1, \
            f"Expected status is New. Observed status is {client2_rec}"
        return self
