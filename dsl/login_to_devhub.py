from devhub.home import HomePage
from devhub.base import DevHubBasePage
from identity.login import LoginPage


class LogIn:
    def __init__(self, config):
        self.config = config

    def navigate_to_login_page(self):
        home = HomePage(self.config)
        home.load()
        home.click_login()
        return self

    def login(self):
        LoginPage(self.config)\
            .fill_in_username_field(self.config.username)\
            .fill_in_password_field(self.config.password)\
            .click_login_button()
        return self

    def assert_user_logged_in(self):
        assert "Welcome," in DevHubBasePage(self.config).get_user_menu_text()
        return self

    def logout(self):
        DevHubBasePage(self.config).click_user_menu().click_logout()
        return self

    def assert_user_logged_out(self):
        assert "Intelliflo Developer Platform" == HomePage(self.config).get_h1_heading(), "Heading does not match the DebHub Home Page"
        return self
