from pfp.base import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self, config):
        super().__init__(config)
        self.domain = config.get_pfp_domain()

    def enter_login(self):
        self.key_enter(self.Locators.LOGIN_BUTTON)
        return self

    def load(self):
        self.driver.get(self.domain)
        return self

    def is_title_matches(self):
        return "Home - Personal Finance Portal (PFP)" == self.driver.title

    class Locators(object):
        LOGIN_BUTTON = (By.CSS_SELECTOR, ".page-nav-loggedout .btn-primary")

