from ioffice.clients.change_fee_status_dialog import ChangeFeeStatusDialog
from ioffice.clients.client_fee import FeeActionsMenuSection


class FeeActions:
    def __init__(self, config):
        self.config = config

    def open_change_fee_status_dialog(self):
        FeeActionsMenuSection(self.config).hover_over_fee_actions().change_fee_status()
        return FeeActions._ChangeFeeStatusDialog(FeeActionsMenuSection(self.config), self)

    class _ChangeFeeStatusDialog:
        def __init__(self, fee_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ChangeFeeStatusDialog(fee_page)

        def change_fee_status_to(self, status):
            self.dialog.select_status(status).click_save()\
                .wait_until_please_wait_spinner_present()
            self.dialog.close_io_dialog()
            return self.journey
