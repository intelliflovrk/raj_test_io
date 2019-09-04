from selenium.webdriver.common.by import By
from ioffice.clients.base import BaseClientPage
from pageobjects import BasePageSection


class BaseDetailsPage(BaseClientPage):

    def details_navigation_menu(self):
        return DetailsNavigationMenuSection(self)


class DetailsNavigationMenuSection(BasePageSection):

    def click_personal_tab(self):
        return self.page.click(self.Locators.PERSONAL_TAB)

    def click_addresses_tab(self):
        return self.page.click(self.Locators.ADDRESSES_TAB)

    def click_contact_tab(self):
        return self.page.click(self.Locators.CONTACT_TAB)

    def click_notes_tab(self):
        return self.page.click(self.Locators.NOTES_TAB)

    def click_summary_tab(self):
        self.page.click(self.Locators.SUMMARY_TAB)
        return self

    class Locators(object):
        SUMMARY_TAB = (By.XPATH, "//div[contains(text(),'Summary')]")
        NOTES_TAB = (By.XPATH, "//div[contains(text(),'Notes')]")
        PERSONAL_TAB = (By.CSS_SELECTOR, "#id_root_2_2_5 > ul > li:nth-child(2) > a > div")
        ADDRESSES_TAB = (By.CSS_SELECTOR, "#id_root_2_2_5 > ul > li:nth-child(4) > a > div")
        CONTACT_TAB = (By.CSS_SELECTOR, "#id_root_2_2_5 > ul > li:nth-child(5) > a > div")

