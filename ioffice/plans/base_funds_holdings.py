from ioffice.plans.base import *


class BasePlanFundsHoldingsPage(BasePlanPage):

    def is_title_matches(self):
        return "Funds / Holdings | Intelligent Office" == self.driver.title

    def get_units_holdings_value(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(BasePlanFundsHoldingsPage.Locators.UNITS_HOLDING_VALUE)).text

    def check_select_all_funds(self):
        return self.click(BasePlanFundsHoldingsPage.Locators.SELECT_ALL_CHECKBOX)

    def click_delete(self):
        return self.click(BasePlanFundsHoldingsPage.Locators.DELETE_BUTTON)

    def get_current_model_portfolio(self):
        return self.get_text(BasePlanFundsHoldingsPage.Locators.CURRENT_MODEL_PORTFOLIO_TEXT)

    def get_latest_version_available(self):
        return self.get_text(BasePlanFundsHoldingsPage.Locators.LATEST_VERSION_AVAILABLE_LINK)

    def get_assigned_model_portfolio(self):
        return self.get_text(BasePlanFundsHoldingsPage.Locators.ASSIGNED_MODEL_PORTFOLIO_TEXT)

    def get_fund_proposal_fund_names(self):
        return WebDriverWait(self.driver, self.TIMEOUT)\
            .until(EC.presence_of_all_elements_located(BasePlanFundsHoldingsPage.Locators.FUND_PROPOSAL_FUND_NAMES_TEXT))

    def click_pick_holdings_filter(self):
        return self.click(self.Locators.HOLDING_FILTER_BUTTON)

    def click_all_holdings(self):
        return self.click(self.Locators.ALL_HOLDINGS_LINK)

    class Locators(object):
        UNITS_HOLDING_VALUE = (By.XPATH, "//table/tbody//td[6]/span")
        SELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, "#grid_ecGridFunds thead input[type='checkbox']")
        DELETE_BUTTON = (By.ID, "ecGridFunds_22")
        CURRENT_MODEL_PORTFOLIO_TEXT = (By.ID, 'id_Current_Name_ro')
        LATEST_VERSION_AVAILABLE_LINK = (By.ID, 'viewLaterModel')
        ASSIGNED_MODEL_PORTFOLIO_TEXT = (By.ID, 'MainForm_2_2')
        FUND_PROPOSAL_FUND_NAMES_TEXT = (By.CSS_SELECTOR, '#grid_gridExistingFunds tbody tr .first span ')
        HOLDING_FILTER_BUTTON = (By.CSS_SELECTOR, '.dropPickerHandle a')
        ALL_HOLDINGS_LINK = (By.CSS_SELECTOR, ".dropPickerItem a[href*='all']")
