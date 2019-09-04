from selenium.webdriver.common.by import By
from ioffice.clients.factfind.base import BaseFactFindPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class RetirementStage(BaseFactFindPage):

    def click_goals_subtab(self):
        return self.click(RetirementStage.Locators.GOALS_SUBTAB)

    def click_eligibility_and_entitlement_subtab(self):
        return self.click(RetirementStage.Locators.ELIGIBILITY_AND_ENTITLEMENT_SUBTAB)

    def click_final_salary_subtab(self):
        return self.click(RetirementStage.Locators.FINAL_SALARY_SUBTAB)

    def click_money_purchase_subtab(self):
        return self.click(RetirementStage.Locators.MONEY_PURCHASE_SUBTAB)

    def click_personal_pensions_subtab(self):
        return self.click(RetirementStage.Locators.PERSONAL_PENSIONS_SUBTAB)

    def click_annuities_subtab(self):
        return self.click(RetirementStage.Locators.ANNUITIES_SUBTAB)

    def click_next_steps_subtab(self):
        return self.click(RetirementStage.Locators.NEXT_STEPS_SUBTAB)

    class Locators(BaseFactFindPage):
        GOALS_SUBTAB = (By.ID, "RetirementGoals")
        ELIGIBILITY_AND_ENTITLEMENT_SUBTAB = (By.ID, "ExistingRetirementProvision")
        FINAL_SALARY_SUBTAB = (By.ID, "finalsalaryschemes")
        MONEY_PURCHASE_SUBTAB = (By.ID, "moneypurchaseschemes")
        PERSONAL_PENSIONS_SUBTAB = (By.ID, "personalpensions")
        ANNUITIES_SUBTAB = (By.ID, "annuities")
        NEXT_STEPS_SUBTAB = (By.ID, "retirementnextsteps")

    class Goals(BaseFactFindPage):

        def click_add_button(self):
            return self.click(RetirementStage.Goals.Locators.ADD_BUTTON)

        def click_save_button(self):
            return self.click(RetirementStage.Goals.Locators.SAVE_BUTTON)

        class Locators(BaseFactFindPage.Locators):
            ADD_BUTTON = (By.XPATH, "//*[@id='50755_grid_0']/a")
            SAVE_BUTTON = (By.ID, "ff-form-save")
            GOAL_TYPE = (By.ID, "GoalTypeRetirement_GoalType_0")
            GOAL_DESCRIPTION = (By.ID, "Objective_Objective_0")
            TARGET_AMOUNT = (By.ID, "TargetAmount_TargetAmount_0")
            TARGET_AGE = (By.ID, "RetirementAge_RetirementAge_0")
            DETAILS_NOTES = (By.ID, "Details_Details_0")
            START_DATE = (By.ID, "StartDate_StartDate_0")

    class Eligibility(BaseFactFindPage):

        def click_pension_scheme_radiobutton_yes(self):
            return self.click(RetirementStage.Eligibility.Locators.PENSION_SCHEME_RADIOBUTTON_YES)

        def click_member_radiobutton_yes(self):
            return self.click(RetirementStage.Eligibility.Locators.MEMBER_RADIOBUTTON_YES)

        def click_add_button(self):
            return self.click(RetirementStage.Eligibility.Locators.ADD_BUTTON)

        def click_save_button(self):
            return self.click(BaseFactFindPage.Locators.SAVE_BUTTON)

        class Locators(BaseFactFindPage.Locators):
            PENSION_SCHEME_RADIOBUTTON_YES = (By.ID, "Yes_595_EmployerHasPensionSchemeFg_0")
            MEMBER_RADIOBUTTON_YES = (By.ID, "Yes_596_MemberOfEmployerPensionSchemeFg_0")
            RETIREMENT_AGE = (By.ID, "StatePensionRetirementAge_StatePensionRetirementAge_0")
            BASIC_PENSION = (By.ID, "BasicStatePension_BasicStatePension_0")
            PENSION_CREDIT = (By.ID, "PensionCredit_PensionCredit_0")
            NOTES = (By.ID, "Notes_Notes_0")
            ADD_BUTTON = (By.LINK_TEXT, "Add")
            SAVE_BUTTON = (By.ID, "ff-form-savebar")

    class FinalSalary(BaseFactFindPage):

        def click_existing_schemes_radiobutton_yes(self):
            return self.click(RetirementStage.FinalSalary.Locators.EXISTING_SCHEME_RADIOBUTTON_YES)

        def click_save_button(self):
            return self.click(BaseFactFindPage.Locators.SAVE_BUTTON)

        class Locators(BaseFactFindPage.Locators):
            EXISTING_SCHEME_RADIOBUTTON_YES = (By.ID, "Yes_600_HasExistingSchemesFg_0")
            SAVE_BUTTON = (By.ID, "ff-form-savebar")

    class MoneyPurchase(BaseFactFindPage):

        def click_existing_schemes_radiobutton_yes(self):
            return self.click(RetirementStage.MoneyPurchase.Locators.EXISTING_SCHEME_RADIOBUTTON_YES)

        def click_save_button(self):
            return self.click(BaseFactFindPage.Locators.SAVE_BUTTON)

        class Locators(BaseFactFindPage.Locators):
            EXISTING_SCHEME_RADIOBUTTON_YES = (By.ID, "Yes_591_ExistingMoneyPurchaseSchemes_0")
            SAVE_BUTTON = (By.ID, "ff-form-savebar")

    class PersonalPensions(BaseFactFindPage):

        def click_existing_schemes_radiobutton_yes(self):
            return self.click(RetirementStage.PersonalPensions.Locators.EXISTING_SCHEME_RADIOBUTTON_YES)

        def click_save_button(self):
            return self.click(BaseFactFindPage.Locators.SAVE_BUTTON)

        class Locators(BaseFactFindPage.Locators):
            EXISTING_SCHEME_RADIOBUTTON_YES = (By.ID, "Yes_HasPersonalPensions_HasPersonalPensions_0")
            SAVE_BUTTON = (By.ID, "ff-form-savebar")

    class Annuities(BaseFactFindPage):

        def click_existing_schemes_radiobutton_yes(self):
            return self.click(RetirementStage.Annuities.Locators.EXISTING_SCHEME_RADIOBUTTON_YES)

        def click_save_button(self):
            return self.click(BaseFactFindPage.Locators.SAVE_BUTTON)

        class Locators(BaseFactFindPage.Locators):
            EXISTING_SCHEME_RADIOBUTTON_YES = (By.ID, "Yes_HasAnnuities_HasAnnuities_0")
            SAVE_BUTTON = (By.ID, "ff-form-savebar")

    class NextSteps(BaseFactFindPage):

        def get_retirement_goals_str_list(self):
            textlist = []
            data = RetirementStage(self.config).NextSteps.get_data_table_rows(self)
            for item in data:
                textlist.append(item.text)
            return textlist

        def get_data_table_rows(self):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(RetirementStage.NextSteps.Locators.TABLE_ROW))
            return self.driver.find_elements_by_css_selector("#sidebar-container table tbody tr:not(.filter)")

        def is_string_present(self, dataset, string):
            result = False
            for item in dataset:
                if string in item:
                    result = True
            return result

        class Locators(BaseFactFindPage.Locators):

            TABLE_ROW = (By.CSS_SELECTOR, "#sidebar-container table tbody tr:not(.filter)")
