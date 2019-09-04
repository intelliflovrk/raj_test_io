from selenium.webdriver.common.by import By

from ioffice.base import IOBasePage
from pageobjects import BasePageSection, BasePage


class BaseOrganiserPage(IOBasePage):

    def level2_menu(self):
        return IoLevel2NavigationMenuSection(self)

    class Locators(object):
        pass


class IoLevel2NavigationMenuSection(BasePageSection, BasePage):

    def click_tasks(self):
        return self.click(IoLevel2NavigationMenuSection.Locators.TASKS_TAB)

    class Locators(object):
        TASKS_TAB = (By.CSS_SELECTOR, "#secure_marker > li:nth-child(1) > a")
