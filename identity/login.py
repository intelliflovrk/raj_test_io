from pageobjects import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def click_login_button(self):
        self.click(self.Locators.LOGIN_BUTTON)
        return self

    def fill_in_username_field(self, data):
        self.clear_and_fill_in_field(self.Locators.USERNAME, data)
        return self

    def fill_in_password_field(self, data):
        self.clear_and_fill_in_field(self.Locators.PASSWORD, data)
        return self

    class Locators(object):
        LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Login']")
        USERNAME = (By.ID, "username")
        PASSWORD = (By.ID, "password")


class UnipassLoginPage(BasePage):

    def fill_in_username_field(self, data):
        self.fill_in_field(self.Locators.USERNAME, data)
        return self

    def fill_in_password_field(self, data):
        self.fill_in_field(self.Locators.PASSWORD, data)
        return self

    def click_login_button(self):
        return self.click(UnipassLoginPage.Locators.LOGIN_BUTTON)

    class Locators(object):
        LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Login']")
        USERNAME = (By.ID, "username")
        PASSWORD = (By.ID, "password")


