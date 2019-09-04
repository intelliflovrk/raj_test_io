import fakedata
import utils
from ioffice.userdashboard import UserDashboardPage
from ioffice.leads.add_lead_wizard import AddLeadWizard
from ioffice.leads.lead_details_page import LeadDetailsPage
from ioffice.leads.leads_search_page import LeadSearchPage
from ioffice.adviserworkplace import AdviserWorkplacePage


class CreateLead:

    def __init__(self, config):
        self.config = config
        self.wizard = {}

    def navigate_to_lead_page(self):
        UserDashboardPage(self.config).level1_menu()\
            .hover_over_navigation_menu()\
            .click_adviserworkplace()
        AdviserWorkplacePage(self.config).click_leads_tab()
        return self

    def search_and_open_lead(self):
        lead = utils.get_temp_data(self.config, "lead")
        LeadSearchPage(self.config).clear_first_name()\
            .clear_last_name()\
            .fill_in_first_name(lead["person"]["firstName"])\
            .fill_in_last_name(lead["person"]["lastName"])\
            .select_lead_status_by_text("Initial")\
            .click_search_button()\
            .click_open()
        return self

    def using_add_lead_wizard(self):
        dashboard = UserDashboardPage(self.config)
        dashboard.level1_menu().hover_over_navigation_menu().click_adviserworkplace()
        adviserworkplace = AdviserWorkplacePage(self.config)
        adviserworkplace.click_leads_tab()
        leadspage = LeadSearchPage(self.config)
        assert leadspage.is_title_matches(), "Title does not match the lead search page"
        leadspage.click_add_lead()
        wizard = CreateLead._LeadWizard(self, AddLeadWizard(self.config))
        self.wizard = wizard
        return wizard

    def assert_lead_exists(self):
        leaddetails = LeadDetailsPage(self.config)
        assert leaddetails.is_title_matches(), "Title does not match the lead details page"
        assert leaddetails.get_lead_bar_info() == \
               utils.get_temp_data(self.config, "lead")["person"]["firstName"] + ' ' + utils.get_temp_data(self.config, "lead")["person"]["lastName"], "Lead name not matching"
        return self

    class _LeadWizard:
        def __init__(self, journey, wizard):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddLeadWizard(self.config)
            assert self.wizard.is_title_matches(), "Title does not match the Add Lead Wizard"

        def add_basic_lead_details(self):
            utils.add_temp_data(self.config, "lead", {"person": {"firstName": fakedata.rand_firstname(
                self, "first_name"), "lastName": fakedata.rand_lastname(self, "last_name")}})
            basic_details = self.wizard.basic_details_stage()
            basic_details.goto_stage()
            basic_details.page.fill_in_form(utils.get_common_data(self.config)["test_data"]["add_basic_lead_details"], basic_details)
            basic_details.fill_in_first_name_field(utils.get_temp_data(self.config, "lead")["person"]["firstName"])
            basic_details.fill_in_last_name_field(utils.get_temp_data(self.config, "lead")["person"]["lastName"])
            return self

        def finish(self):
            self.wizard.click_finish_button()
            utils.update_temp_data(self.config, "lead", 0, "id", LeadDetailsPage(self.config).get_lead_id())
            return self.journey
