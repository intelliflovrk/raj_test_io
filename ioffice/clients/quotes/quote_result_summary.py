import re

from selenium.webdriver.common.by import By
from ioffice.clients.quotes.quote_result_base import QuoteResultBasePage


class QuoteResultSummaryPage(QuoteResultBasePage):

    def click_add_plan(self):
        return self.click(QuoteResultSummaryPage.Locators.ADD_PLAN_BUTTON)

    def click_docs_button(self):
        return self.click(QuoteResultSummaryPage.Locators.DOCS_BUTTON)

    def click_details_button(self):
        return self.click(QuoteResultSummaryPage.Locators.DETAILS_BUTTON)

    def get_first_column_name(self):
        return self.get_text(QuoteResultSummaryPage.Locators.QUOTE_RESULT_FIRST_COLUMN)

    def get_second_column_name(self):
        return self.get_text(QuoteResultSummaryPage.Locators.QUOTE_RESULT_SECOND_COLUMN)

    def get_second_column_value(self):
        return self.get_text(QuoteResultSummaryPage.Locators.QUOTE_RESULT_SECOND_COLUMN_CELL)

    def get_third_column_name(self):
        return self.get_text(QuoteResultSummaryPage.Locators.QUOTE_RESULT_THIRD_COLUMN)

    def get_third_column_value(self):
        return self.get_text(QuoteResultSummaryPage.Locators.QUOTE_RESULT_THIRD_COLUMN_CELL)

    def get_forth_column_name(self):
        return self.get_text(QuoteResultSummaryPage.Locators.QUOTE_RESULT_FORTH_COLUMN)

    def get_forth_column_value(self):
        return self.get_text(QuoteResultSummaryPage.Locators.QUOTE_RESULT_FORTH_COLUMN_CELL)

    def get_fifth_column_name(self):
        return self.get_text(QuoteResultSummaryPage.Locators.QUOTE_RESULT_FIFTH_COLUMN)

    def get_quote_id_from_url(self):
        return re.search(r'(?<=QuoteResultSummary/)\d+', self.driver.current_url, flags=re.IGNORECASE).group(0)

    def get_joint_state(self):
        return self.get_text(QuoteResultSummaryPage.Locators.FIRST_ROW_JOINT_TEXT)

    class Locators(object):
        DOCS_BUTTON = (By.XPATH, "//*[starts-with(@id, 'ProductGrid')]/td[6]/a")
        DETAILS_BUTTON = (By.XPATH, "//*[starts-with(@id, 'ProductGrid')]/td[7]/a")
        ADD_PLAN_BUTTON = (By.XPATH, "//*[starts-with(@id, 'ProductGrid')]/td[8]/a")
        QUOTE_RESULT_FIRST_COLUMN = (By.XPATH, "//*[starts-with(@id, 'grid_ProductGrid')]/thead/tr/th[1]")
        QUOTE_RESULT_FIRST_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'ProductGrid')]/td[1]/span")
        QUOTE_RESULT_SECOND_COLUMN = (By.XPATH, "//*[starts-with(@id, 'grid_ProductGrid')]/thead/tr/th[2]")
        QUOTE_RESULT_SECOND_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'ProductGrid')]/td[2]/span")
        QUOTE_RESULT_THIRD_COLUMN = (By.XPATH, "//*[starts-with(@id, 'grid_ProductGrid')]/thead/tr/th[3]")
        QUOTE_RESULT_THIRD_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'ProductGrid')]/td[3]/span")
        QUOTE_RESULT_FORTH_COLUMN = (By.XPATH, "//*[starts-with(@id, 'grid_ProductGrid')]/thead/tr/th[4]")
        QUOTE_RESULT_FORTH_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'ProductGrid')]/td[4]/span")
        QUOTE_RESULT_FIFTH_COLUMN = (By.XPATH, "//*[starts-with(@id, 'grid_ProductGrid')]/thead/tr/th[5]")
        QUOTE_RESULT_FIFTH_COLUMN_CELL = (By.XPATH, "//*[starts-with(@id, 'ProductGrid')]/td[5]/span")
        FIRST_ROW_JOINT_TEXT = (By.XPATH, "//tbody/tr[1]/td[5]/span")
