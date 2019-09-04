from ioffice.base import IOBasePage
from selenium.webdriver.common.by import By


class ApplicationSupportPage(IOBasePage):

    def click_tertiary_menu_item(self):
        return self.click(Locators.DELEGATION_SUPPORT_USERS_LINK)


class Locators(object):
    DELEGATION_SUPPORT_USERS_LINK = (By.LINK_TEXT, "Delegation - Support Users")
