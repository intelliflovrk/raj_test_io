from pageobjects import BasePageSection
from selenium.webdriver.common.by import By


class AcceptRecommendationDialog(BasePageSection):

    def __init__(self, parent_page):
        super().__init__(parent_page)

    def click_accept(self):
        return self.page.click(AcceptRecommendationDialog.Locators.ACCEPT_BUTTON)

    class Locators(object):
        ACCEPT_BUTTON = (By.CSS_SELECTOR, "#accept-recommendation button[type='submit']")
