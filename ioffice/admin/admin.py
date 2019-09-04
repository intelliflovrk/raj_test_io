from ioffice.base import IOBasePage
from pageobjects import BasePageSection
from selenium.webdriver.common.by import By


class AdministrationPage(IOBasePage):

    def is_title_matches(self):
        return "User Search | Intelligent Office" == self.driver.title

    def level2_menu(self):
        return IoLevel2NavigationMenuSection(self)

    class Locators(object):
        pass


class IoLevel2NavigationMenuSection(BasePageSection, IOBasePage):

    def click_workflow(self):
        return self.click(IoLevel2NavigationMenuSection.Locators.WORKFLOW_TAB), "Workflow tab not found"

    def click_manage_users(self):
        return self.click(IoLevel2NavigationMenuSection.Locators.MANAGE_USERS_TAB), "Manage Users tab not found"

    def click_organisation(self):
        return self.click(IoLevel2NavigationMenuSection.Locators.ORGANISATION_TAB), "Organisation tab not found"

    class Locators(object):
        WORKFLOW_TAB = (By.CLASS_NAME, 'menu_node_administration_workflow')
        ORGANISATION_TAB = (By.CSS_SELECTOR, '#secure_marker > li:nth-child(2) > a')
        MANAGE_USERS_TAB = (By.CSS_SELECTOR, '#secure_marker > li:nth-child(1) > a')
