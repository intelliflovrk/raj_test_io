from pageobjects import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class PFPBasePage(BasePage):

    def click_logout(self):
        return self.click(self.Locators.LOGOUT_BUTTON)

    def click_contact(self):
        return self.click(self.Locators.CONTACT_BUTTON)

    def click_view_profile_link(self):
        return self.click(self.Locators.VIEW_PROFILE_LINK)

    def is_overlay_visible(self):
        return WebDriverWait(self.driver, self.TIMEOUT) \
            .until(EC.visibility_of_element_located(self.Locators.OVERLAY))

    def is_overlay_invisible(self):
        return WebDriverWait(self.driver, self.TIMEOUT)\
            .until(EC.staleness_of(WebDriverWait(self.driver, self.TIMEOUT)
                                   .until(EC.visibility_of_element_located(self.Locators.OVERLAY))))

    class Locators(object):
        LOGOUT_BUTTON = (By.CSS_SELECTOR, "div > a[title = 'Logout']")
        CONTACT_BUTTON = (By.ID, "composeMessageBtn")
        OVERLAY = (By.CSS_SELECTOR, ".overlay-dimmer")
        VIEW_PROFILE_LINK = (By.CSS_SELECTOR, "a[title='View Profile']")
