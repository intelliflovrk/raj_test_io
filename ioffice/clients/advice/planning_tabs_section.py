from selenium.webdriver.common.by import By
from ioffice.clients.base import BasePageSection


class PlanningTabsSection(BasePageSection):

    def click_fact_find(self):
        self.page.click(PlanningTabsSection.Locators.FACT_FIND_TAB)
        return self

    def click_research_tools(self):
        self.page.click(PlanningTabsSection.Locators.RESEARCH_TOOLS_TAB)
        return self

    def click_recommendations(self):
        self.page.click(PlanningTabsSection.Locators.RECOMMENDATIONS_TAB)
        return self

    class Locators(object):
        FACT_FIND_TAB = (By.ID, 'planningfactfind')
        RESEARCH_TOOLS_TAB = (By.ID, 'planningresearchtools')
        RECOMMENDATIONS_TAB = (By.ID, 'planningrecommendations')
