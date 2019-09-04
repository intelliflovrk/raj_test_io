import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ioffice.base import *
from ioffice.clients.base import BaseClientPage


class BasePlanPage(BaseClientPage):

    def get_bar_info(self):
        return self.get_text(BasePlanPage.Locators.BAR_INFO)

    def get_plan_id(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(BasePlanPage.Locators.STATUS_AND_REF_BAR_INFO))
        url = self.driver.current_url
        return re.search(r'(?<=SummaryPlan/)\d+', url, flags=re.IGNORECASE).group(0)

    def get_plan_ref(self):
        return "IOB" + re.search(r'(?<=IOB)\d+', self.get_text(BasePlanPage.Locators.STATUS_AND_REF_BAR_INFO)).group(0)

    def plan_actions(self):
        return PlanActionsMenuSection(self)

    def click_activities(self):
        return self.click(BasePlanPage.Locators.ACTIVITIES_TAB)

    def click_contributions(self):
        return self.click(BasePlanPage.Locators.CONTRIBUTION_TAB)

    def click_withdrawals(self):
        return self.click(BasePlanPage.Locators.WITHDRAWALS_TAB) 

    def click_summary(self):
        return self.click(BasePlanPage.Locators.SUMMARY_TAB)

    def click_valuations(self):
        return self.click(BasePlanPage.Locators.VALUATIONS_TAB)        

    def click_funds_holdings(self):
        return self.click(BasePlanPage.Locators.FUNDS_HOLDINGS_TAB)

    def click_open_first_plan_fee(self):
        self.click(BasePlanPage.Locators.FIRST_PLAN_FEE)
        return self

    def plan_level_menu(self):
        return PlanLevelMenuSection(self)

    class Locators(object):
        BAR_INFO = (By.XPATH, "//div[@class='bar-info']/strong[2]")
        STATUS_AND_REF_BAR_INFO = (By.XPATH, "//div[@class='bar-info']")
        ACTIONS_MENU = (By.ID, "secondary")
        ACTIVITIES_TAB = (By.XPATH, "//a[contains(@href, '/TasksTab/')]")
        CONTRIBUTION_TAB = (By.XPATH, "//a[contains(@href, '/ContributionsTab/')]")
        WITHDRAWALS_TAB = (By.XPATH, "//a[contains(@href, '/WithdrawalsTab/')]")
        FUNDS_HOLDINGS_TAB = (By.CSS_SELECTOR, "a[href*='FundsHoldingsTab']")
        SUMMARY_TAB = (By.CSS_SELECTOR, "a[href*='SummaryPlan']")
        VALUATIONS_TAB = (By.CSS_SELECTOR, "a[href*='ValuationsTab']")
        FIRST_PLAN_FEE = (By.XPATH, "//table[@id='grid_RelateToFeeGrid']/tbody/tr[1]//a")


class PlanActionsMenuSection(BasePageSection, BasePage):

    def hover_over_plan_actions(self):
        return self.hover_over(BasePlanPage.Locators.ACTIONS_MENU)

    def add_valuation(self):
        return self.click(PlanActionsMenuSection.Locators.ADD_VALUATION_LINK)

    def add_fund(self):
        return self.click(PlanActionsMenuSection.Locators.ADD_FUND_LINK)

    def add_fee(self):
        return self.click(PlanActionsMenuSection.Locators.ADD_FEE_LINK)

    def change_plan_status(self):
        return self.click(PlanActionsMenuSection.Locators.CHANGE_STATUS_LINK)

    def add_sub_plan(self):
        return self.click(PlanActionsMenuSection.Locators.ADD_SUB_PLAN_LINK)

    def click_upload_document(self):
        return self.click(PlanActionsMenuSection.Locators.UPLOAD_DOCUMENT_LINK)

    def add_to_wrapper(self):
        return self.click(PlanActionsMenuSection.Locators.ADD_TO_WRAPPER_LINK)

    class Locators(object):
        ADD_VALUATION_LINK = (By.CSS_SELECTOR, "#secondary a[onclick*= 'Add Valuation']")
        ADD_FUND_LINK = (By.CSS_SELECTOR, "#secondary a[onclick*= 'Add Fund']")
        ADD_FEE_LINK = (By.CSS_SELECTOR, "#secondary a[onclick*= 'Add Fee']")
        ADD_SUB_PLAN_LINK = (By.CSS_SELECTOR, "#secondary a[onclick*= 'Add Sub Plan']")
        CHANGE_STATUS_LINK = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Change Status')]")
        ADD_TO_WRAPPER_LINK = (By.CSS_SELECTOR, "#secondary a[onclick*= 'Add To Wrapper']")
        UPLOAD_DOCUMENT_LINK = (By.CSS_SELECTOR, "#secondary a[onclick*= 'Upload Document']")


class PlanLevelMenuSection(BasePageSection):

    def click_more_tabs(self):
        self.page.click(PlanLevelMenuSection.Locators.MORE_TABS_BUTTON)
        return self

    def click_recommendations_tab(self):
        self.page.click(PlanLevelMenuSection.Locators.RECOMMENDATIONS_TAB)
        return self

    class Locators(object):
        MORE_TABS_BUTTON = (By.CSS_SELECTOR, ".nextGroup")
        RECOMMENDATIONS_TAB = (By.CSS_SELECTOR, "a[href*='RecommendationsTab']")
