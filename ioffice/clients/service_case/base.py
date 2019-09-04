from selenium.webdriver.common.by import By
from ioffice.clients.base import BaseClientPage, BasePageSection


class ServiceCaseBasePage(BaseClientPage):

    def hover_over_service_case_actions_menu(self):
        self.hover_over(ServiceCaseBasePage.Locators.SERVICE_CASE_ACTIONS_MENU)
        return ServiceCaseActionsMenuSection(self)

    class Locators(object):
        SERVICE_CASE_ACTIONS_MENU = (By.ID, "secondary")


class ServiceCaseActionsMenuSection(BasePageSection):

    def click_delete_service_case(self):
        self.page.click(ServiceCaseActionsMenuSection.Locators.DELETE_SERVICE_CASE_LINK)
        return self

    class Locators(object):
        DELETE_SERVICE_CASE_LINK = (By.XPATH, "//a[text()='Delete Service Case']")
