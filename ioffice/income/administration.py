from ioffice.income.base import IncomeBasePage, By
from ioffice.income.process_manager_dialog import PaymentRunProcessManagerDialog, MonthEndProcessManagerDialog


class IncomeAdministrationBasePage(IncomeBasePage):

    def click_payment_run(self):
        self.click(self.Locators.PAYMENT_RUNS)
        return self

    class Locators(object):
        PAYMENT_RUNS = (By.CSS_SELECTOR, ".menu_node_commissions_administration_paymentruns")


class PaymentRunsPage(IncomeAdministrationBasePage):

    def click_generate_payment_run(self):
        self.click(self.Locators.GENERATE_PAYMENT_RUN)
        return PaymentRunProcessManagerDialog(self)

    def click_close_month_end(self):
        self.click(self.Locators.CLOSE_MONTH_END)
        return MonthEndProcessManagerDialog(self)

    def click_payment_history(self):
        self.click(self.Locators.PAYMENT_HISTORY)
        return self

    def click_period_end_history(self):
        self.click(self.Locators.PERIOD_END_HISTORY)
        return self

    def get_payment_run_date_value(self):
        payment_date, paymetn_time = self.get_text(self.Locators.RUN_DATE_VALUE).split(" ")
        return payment_date

    def get_month_end_description_value(self):
        return self.get_text(self.Locators.DESCRIPTION_VALUE)

    class Locators(object):
        GENERATE_PAYMENT_RUN = (By.XPATH, "//a[contains(text(),'Generate Payment Run')]")
        CLOSE_MONTH_END = (By.XPATH, "//a[contains(text(),'Close Month End')]")
        RUN_DATE_VALUE = (By.CSS_SELECTOR, "tbody tr:nth-of-type(1) .first")
        PAYMENT_HISTORY = (By.CSS_SELECTOR, ".ux-ctl-tabs-current .ux-lib-tbody")
        PERIOD_END_HISTORY = (By.CSS_SELECTOR, ".ux-ctl-tabs-normal .ux-lib-tbody")
        DESCRIPTION_VALUE = (By.XPATH, "//*[@id='grid_id_root_2_2_3_3_2']/tbody/tr[1]/td[2]")