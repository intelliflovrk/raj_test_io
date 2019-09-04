import utils
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.quotes.quotes_apps import QuotesAppsPage
from ioffice.clients.quotes.quote_summary import QuoteSummaryPage
from ioffice.clients.quotes.add_plan_dialog import AddPlanDialog
from ioffice.plans.base_summary import BasePlanSummaryPage


class CreatePlanFromQuote:
    def __init__(self, config):
        super().__init__(config)
        self.driver = config.driver
        self.config = config

    def navigate_to_quotes_apps_tab(self):
        ClientDashboardPage(self.config).level3_menu().click_quotes_apps()
        return self

    def verify_plan_created_from_quote(self):
        assert QuotesAppsPage(self.config).get_plan_reference(), "Plan was not created from quote"
        return self

    def open_plan_and_save_details(self):
        QuotesAppsPage(self.config).open_plan()
        plan_ref = BasePlanSummaryPage(self.config).get_plan_ref()
        utils.add_temp_data(self.config, "plan", {"reference": plan_ref})
        plan_id = BasePlanSummaryPage(self.config).get_plan_id()
        utils.update_temp_data(self.config, "plan", 0, "id", plan_id)
        return self

    def create_plan_from_quote(self):
        QuoteSummaryPage(self.config).click_apply_for_first_quote()
        AddPlanDialog(QuoteSummaryPage(self.config))\
            .click_yes_radiobutton()\
            .click_continue()
        utils.switch_to_window_by_name(self, "poster")
        utils.close_current_window(self)
        utils.switch_to_parent_window(self)
        utils.refresh_page(self)
        return self