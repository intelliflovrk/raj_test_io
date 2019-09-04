from ioffice.base import *
from ioffice.base import BasePage
from selenium.webdriver.common.by import By
from pageobjects import BasePageSection
import re


class BaseUserPage(IOBasePage):

    def level4_menu(self):
        return IoLevel4NavigationMenuSection(self)

    def user_actions_menu(self):
        return UserActionsMenuSection(self)

    def get_user_id(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(BaseUserPage.Locators.USER_BAR_INFO))
        url = self.driver.current_url
        return re.search(r'(?<=user/)\d+', url, flags=re.IGNORECASE).group(0)

    class Locators(object):
        ACTIONS_MENU = (By.ID, "primary")
        USER_BAR_INFO = (By.XPATH, "//div[@class='bar-info']/strong")


class IoLevel4NavigationMenuSection(BasePageSection, BasePage):

    def click_delegates_tab(self):
        return self.click(IoLevel4NavigationMenuSection.Locators.DELEGATES_TAB)

    class Locators(object):
        DELEGATES_TAB = (
            By.CSS_SELECTOR, "li:nth-child(3) > a > div > div > div > div.ux-lib-tcontent > div")


class UserActionsMenuSection(BasePageSection, BaseUserPage):

    def hover_over_user_actions_menu(self):
        return self.hover_over(BaseUserPage.Locators.ACTIONS_MENU)

    def click_add_delegate(self):
        return self.click(UserActionsMenuSection.Locators.ADD_DELEGATE)

    class Locators(object):
        ADD_DELEGATE = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Add Delegate')]")
