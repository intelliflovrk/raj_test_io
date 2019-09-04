from pfp.base import PFPBasePage
from selenium.webdriver.common.by import By


class ProfilePage(PFPBasePage):

    def click_you_and_your_family_link(self):
        return self.click(self.Locators.YOU_AND_YOUR_FAMILY)

    class Locators(object):
        YOU_AND_YOUR_FAMILY = (By.CSS_SELECTOR, "a[title='You & Your Family']")