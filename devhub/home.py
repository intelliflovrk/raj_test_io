from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pageobjects import BasePage


class HomePage(BasePage):

    def __init__(self, config):
        super().__init__(config)
        self.domain = config.get_devhub_domain()

    def click_login(self):
        return self.click(HomePage.Locators.LOGIN_BUTTON)

    def load(self):
        self.driver.get(self.domain)

    def is_title_matches(self):
        return "Intelliflo Developer Platform" == self.driver.title

    def get_h1_heading(self):
        return self.get_text(HomePage.Locators.H1_HEADING)

    class Locators(object):
        LOGIN_BUTTON = (By.XPATH, "//div[3]/a")
        H1_HEADING = (By.CSS_SELECTOR, "main h1")
