from pfp.base import PFPBasePage
from selenium.webdriver.common.by import By


class RecommendationPage(PFPBasePage):

    def click_accept(self):
        return self.click(RecommendationPage.Locators.ACCEPT_BUTTON)

    class Locators(object):
        ACCEPT_BUTTON = (By.CSS_SELECTOR, "button[title='Accept']")
