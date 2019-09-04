from ioffice.base import BasePage
from selenium.webdriver.common.by import By


class DelegationSupportUsersPage(BasePage):

    def is_title_matches(self):
        return "Administration | Application Support | Delegation - Support Users | Intelligent Office" == self.driver.title

    def click_clear_button(self):
        return self.click(Locators.CLEAR_BUTTON)

    def click_search_button(self):
        return self.click(Locators.SEARCH_BUTTON)


class Locators(object):
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'div.actions.ux-ctl-form-actions > div > a')
    CLEAR_BUTTON = (By.LINK_TEXT, 'Clear')
