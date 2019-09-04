from ioffice.home import HomePage, IOBasePage
from ioffice.userdashboard import UserDashboardPage
from identity.login import LoginPage, UnipassLoginPage
from utils import get_user_by_type


class LogIn:
    def __init__(self, config):
        self.config = config

    def navigate_to_login_page(self):
        HomePage(self.config).load().click_login()
        return self

    def navigate_to_unipass_login_page(self):
        HomePage(self.config).load().click_unipass_login()
        return self

    def login(self):
        LoginPage(self.config)\
            .fill_in_username_field(self.config.username)\
            .fill_in_password_field(self.config.password)\
            .click_login_button()
        return self

    def login_with_unipass(self):
        UnipassLoginPage(self.config)\
            .fill_in_username_field(self.config.username)\
            .fill_in_password_field(self.config.password)\
            .click_login_button()
        return self

    def logout(self):
        IOBasePage(self.config).level1_menu().hover_over_user_navigation_menu().click_logout()
        return self

    def assert_user_logged_in(self):
        assert UserDashboardPage(self.config).is_title_matches(), "Title does not match the user dashboard"
        return self

    def assert_user_logged_out(self):
        assert HomePage(self.config).is_title_matches(), "User is not logged out"
        return self

    def login_as(self, user_type):
        user = get_user_by_type(self.config, user_type)
        HomePage(self.config) \
            .load() \
            .click_login()
        LoginPage(self.config) \
            .fill_in_username_field(user["username"]) \
            .fill_in_password_field(user["password"]) \
            .click_login_button()
        return self