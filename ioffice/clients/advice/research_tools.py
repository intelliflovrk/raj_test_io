from selenium.webdriver.common.by import By
from ioffice.clients.base import BaseClientPage
from ioffice.clients.advice.planning_tabs_section import PlanningTabsSection


class ResearchToolsPage(BaseClientPage):

    def __init__(self, config):
        super().__init__(config)
        self.planning_tabs = PlanningTabsSection(self)

    def click_get_new_quote(self):
        return self.click(ResearchToolsPage.Locators.GET_NEW_QUOTE_BUTTON)

    class Locators(object):
        GET_NEW_QUOTE_BUTTON = (By.ID, 'getQuoteToolLauncher')
