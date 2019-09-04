import pytest

from dsl.login_to_pfp import LogIn

pytestmark = [pytest.mark.pfp_login, pytest.mark.pfp]


def test_pfp_login_logoff(config):
    """ Test Description: Logging in and out of PFP """
    test = (LogIn(config)
            .navigate_to_login_page()
            .login()
            .assert_user_logged_in()
            .logout()
            .assert_user_logged_out()
            )
