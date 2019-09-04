from ioffice.clients.service_case.service_cases import ServiceCasePage
from ioffice.clients.service_case.base import ServiceCaseBasePage
from ioffice.clients.service_case.delete_service_case_dialog import DeleteServiceCaseDialog
from ioffice.clients.base import BaseClientPage


class ClientServiceCase:
    def __init__(self, config):
        self.config = config

    def navigate_to_service_cases(self):
        BaseClientPage(self.config)\
            .level3_menu()\
            .click_service_case()
        return ClientServiceCase._ClientServiceCasesList(self)

    class _ClientServiceCasesList:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = ServiceCasePage(self.config)

        def open_service_case(self):
            self.page.click_first_open_link()
            return ClientServiceCase._ClientServiceCase(self)

    class _ClientServiceCase:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = ServiceCaseBasePage(self.config)

        def delete_service_case(self):
            self.page.hover_over_service_case_actions_menu()\
                .click_delete_service_case()
            DeleteServiceCaseDialog(self.page)\
                .click_delete()\
                .close_dialog()
            return self.journey
