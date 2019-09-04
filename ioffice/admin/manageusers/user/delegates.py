from ioffice.base import BasePage
from selenium.webdriver.common.by import By


class DelegatesPage(BasePage):

    def is_title_matches(self):
        return "Delegates | Intelligent Office" == self.driver.title

    def click_delete_button(self):
        return self.click(DelegatesPage.Locators.DELETE)

    def click_first_result_checkbox(self):
        return self.click(DelegatesPage.Locators.FIRST_RESULT)

    class Locators(object):
        DELETE = (By.CSS_SELECTOR, '#id_root_2_2_3_4_3_6')
        FIRST_RESULT = (By.XPATH, "//*[contains(., 'Delegation')]/td[1]/input")
