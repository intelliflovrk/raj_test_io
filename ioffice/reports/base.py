from selenium.webdriver.common.by import By

from ioffice.base import IOBasePage


class BaseReportsPage(IOBasePage):

    def click_run_protfolio_report(self):
        return self.click(BaseReportsPage.Locators.RUN_PORTFOLIO_REPORT)

    class Locators(object):
        RUN_PORTFOLIO_REPORT = (By.CSS_SELECTOR, "#id_root_2_2_3__1 > td.last > a")
