from selenium.webdriver.common.by import By
from ioffice.clients.client_dashboard import BaseClientPage


class ServiceCasePage(BaseClientPage):

    def get_service_case_name(self):
        return self.get_text(self.Locators.SERVICE_CASE_NAME)

    def click_first_open_link(self):
        return self.click(ServiceCasePage.Locators.FIRST_OPEN_LINK)

    class Locators(object):
        SERVICE_CASE_NAME = (By.XPATH, "//span[contains(text(),'Test Automation Service Case')]")
        FIRST_OPEN_LINK = (By.CSS_SELECTOR, "#grid_ListAdviceCasesForClient tbody a[title='Open']")
