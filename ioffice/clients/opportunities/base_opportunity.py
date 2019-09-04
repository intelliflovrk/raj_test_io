from selenium.webdriver.common.by import By
from ioffice.clients.base import BaseClientPage, BasePageSection
import re


class OpportunityBasePage(BaseClientPage):

    def hover_over_opportunity_actions(self):
        self.hover_over(OpportunityBasePage.Locators.OPPORTUNITY_ACTIONS_MENU)
        return OpportunityActionsMenuSection(self)

    def get_opportunity_ref(self):
        return re.search("IOO\d+", self.get_text(OpportunityBasePage.Locators.BAR_INFO_TEXT)).group(0)

    def get_opportunity_id(self):
        url = self.driver.current_url
        return re.search("(?<=ViewOpportunity\/)\d+", url, flags=re.IGNORECASE).group(0)

    class Locators(object):
        OPPORTUNITY_ACTIONS_MENU = (By.ID, "secondary")
        BAR_INFO_TEXT = (By.CSS_SELECTOR, ".bar-info")


class OpportunityActionsMenuSection(BasePageSection):

    def click_delete_opportunity(self):
        self.page.click(OpportunityActionsMenuSection.Locators.DELETE_OPPORTUNITY_LINK)
        return self

    class Locators(object):
        DELETE_OPPORTUNITY_LINK = (By.XPATH, "//a[text()='Delete Opportunity']")
