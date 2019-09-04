from ioffice.base import IOBasePage
from selenium.webdriver.common.by import By


class HomePage(IOBasePage):

    def __init__(self, config):
        super().__init__(config)
        self.domain = config.get_io_domain()

    def click_login(self):
        return self.click(HomePage.Locators.LOGIN_BUTTON)

    def click_unipass_login(self):
        return self.click(HomePage.Locators.UNIPASS_LOGIN_BUTTON)

    def load(self):
        self.driver.get(self.domain)
        return self

    def is_title_matches(self):
        return "Login | Intelligent Office" == self.driver.title

    class Locators(object):
        LOGIN_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-primary btn-block btn-lg")
        UNIPASS_LOGIN_BUTTON = (By.CSS_SELECTOR, r"[href='\/nio\/authentication\/loginIdentityUnipass']")
