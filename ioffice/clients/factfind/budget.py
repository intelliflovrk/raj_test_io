from selenium.webdriver.common.by import By
from ioffice.clients.factfind.base import BaseFactFindPage
from selenium.webdriver.support.wait import WebDriverWait
from pageobjects import EC


class BudgetStage(BaseFactFindPage):

    def click_income_subtab(self):
        return self.click(BudgetStage.Locators.INCOME_SUBTAB)

    def click_expenditure_subtab(self):
        return self.click(BudgetStage.Locators.EXPENDITURE_SUBTAB)

    def click_monthly_affordability_subtab(self):
        return self.click(BudgetStage.Locators.MONTHLY_AFFORDABILITY_SUBTAB)

    class Locators(BaseFactFindPage):
        INCOME_SUBTAB = (By.ID, "income")
        EXPENDITURE_SUBTAB = (By.ID, "expenditure")
        MONTHLY_AFFORDABILITY_SUBTAB = (By.ID, "monthlyaffordability")

    class Income(BaseFactFindPage):

        def click_add_button(self):
            return self.click(BudgetStage.Income.Locators.ADD_BUTTON)

        def click_save_button(self):
            return self.click(BudgetStage.Income.Locators.SAVE_BUTTON)

        def get_monthly_total(self):
            return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable
                (BudgetStage.Income.Locators.MONTHLY_TOTAL)).text

        class Locators(BaseFactFindPage):
            DESCRIPTION = (By.XPATH, "//*[@id='109_Description_0']")
            INCOME_AMOUNT = (By.XPATH, "//*[@id='110_Amount_0']")
            FREQUENCY = (By.XPATH, "//*[@id='111_Frequency_0']")
            ADD_BUTTON = (By.LINK_TEXT, "Add")
            SAVE_BUTTON = (By.ID, "ff-form-save")
            MONTHLY_TOTAL = (By.XPATH, "//*[@id='DetailedincomebreakdownTable_0']/tfoot/tr/td[6]")

    class Expenditure(BaseFactFindPage):

        def click_expenditure_yes_button(self):
            return self.click(BudgetStage.Expenditure.Locators.YES_RADIO_BUTTON)

        def click_expenditure_no_button(self):
            return self.click(BudgetStage.Expenditure.Locators.NO_RADIO_BUTTON)

        def fill_in_total_net_monthly_expenditure_field(self, data):
            return self.fill_in_field(BudgetStage.Expenditure.Locators.TOTAL_NET_MONTHLY_EXPENDITURE, data)

        def get_total_monthly_expenditure(self):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located
                (BudgetStage.Expenditure.Locators.TOTAL_MONTHLY_HOUSEHOLD_EXPENDITURE)).get_attribute("value")

        class Locators(BaseFactFindPage):
            YES_RADIO_BUTTON = (By.XPATH, "//*[@id='Yes_ExDetailed_IsDetailed_0']")
            NO_RADIO_BUTTON = (By.XPATH, "//*[@id='No_ExDetailed_IsDetailed_0']")
            RENT_AMOUNT = (By.ID, "ExpenditureGridEssentialItems_0_NetMonthlyAmount")
            CLOTHING_AMOUNT = (By.ID, "ExpenditureGridQualityOfLivingItems_0_NetMonthlyAmount")
            GYM_AMOUNT = (By.ID, "ExpenditureGridNonEssentialItems_0_NetMonthlyAmount")
            PERSONAL_LOAN_AMOUNT = (By.ID, "ExpenditureGridLiabilityItems_0_NetMonthlyAmount")
            TOTAL_MONTHLY_HOUSEHOLD_EXPENDITURE = (By.XPATH, "//*[@id='EcCalculated_TotalExpenditure_0']")
            TOTAL_NET_MONTHLY_EXPENDITURE = (By.XPATH, "//*[@id='ExSummaryTotal_NetMonthlySummaryAmount_0']")

    class MonthlyExpenditure(BaseFactFindPage):

        def get_total_monthly_income(self):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located
                (BudgetStage.MonthlyExpenditure.Locators.TOTAL_MONTHLY_INCOME)).get_attribute("value")

        def get_total_monthly_expenditure(self):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located
                (BudgetStage.MonthlyExpenditure.Locators.TOTAL_MONTHLY_EXPENDITURE)).get_attribute("value")

        def get_total_monthly_disposable_income(self):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located
                (BudgetStage.MonthlyExpenditure.Locators.TOTAL_MONTHLY_DISPOSABLE_INCOME)).get_attribute("value")

        class Locators(BaseFactFindPage):
            TOTAL_MONTHLY_INCOME = (By.XPATH, "//*[@id='AffMonthlyInc_MonthlyIncome_0']")
            TOTAL_MONTHLY_EXPENDITURE = (By.XPATH, "//*[@id='AffMonthlyEx_MonthlyExpenditure_0']")
            TOTAL_MONTHLY_DISPOSABLE_INCOME = (By.XPATH, "//*[@id='AffDisp_MonthlyDispIncome_0']")
