from ioffice.plans.base import *


class PlanWithdrawalsPage(BasePlanPage):

    def get_withdrawal_id(self):
        return self.get_attribute(self.Locators.FIRST_WITHDRAWAL_ID, "value")

    def select_type(self, data):
        return self.select_by_visible_text(self.Locators.WITHDRAWALS_TYPE, data)

    def fill_in_amount(self, data):
        return self.clear_and_fill_in_field(self.Locators.AMOUNT, data)

    def fill_in_effective_date(self, data):
        return self.clear_and_fill_in_field(self.Locators.EFFECTIVE_DATE, data)

    def click_create(self):
        return self.click(self.Locators.CREATE_BUTTON)

    def get_amount(self):
        return self.get_text(self.Locators.FIRST_AMOUNT)

    def get_effective_date(self):
        return self.get_text(self.Locators.FIRST_EFFECTIVE_DATE)

    class Locators(object):
        WITHDRAWALS_TYPE = (By.CSS_SELECTOR, "#id_RefWithdrawalType1")
        AMOUNT = (By.CSS_SELECTOR, "#id_Amount2")
        EFFECTIVE_DATE = (By.CSS_SELECTOR, "#id_PaymentStartDate2")
        CREATE_BUTTON = (By.XPATH, "//a[contains(text(),'Create')]")
        FIRST_AMOUNT = (By.CSS_SELECTOR, "tbody td:nth-of-type(4) .alignRight")
        FIRST_EFFECTIVE_DATE = (By.CSS_SELECTOR, "tbody tr:nth-of-type(1) td:nth-of-type(7) span")
        FIRST_WITHDRAWAL_ID = (By.XPATH, "//*[@id='grid_ecGrid']//td[1]/input")
