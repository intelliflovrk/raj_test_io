import utils
from dsl.get_client_quote import GetClientQuote
from ioffice.clients.source_mortgage_dialog import SourceMortgageDialog
from ioffice.clients.client_dashboard import ClientDashboardPage


class SourceMortgage(GetClientQuote):
    def __init__(self, config):
        super().__init__(config)
        self.driver = config.driver

    def using_source_mortgage_dialog(self):
        ClientDashboardPage(self.config) \
            .client_actions_menu() \
            .hover_over_client_actions() \
            .add_source_mortgage()
        self.dialog = SourceMortgage._SourceMortgageDialog(ClientDashboardPage(self.config), self)
        return self.dialog

    def switch_to_io_window(self):
        utils.switch_to_parent_window(self)
        return self

    class _SourceMortgageDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = SourceMortgageDialog(current_page)

        def open_mortgage_brain_anywhere(self):
            self.dialog\
                .click_mortgage_brain_anywhere_radio_button()\
                .click_next_button()
            return MortgageBrainAnywhere(self.config)


class MortgageBrainAnywhere(SourceMortgage):

    def verify_mortgage_brain_anywhere_status_code(self):
        utils.switch_to_window_by_title(self, "Level 1 Filters")
        assert 200 == utils.get_response_code_by_url(self.driver.current_url), "Incorrect status code"
        utils.close_current_window(self)
        return self