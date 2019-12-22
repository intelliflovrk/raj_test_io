import pytest

from dsl.login_to_devhub import LogIn

pytestmark = [pytest.mark.devhub_login, pytest.mark.devhub]


def test_login_logoff(config):
    """Logging in and out of DevHub."""
    test = (LogIn(config)
            .navigate_to_login_page()
            .login()
            .assert_user_logged_in()
            .logout()
            .assert_user_logged_out()
            )