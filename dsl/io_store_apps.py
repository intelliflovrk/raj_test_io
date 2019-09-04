from dsl.search import SearchClient
from ioffice.clients.base import BaseClientPage
from utils import get_str_list_from_list_of_webelements
import time


class IOStoreApps(SearchClient):

    def open_client_actions_menu(self):
        BaseClientPage(self.config).client_actions_menu().hover_over_client_actions()
        return self

    def verify_app_link_is_present_in_client_actions_menu(self, link_text):
        time.sleep(1)
        assert link_text in get_str_list_from_list_of_webelements(
            BaseClientPage(self.config).client_actions_menu().get_io_store_apps_links()),\
            "{0} not found".format(link_text)
        return self
