from ioffice.clients.base import BaseClientPage, BasePageSection
from selenium.webdriver.common.by import By


class ActivitiesBasePage(BaseClientPage):
    def activities_navigation_menu(self):
        return ActivitiesNavigationMenuSection(self)


class ActivitiesNavigationMenuSection(BasePageSection):

    def click_tasks_and_appts(self):
        self.page.click(ActivitiesNavigationMenuSection.Locators.TASKS_AND_APPTS_TAB)
        return self

    def click_workflows(self):
        self.page.click(ActivitiesNavigationMenuSection.Locators.WORKFLOWS_TAB)
        return self

    class Locators(object):
        WORKFLOWS_TAB = (By.CSS_SELECTOR, ".tabTabs a[href*='ViewWorkflows']")
        TASKS_AND_APPTS_TAB = (By.CSS_SELECTOR, ".tabTabs a[href*='ListClientActivity']")
