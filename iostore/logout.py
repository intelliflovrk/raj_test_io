from selenium.webdriver.common.by import By
from iostore.base import IoStoreBasePage


class LogoutPage(IoStoreBasePage):

    def get_logout_message(self):
        return self.get_text(LogoutPage.Locators.LOGOUT_MESSAGE)

    class Locators:
        LOGOUT_MESSAGE = (By.XPATH, "//h2[contains(text(),'You have been logged out.')]")
