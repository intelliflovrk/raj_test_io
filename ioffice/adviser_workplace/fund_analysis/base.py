from ioffice.adviserworkplace import AdviserWorkplacePage, BasePageSection
from selenium.webdriver.common.by import By


class FundAnalysisBasePage(AdviserWorkplacePage):

    def fund_analysis_level_menu(self):
        return FundAnalysisLevelMenuSection(self)


class FundAnalysisLevelMenuSection(BasePageSection):

    def click_rebalance_tab(self):
        self.page.click(FundAnalysisLevelMenuSection.Locators.REBALANCE_TAB)
        return self

    class Locators(object):
        REBALANCE_TAB = (By.CSS_SELECTOR, ".menu_node_FundAnalysisRebalance  ")
