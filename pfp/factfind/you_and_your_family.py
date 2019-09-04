from pfp.base import PFPBasePage
from selenium.webdriver.common.by import By


class YouAndYourFamily(PFPBasePage):

    def click_about_you(self):
        return self.click(self.Locators.ABOUT_YOU_LINK)

    def click_your_family(self):
        return self.click(self.Locators.YOUR_FAMILY_LINK)

    def click_employment(self):
        return self.click(self.Locators.EMPLOYMENT_LINK)

    class Locators:
        ABOUT_YOU_LINK = (By.ID, "your-profile-tab")
        YOUR_FAMILY_LINK = (By.CSS_SELECTOR, "a[title='Your Family']")
        EMPLOYMENT_LINK = (By.CSS_SELECTOR, "a[title='Employment']")
