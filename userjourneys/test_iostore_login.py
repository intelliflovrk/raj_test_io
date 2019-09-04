import pytest
from dsl.login_to_iostore import LogIn

pytestmark = [pytest.mark.login, pytest.mark.iostore]


@pytest.mark.usefixtures("ui_login")
def test_iostore_sso_logoff(config):
    """ Test Description: Logging into IO Store though SSO and out"""
    test = (LogIn(config)
            .navigate_to_iostore()
            .assert_user_logged_in()
            .logout()
            .assert_user_logged_out()
            )
