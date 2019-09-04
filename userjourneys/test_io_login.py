import pytest
from dsl.login_to_io import *
import sys

pytestmark = [pytest.mark.login, pytest.mark.io_all]


def test_login_logoff(config):
    """ Test Description: Logging in and out of IO """
    test = (LogIn(config)
            .navigate_to_login_page()
            .login()
            .assert_user_logged_in()
            .logout()
            .assert_user_logged_out()
            )


@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='fails on tst')
@pytest.mark.unipass
@pytest.mark.usefixtures("ui_logout")
def test_unipass_login(config):
    """ Test Description: Logging in IO via the Unipass button """
    test = (LogIn(config)
            .navigate_to_unipass_login_page()
            .login_with_unipass()
            .assert_user_logged_in()
            )
