from selenium.webdriver.common.by import By
from ioffice.clients.factfind.base import BaseFactFindPage


class MortgageStage(BaseFactFindPage):

    def click_existing_provision_subtab(self):
        return self.click(MortgageStage.Locators.EXISTING_PROVISION_SUBTAB)

    def click_property_details_subtab(self):
        return self.click(MortgageStage.Locators.PROPERTY_DETAILS_SUBTAB)

    def click_requirements_subtab(self):
        return self.click(MortgageStage.Locators.REQUIREMENTS_SUBTAB)

    def click_preferences_and_risk_subtab(self):
        return self.click(MortgageStage.Locators.PREFERENCES_AND_RISK_SUBTAB)

    def click_checklist_subtab(self):
        return self.click(MortgageStage.Locators.CHECKLIST_SUBTAB)

    def click_form_save_button(self):
        return self.click(MortgageStage.Locators.SAVE_BUTTON)

    class Locators(object):
        EXISTING_PROVISION_SUBTAB = (By.ID, "mortgageprovision")
        PROPERTY_DETAILS_SUBTAB = (By.ID, "propertydetails")
        REQUIREMENTS_SUBTAB = (By.ID, "mortgagerequirements")
        PREFERENCES_AND_RISK_SUBTAB = (By.ID, "mortgagepreferences")
        CHECKLIST_SUBTAB = (By.ID, "checklist")
        SAVE_BUTTON = (By.ID, "ff-form-save")

    class ExistingProvision(BaseFactFindPage):

        def click_yes_radiobutton(self):
            return self.click(MortgageStage.ExistingProvision.Locators.YES_RADIOBUTTON)

        def click_add_button(self):
            return self.click(MortgageStage.ExistingProvision.Locators.ADD_BUTTON)

        class Locators(object):
            ADD_BUTTON = (By.XPATH, "//*[@id='46792_grid_0']/a")
            YES_RADIOBUTTON = (By.XPATH, "//*[@id='Yes_880_HasExistingProvision_0']")
            LENDER = (By.ID, "884_Provider_0")
            RATE_TYPE = (By.ID, "891_MortgageType_0")
            MORTGAGE_TYPE = (By.ID, "887_RefPlanType2ProdSubTypeId_0")
            REPAYMENT_METHOD = (By.ID, "886_RepaymentMethod_0")
            START_DATE = (By.ID, "895_StartDate_0")
            END_DATE = (By.ID, "896_MaturityDate_0")
            CAPITAL_REPAYMENT_AMOUNT = (By.ID, "890_RepaymentAmount_0")
            VALUE_OF_PROPERTY = (By.ID, "PropertyValue_ValueOfProperty_0")
            MONTHLY_REPAYMENT_AMOUNT = (By.ID, "890a_MonthlyRepaymentAmount_0")
            ORIGINAL_MORTGAGE_TERM = (By.ID, "894_MortgageTerm_0")
            CURRENT_BALANCE = (By.ID, "898_CurrentBalance_0")

    class PropertyDetails(BaseFactFindPage):

        def click_add_button(self):
            return self.click(MortgageStage.PropertyDetails.Locators.ADD_BUTTON)

        class Locators(object):
            ADD_BUTTON = (By.XPATH, "//*[@id='propertydetail_grid_0']/a")
            ADDRESSLINE_1 = (By.ID, "PDLine1_AddressLine1_0")
            ADDRESSLINE_2 = (By.ID, "PDLine2_AddressLine2_0")
            ADDRESSLINE_3 = (By.ID, "PDLine3_AddressLine3_0")
            ADDRESSLINE_4 = (By.ID, "PDLine4_AddressLine4_0")

    class Requirements(BaseFactFindPage):

        def click_add_button(self):
            return self.click(MortgageStage.Requirements.Locators.ADD_BUTTON)

        class Locators(object):
            ADD_BUTTON = (By.XPATH, "//*[@id='41672_grid_0']/a")
            MORTGAGE_TYPE = (By.ID, "RefOpportunityType2ProdSubTypeId_RefOpportunityType2ProdSubTypeId_0")
            PRICE_VALUATION = (By.ID, "Price_Price_0")
            DEPOSIT_EQUITY = (By.ID, "Deposit_Deposit_0")

    class PreferencesAndRisk(BaseFactFindPage):

        def click_radiobutton(self):
            return self.click(MortgageStage.PreferencesAndRisk.Locators.RADIOBUTTON)

        class Locators(object):
            RADIOBUTTON = (By.XPATH, "//*[@id='No_riskMortgRepaid_RiskMortgRepaid_0']")
