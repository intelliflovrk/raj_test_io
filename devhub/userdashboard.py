from devhub.base import DevHubBasePage
from selenium.webdriver.common.by import By


class DeveloperDashboardPage(DevHubBasePage):

    def is_title_matches(self):
        return "Intelliflo Developer Platform" == self.driver.title

    def click_create_app_button(self):
        return self.click(DeveloperDashboardPage.Locators.CREATE_APP_BUTTON)

    def click_modal_cancel_button(self):
        return self.click(DeveloperDashboardPage.Locators.MODAL_CANCEL_BUTTON)

    class Locators(object):
        CREATE_APP_BUTTON = (By.XPATH, "*//div/div/div/div/div[1]/a")
        MODAL_CANCEL_BUTTON = (By.XPATH, "//*[@id='modal-wrapper']//form/div[2]/button[2]")
