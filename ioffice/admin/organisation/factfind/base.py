from ioffice.base import *
from selenium.webdriver.common.by import By
from pageobjects import BasePageSection


class BaseOrganisationFactFindPage(IOBasePage):

    def level4_menu(self):
        return IoLevel4NavigationMenuSection(self)


class IoLevel4NavigationMenuSection(BasePageSection, BasePage):

    def click_needs_questions(self):
        return self.click(IoLevel4NavigationMenuSection.Locators.NEEDS_QUESTIONS_TAB)

    class Locators(object):
        NEEDS_QUESTIONS_TAB = (
            By.CSS_SELECTOR, "li:nth-child(4) > a > div > div > div > div.ux-lib-tcontent > div")
