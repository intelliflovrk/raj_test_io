from ioffice.base import *
from selenium.webdriver.common.by import By
from pageobjects import BasePageSection


class BaseOrganisationPage(IOBasePage):

    def level3_menu(self):
        return IoLevel3NavigationMenuSection(self)


class IoLevel3NavigationMenuSection(BasePageSection, BasePage):

    def click_factfind(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.FACTFIND_TAB)

    class Locators(object):
        FACTFIND_TAB = (By.CSS_SELECTOR, "ul.nav-tertiary.group > li:nth-child(4) > a")
