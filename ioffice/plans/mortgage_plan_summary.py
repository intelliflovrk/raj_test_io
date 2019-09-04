from ioffice.plans.base_summary import *


class MortgagePlanSummaryPage(BasePlanSummaryPage):

    def is_mortgage_details_section_present(self):
        return "Mortgage Details" == WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MortgagePlanSummaryPage.Locators.MORTGAGE_DETAILS_SECTION_LABEL)).text

    def get_price_valuation(self):
        return self.get_attribute(self.Locators.PRICE_VALUATION, "value")

    def get_equity_deposit(self):
        return self.get_attribute(self.Locators.DEPOSIT_EQUITY, "value")

    def get_second_owner_name(self):
        return self.get_drop_down_selected_value(self.Locators.SECOND_OWNER)

    def click_save(self):
        self.click(self.Locators.SAVE)
        return self

    class Locators(object):
        MORTGAGE_DETAILS_SECTION_LABEL = (By.XPATH, "//div[@class='label'][contains(text(), 'Mortgage Details')]")
        PRICE_VALUATION = (By.ID, "Price")
        DEPOSIT_EQUITY = (By.ID, "Deposit")
        SAVE = (By.ID, "SavePlanSummaryBtn")
        SECOND_OWNER = (By.ID, "SummaryTab_Owner2")