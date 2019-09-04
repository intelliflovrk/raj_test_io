from ioffice.base import IOBasePage, BasePageSection
from selenium.webdriver.common.by import By


class AdviserWorkplacePage(IOBasePage):

    def click_leads_tab(self):
        return self.click(AdviserWorkplacePage.Locators.LEADS_TAB)

    def click_clients_tab(self):
        return self.click(AdviserWorkplacePage.Locators.CLIENTS_TAB)

    def adviser_workplace_level_menu(self):
        return AdviserWorkplaceLevelMenuSection(self)

    class Locators(object):
        LEADS_TAB = (By.XPATH, "//*[@id='secure_marker']/li[2]/a")
        CLIENTS_TAB = (By.CSS_SELECTOR, "[class='menu_node_clients_index on io-icon-users']")


class AdviserWorkplaceLevelMenuSection(BasePageSection):

    def click_leads_tab(self):
        self.page.click(AdviserWorkplaceLevelMenuSection.Locators.LEADS_TAB)
        return self

    def click_clients_tab(self):
        self.page.click(AdviserWorkplaceLevelMenuSection.Locators.CLIENTS_TAB)
        return self

    def click_fund_analysis_tab(self):
        self.page.click(AdviserWorkplaceLevelMenuSection.Locators.FUND_ANALYSIS_TAB)
        return self

    class Locators(object):
        LEADS_TAB = (By.XPATH, "//*[@id='secure_marker']/li[2]/a")
        CLIENTS_TAB = (By.CSS_SELECTOR, "[class='menu_node_clients_index on io-icon-users']")
        FUND_ANALYSIS_TAB = (By.CSS_SELECTOR, "[class*='menu_node_FundAnalysis']")
