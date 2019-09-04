from pageobjects import BasePage
from selenium.webdriver.common.by import By


class DevHubBasePage(BasePage):

    def click_user_menu(self):
        return self.click(DevHubBasePage.Locators.USER_MENU_LINK)

    def click_logout(self):
        return self.click(DevHubBasePage.Locators.LOGOUT_LINK)

    def get_user_menu_text(self):
        return self.get_text(DevHubBasePage.Locators.USER_MENU_LINK)

    class Locators(object):
        USER_MENU_LINK = (By.CSS_SELECTOR, 'a.dropdown-toggle')
        LOGOUT_LINK = (By.XPATH, '*//div/div/ul//li/ul/li[2]/a')
