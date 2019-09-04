import utils
from dsl.plan_actions import PlanActions
from dsl.search import SearchClient
from ioffice.add_scheme_member_dialog import AddSchemeMemberDialog
from ioffice.clients.client_plans_list import ClientListPlansPage
from ioffice.plans.base import BasePlanPage
from ioffice.schemes.base import BaseSchemePage
from ioffice.clients.add_scheme_wizard import AddSchemeWizard
from ioffice.clients.client_dashboard import ClientDashboardPage
from utils import *


class CompleteSchemes(SearchClient):

    def using_add_scheme_wizard(self):
        ClientDashboardPage(self.config) \
            .client_actions_menu() \
            .hover_over_client_actions() \
            .add_scheme()
        self.wizard = CompleteSchemes._AddSchemeWizard(self)
        return self.wizard

    def open_first_schemes(self):
        BaseSchemePage(self.config).click_first_open_link()
        return self

    def change_scheme_status_to_in_force(self):
        data = get_common_data(self.config)["test_data"]["change_plan_status_data"]
        PlanActions(self.config).open_change_plan_status_dialog().change_plan_status_to(data["submitted_to_provider"])
        self.open_first_schemes()
        PlanActions(self.config).open_change_plan_status_dialog().change_plan_status_to(data["inforce"])
        return self

    def select_schemes_member(self):
        BaseSchemePage(self.config)\
            .click_first_open_link()\
            .click_members_tab()\
            .select_first_member_check_box()
        return self

    def using_add_to_scheme_dialog(self):
        BaseSchemePage(self.config).click_add_to_scheme()
        return CompleteSchemes._AddSchemeMemberDialog(BaseSchemePage(self.config), self)

    def navigate_to_plans_tab(self):
        ClientDashboardPage(self.config).level3_menu().click_plans()
        return self

    def verify_plan_added_in_plan_list(self):
        ClientListPlansPage(self.config).click_open_first_link()
        plan_id = BasePlanPage(self.config).get_plan_id()
        assert plan_id, "Plan not added successfully"
        return self

    class _AddSchemeWizard:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddSchemeWizard(self.config)

        def add_scheme_basic_details(self):
            data = get_common_data(self.config)["test_data"]["scheme_data"]
            scheme = self.wizard.basic_details_stage()
            scheme.goto_stage()
            scheme.open_adviser_dialog() \
                .clear_adviser_firstname_field() \
                .fill_in_adviser_firstname_field(get_common_data(self.config)["advisers"]["default"]["firstname"]) \
                .click_search() \
                .click_first_result() \
                .close_io_dialog()
            scheme.open_provider_search_dialog() \
                .select(data["PLAN_PROVIDER"]) \
                .click_ok_button() \
                .close_io_dialog()
            scheme.select_scheme_type(data["SCHEME_TYPE"])
            self.wizard.wait_until_please_wait_spinner_present()
            scheme.select_plan_type(data["PLAN_TYPE"])
            self.wizard.wait_until_please_wait_spinner_present()
            scheme.fill_in_scheme_name(data["SCHEME_NAME"])
            return self

        def add_scheme_category_details(self):
            self.wizard \
                .category_details_stage() \
                .goto_stage() \
                .fill_in_category_name(get_common_data(self.config)["test_data"]["scheme_data"]["CATEGORY_NAME"])
            return self

        def finish(self):
            self.wizard.click_finish_button(False)
            self.wizard.wait_until_please_wait_spinner_present()
            return self.journey

    class _AddSchemeMemberDialog:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddSchemeMemberDialog(parent_page)

        def add_schemes_member(self):
            self.dialog.click_save()
            return self.journey

