from pageobjects import BasePage, BasePageSection
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class IoStoreBasePage(BasePage):

    def is_title_matches(self):
        return "iO Store" == self.driver.title

    def level1_menu(self):
        return IoStoreLevel1NavigationMenuSection(self)


class IoStoreLevel1NavigationMenuSection(BasePage, BasePageSection):

    def click_home_button(self):
        return self.click(IoStoreLevel1NavigationMenuSection.Locators.HOME_LINK)

    def click_toggle_user_menu(self):
        return self.click(IoStoreLevel1NavigationMenuSection.Locators.USER_MENU_LINK)

    def click_logout(self):
        el = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(IoStoreLevel1NavigationMenuSection.Locators.LOGOUT_LINK))
        return ActionChains(self.driver).move_to_element(el).click().perform()

    class Locators(object):
        """A class for top level navigation locators. All navigation page locators should come here"""

        USER_MENU_LINK = (By.CSS_SELECTOR, "[title='Toggle User Menu']")
        LOGOUT_LINK = (By.XPATH, "//span[text()='Logout']")
        HOME_LINK = (By.CSS_SELECTOR, 'div.p-r-05 > a > div > div > i')

