from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from ioffice.clients.factfind.base import BaseFactFindPage
from selenium.webdriver.support import expected_conditions as EC


class EmploymentStage(BaseFactFindPage):

    def click_add_button(self):
        return self.click(EmploymentStage.Locators.ADD_BUTTON)

    def select_employment_status(self, data):
        return self.select_by_visible_text(EmploymentStage.Locators.EMPLOYMENT_STATUS, data)

    def click_save_button(self):
        return self.click(EmploymentStage.Locators.SAVE_BUTTON)

    def get_first_life_full_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(EmploymentStage.Locators.FIRST_LIFE_FULL_NAME)).text

    def get_second_life_full_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(EmploymentStage.Locators.SECOND_LIFE_FULL_NAME)).text

    def get_employment_rows_string(self):
        return WebDriverWait(self.driver, self.TIMEOUT)\
            .until(EC.presence_of_all_elements_located(self.Locators.EMPLOYMENT_ROWS))

    class Locators(BaseFactFindPage.Locators):
        EMPLOYMENT_STATUS = (By.ID, "EDStatus_EmploymentStatus_0")
        RETIREMENT_AGE = (By.ID, "EDRetirementAge_IntendedRetirementAge_0")
        EMPLOYMENT_START_DATE = (By.ID, "EDStartDate_StartDate_0")
        EMPLOYMENT_END_DATE = (By.ID, "EDEndDate_EndDate_0")
        EMPLOYER = (By.ID, "EDEmployer_Employer_0")
        GROSS_INCOME = (By.ID, "EDBasicAnnualIncome_BasicAnnualIncome_0")
        ADD_BUTTON = (By.LINK_TEXT, "Add")
        SAVE_BUTTON = (By.ID, "ff-form-save")
        FIRST_LIFE_FULL_NAME = (By.ID, "EDFullName_FullName_0")
        SECOND_LIFE_FULL_NAME = (By.ID, "EDFullName_FullName_1")
        EMPLOYMENT_ROWS = (By.CSS_SELECTOR, "#EmploymentDetailTable_0 tbody")
