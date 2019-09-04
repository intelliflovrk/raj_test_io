from pfp.base import PFPBasePage
from pfp.compose_message_dialogue import ComposeMessageDialogue
from pfp.secure_messaging_base import BaseSecureMessagingPage
from pfp.sent_messages import SentMessagesPage
from pfp.userdashboard import UserDashboardPage
from fakedata import rand_text
from utils import get_temp_data


class SecureMessage:

    def __init__(self, config):
        self.config = config

    def using_contact_adviser_dialogue(self):
        pfp_base_page = PFPBasePage(self.config).click_contact()
        return SecureMessage._ComposeMessageDialogue(pfp_base_page, self)

    def verify_dashboard_loaded(self):
        assert PFPBasePage(self.config).is_overlay_visible(), "Overlay is not visible"
        assert PFPBasePage(self.config).is_overlay_invisible(), "Overlay is displayed"
        return self

    def open_secure_messages(self):
        UserDashboardPage(self.config).click_view_all()
        return self

    def open_sent_messages(self):
        BaseSecureMessagingPage(self.config).click_sent_messages()
        return self._SentMessages(self)

    class _ComposeMessageDialogue:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ComposeMessageDialogue(current_page)

        def send_basic_message(self):
            self.dialog\
                .fill_in_subject(rand_text(10))\
                .fill_in_body(rand_text(10))\
                .click_send()
            return self.journey

    class _SentMessages:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = SentMessagesPage(self.config)

        def verify_message_present_in_sent_messages(self):
            assert self.page.get_message_title() == get_temp_data(self.config, "secure_message")["subject"], "Subject does not match"
