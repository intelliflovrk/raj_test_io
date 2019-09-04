from ioffice.base import BasePage
from selenium.webdriver.common.by import By


class UsersSearchPage(BasePage):

    def is_title_matches(self):
        return "User Search | Intelligent Office" == self.driver.title

    def fill_in_firstname_field(self, data):
        self.fill_in_field(UsersSearchPage.Locators.FIRSTNAME_FIELD, data)
        return self

    def fill_in_lastname_field(self, data):
        self.fill_in_field(UsersSearchPage.Locators.LASTNAME_FIELD, data)
        return self

    def fill_in_username(self, data):
        self.fill_in_field(UsersSearchPage.Locators.USERNAME_FIELD, data)
        return self

    def click_clear(self):
        return self.click(UsersSearchPage.Locators.CLEAR)

    def click_search(self):
        return self.click(UsersSearchPage.Locators.SEARCH)

    def open_first_result(self):
        return self.click(UsersSearchPage.Locators.FIRST_RESULT_OPEN_LINK)

    class Locators(object):
        CLEAR = (By.CSS_SELECTOR, 'div.ux-ctl-search-options > a:nth-child(3)')
        SEARCH = (By.CSS_SELECTOR, 'div.actions.ux-ctl-form-actions > div > a')
        USERNAME_FIELD = (By.ID, "id_User_UserIdentifier")
        FIRSTNAME_FIELD = (By.CSS_SELECTOR, "#id_User_FirstName")
        LASTNAME_FIELD = (By.CSS_SELECTOR, "#id_User_LastName")
        FIRST_RESULT_OPEN_LINK = (By.XPATH, "//td[@class='last']/a")
