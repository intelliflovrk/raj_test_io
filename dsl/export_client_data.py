from utils import *
from dsl.create_client import CreateClient
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.factfind.export_client_data import ExportClientDataSection
import time


class ExportClientData(CreateClient):
    def __init__(self, config):
        super().__init__(config)

    def navigate_to_factfind(self):
        ClientDashboardPage(self.config).level3_menu().click_factfind()
        return self

    def click_export_client_data(self):
        ClientDashboardPage(
            self.config).client_actions_menu().hover_over_client_actions().export_client_data()
        return self

    def download_client_data(self):
        ExportClientDataSection(self.config).click_go_button()
        return self

    def verify_client_data_document_downloaded(self):
        time.sleep(30)
        url = get_download_folder(self.config)
        verify_file_is_downloaded(url, "ClientData.dt")
        return self
