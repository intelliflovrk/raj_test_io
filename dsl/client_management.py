from dsl.create_client import CreateClient
from ioffice.clients.base import BaseClientPage
from ioffice.clients.client_restrict_processing import ClientRestrictProcessing
from ioffice.client_search import ClientSearch
from ioffice.userdashboard import UserDashboardPage
from utils import get_temp_data, is_string_present


class ClientManagement(CreateClient):

    def __init__(self, config):
        super().__init__(config)
        self.dialog = {}
        self.page = UserDashboardPage(self.config)

    def open_restrict_processing(self):
        BaseClientPage(self.config).client_actions_menu().hover_over_client_actions().select_restrict_processing()
        return self

    def confirm_restriction(self):
        ClientRestrictProcessing(BaseClientPage(self.config)).click_confirm_button()
        return self

    def search_for_client(self):
        client = get_temp_data(self.config, "client")
        ClientSearch(self.config)\
            .click_clear_button()\
            .fill_in_firstname(client["person"]["firstName"])\
            .fill_in_lastname(client["person"]["lastName"])\
            .click_go_button()
        return self

    def verify_client_not_present_in_result(self):
        client = get_temp_data(self.config, "client")
        clientsearch = ClientSearch.ClientQuickSearchResult(self.config)
        assert not is_string_present(clientsearch.get_client_search_result(), client["person"]["firstName"]), \
            "User is present in the list."
        assert not is_string_present(clientsearch.get_client_search_result(), client["person"]["lastName"]), \
            "User is present in the list."
        return self

    def close_search_result_dialog(self):
        clientsearch = ClientSearch.ClientQuickSearchResult(self.config)
        clientsearch.driver.switch_to.default_content()
        clientsearch.close_client_search_dialog()
        return self

    def verify_client_not_present_in_recent_clients(self):
        client = get_temp_data(self.config, "client")
        is_string_present(UserDashboardPage(self.config).get_recent_clients(), client["person"]["firstName"])
        return self
