from ioffice.base import *
from selenium.webdriver.common.by import By
from pageobjects import BasePageSection


class BaseManageUsersPage(IOBasePage):

    def level3_menu(self):
        return IoLevel3NavigationMenuSection(self)


class IoLevel3NavigationMenuSection(BasePageSection, BasePage):

    def click_users(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.USERS_TAB)

    class Locators(object):
        USERS_TAB = (By.CSS_SELECTOR, "ul.nav-tertiary.group > li:nth-child(1) > a")
