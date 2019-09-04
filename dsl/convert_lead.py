from dsl.create_lead import CreateLead
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.leads.change_status_dialog import ChangeStatusDialog
from ioffice.leads.lead_details_page import LeadDetailsPage
from utils import get_temp_data, get_common_data


class ConvertLead(CreateLead):

    def using_change_status_dialog(self):
        lead_details_page = LeadDetailsPage(self.config)
        lead_details_page.lead_actions_menu() \
            .hover_over_lead_actions() \
            .change_status()
        return ConvertLead._ChangeStatus(lead_details_page, self)

    def assert_lead_converted_to_client_exists(self):
        lead = get_temp_data(self.config, "lead")
        clientdashboard = ClientDashboardPage(self.config)
        assert clientdashboard.is_title_matches(), "Title does not match the client dashboard"
        assert clientdashboard.get_client_bar_info() == lead["person"]["firstName"] + ' ' + lead["person"]["lastName"]

    class _ChangeStatus:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ChangeStatusDialog(parent_page)

        def convert_lead_to_client(self):
            data = get_common_data(self.config)["test_data"]["lead_data"]
            self.dialog.select_status(data["STATUS"])
            self.dialog.wait_until_please_wait_spinner_present()
            self.dialog.click_save_button()
            self.dialog.close_io_dialog()
            return self.journey