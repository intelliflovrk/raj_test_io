from ioffice.adviser_workplace.fund_analysis.base import FundAnalysisBasePage
from selenium.webdriver.common.by import By


class ViewRebalancePage(FundAnalysisBasePage):

    def click_start_rebalance_communication(self):
        return self.click(ViewRebalancePage.Locators.START_REBALANCE_COMMUNICATION_BUTTON)

    def click_first_report_link(self):
        return self.click(ViewRebalancePage.Locators.REPORT_LINKS)

    class Locators(object):
        START_REBALANCE_COMMUNICATION_BUTTON = (By.ID, "startRebalanceButton")
        REPORT_LINKS = (By.CSS_SELECTOR, "a[href*='ExportRebalanceToCsv']")
