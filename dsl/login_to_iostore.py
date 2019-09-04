import time
from ioffice.userdashboard import UserDashboardPage
from iostore.installedapps import InstalledAppsPage
from iostore.logout import LogoutPage
from pageobjects import BasePage


class LogIn:
    def __init__(self, config):
        self.config = config

    def navigate_to_iostore(self):
        UserDashboardPage(self.config).level1_menu().hover_over_navigation_menu().click_iostore()
        time.sleep(5)
        BasePage(self.config).switch_tab(1)
        return self

    def assert_user_logged_in(self):
        assert InstalledAppsPage(self.config).is_title_matches(), "Title does not match the iO Store page"
        return self

    def logout(self):
        InstalledAppsPage(self.config).level1_menu().click_toggle_user_menu().click_logout()
        return self

    def assert_user_logged_out(self):
        assert "You have been logged out." == LogoutPage(self.config).get_logout_message(), "Heading does not match the iO Store Logout Page"
        return self
