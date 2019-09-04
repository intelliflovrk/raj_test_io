#!/usr/bin/env python

""" This is a test designed to fail for DevOps testing """

import pytest
from ioffice.userdashboard import UserDashboardPage
import sys


@pytest.mark.skipif('fail' not in sys.argv, reason='fail has not been passed as a marker')
@pytest.mark.fail
@pytest.mark.io_all
@pytest.mark.usefixtures("ui_login_logout")
def test_login_fail(config):
    """ Test Description: Logging in and out of IO and asserting that the title is incorrect """
    dashboard = UserDashboardPage(config)
    assert not dashboard.is_title_matches(), "Title does not match the user dashboard"
