import pytest
from dsl.send_secure_message_to_adviser import SecureMessage

pytestmark = [pytest.mark.pfp, pytest.mark.pfp_secure_message]


@pytest.mark.usefixtures("ui_pfp_login_logout")
def test_send_secure_message(config):
    """ Test Description: Send a secure message and verify "Compose Message" dialogue closed"""
    test = (SecureMessage(config)
            .using_contact_adviser_dialogue()
                .send_basic_message()
            .verify_dashboard_loaded()
            )


@pytest.mark.usefixtures("ui_pfp_login_logout", "api_send_secure_message")
def test_sent_items(config):
    """ Test Description: Verify that a sent message appears among sent items"""
    test = (SecureMessage(config)
            .open_secure_messages()
            .open_sent_messages()
            .verify_message_present_in_sent_messages()
            )