import utils
from dsl.add_mortgage_plan import AddMortgagePlan
from dsl.search import SearchPlan, QuickClientSearch
from ioffice.clients.add_client_merge_dialog import MergeClientDialog
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.plans.base import BasePlanPage


class MergeClient(AddMortgagePlan):

    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.wizard = {}

    def using_merge_client_dialog(self):
        clientdashboard = ClientDashboardPage(self.config)
        clientdashboard.client_actions_menu().hover_over_client_actions().merge_client()
        self.dialog = MergeClient._MergeDialog(clientdashboard, self)
        return self.dialog

    def open_existing_merge_client(self):
        QuickClientSearch(self.config).quick_search_client(utils.get_common_data(self.config)["clients"]["merge"]["fullname"])\
            .save_client_id()
        self.config.variables["temp_data"]["client"].reverse()
        return self

    def open_existing_client_plan(self):
        plan = utils.get_temp_data(self.config, "plan")
        SearchPlan(self.config).open_plan(plan["reference"])
        return self

    def verify_created_client_plan_merged(self):
        plan = utils.get_temp_data(self.config, "plan")
        assert BasePlanPage(self.config).get_plan_ref() == plan["reference"],\
             "Merge Client not successfull"
        return self

    class _MergeDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = MergeClientDialog(current_page)

        def search_for_created_client_to_merge(self):
            client = utils.get_temp_data(self.config, "client", 1)
            self.dialog \
                .fill_in_firstname_field(client["person"]["firstName"]) \
                .fill_in_lastname_field(client["person"]["lastName"]) \
                .click_search_button()
            return self

        def merge_created_client_to_existing_client(self):
            self.dialog \
                .click_first_check_box() \
                .click_select_for_merge_button() \
                .click_merge_button() \
                .click_close_button()\
                .close_io_dialog()
            return self.journey
