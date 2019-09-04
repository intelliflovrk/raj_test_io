import time
from pfp.wizard import BaseWizardStage, BaseWizardPage
from pageobjects import BasePageSection
from selenium.webdriver.common.by import By


class EmploymentWizard(BaseWizardPage):

    def click_add_current_employment_record(self):
        time.sleep(1)
        self.click(self.Locators.ADD_CURRENT_EMPLOYMENT_RECORD_BUTTON)
        return self

    def employment_title_stage(self):
        return self.EmploymentTitleStage(self)

    def occupation_stage(self):
        return self.OccupationStage(self)

    def employer_stage(self):
        return self.EmployerStage(self)

    def date_stage(self):
        return self.DateStage(self)

    def income_stage(self):
        return self.IncomeStage(self)

    def overtime_stage(self):
        return self.OvertimeStage(self)

    def bonus_stage(self):
        return self.BonusStage(self)

    def review_stage(self):
        return self.ReviewStage(self)

    def click_save_and_close(self):
        time.sleep(1)
        self.click(self.Locators.SAVE_AND_CLOSE_BUTTON)
        return self

    class Locators(object):
        ADD_CURRENT_EMPLOYMENT_RECORD_BUTTON = (By.CSS_SELECTOR, "button[title*='Add Current Employment']")
        SAVE_AND_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[title*='Save & Close']")

    class EmploymentTitleStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__('Employment status', parent_page)

        def select_job_title(self, data):
            self.page.select_by_visible_text(self.Locators.JOB_TITLE_SELECT_BOX, data)
            return self

        class Locators(object):
            JOB_TITLE_SELECT_BOX = (By.CSS_SELECTOR, ".validation-wrap > div >select")

    class OccupationStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__('Occupation', parent_page)

        def fill_in_occupation(self, data):
            self.page.clear_and_fill_in_field(self.Locators.OCCUPATION_FIELD, data)
            return self

        class Locators(object):
            OCCUPATION_FIELD = (By.CSS_SELECTOR, "input[placeholder*='Occupation']")

    class EmployerStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__('Employer', parent_page)

        def fill_in_employer_name(self, data):
            self.page.clear_and_fill_in_field(self.Locators.EMPLOYER_NAME, data)
            return self

        class Locators(object):
            EMPLOYER_NAME = (By.CSS_SELECTOR, "input[placeholder*='Employer name']")

    class DateStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__('Date', parent_page)

        def fill_in_start_date(self, data):
            self.page.clear_and_fill_in_field(self.Locators.START_DATE_FIELD, data)
            return self

        def fill_in_start_month(self, data):
            self.page.fill_in_field(self.Locators.START_MONTH_FIELD, data)
            return self

        def fill_in_start_year(self, data):
            self.page.clear_and_fill_in_field(self.Locators.START_YEAR_FIELD, data)
            return self

        class Locators(object):
            START_DATE_FIELD = (By.XPATH, "//div[3]/div[1]/div/div/div[1]/div/input")
            START_MONTH_FIELD = (By.XPATH, "//div[3]/div[1]/div/div/div[2]/div/input")
            START_YEAR_FIELD = (By.XPATH, "//div[3]/div[1]/div/div/div[3]/div/input")

    class IncomeStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__('Basic annual income', parent_page)

    class OvertimeStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__('Overtime', parent_page)

    class BonusStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__('Bonus', parent_page)

    class ReviewStage(BasePageSection):
        def __init__(self, parent_page):
            super().__init__(parent_page)

        def click_save_and_close_button(self):
            self.page.click(self.Locators.SAVE_AND_CLOSE_BUTTON)
            return self

        class Locators(object):
            SAVE_AND_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[title='Save & Close']")