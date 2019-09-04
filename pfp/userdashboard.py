from pfp.base import PFPBasePage
from selenium.webdriver.common.by import By


class UserDashboardPage(PFPBasePage):

    def is_title_matches(self):
        return "Dashboard - Personal Finance Portal (PFP)" == self.driver.title

    def click_view_all(self):
        return self.click(self.Locators.VIEW_ALL_BUTTON)

    def click_rebalance_recommended(self):
        return self.click(UserDashboardPage.Locators.RECOMMENDATION_LINK)

    class Locators(object):
        VIEW_ALL_BUTTON = (By.CSS_SELECTOR, "a[title='View all Messages']")
        RECOMMENDATION_LINK = (By.CSS_SELECTOR, "#widget_imps a[href*='/imps/recommendation/']")
