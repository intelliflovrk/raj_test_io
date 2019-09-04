import datetime
import time
import fakedata
from dsl.io_navigation import MyDashboardNavigation
from ioffice.income.administration import PaymentRunsPage


class IncomeAdministration:

    def __init__(self, config):
        self.config = config

    def navigate_to_payment_run(self):
        MyDashboardNavigation(self.config).income().income_administration_tab().payment_runs_tab()
        return self

    def navigate_to_payment_history(self):
        MyDashboardNavigation(self.config).income() \
            .income_administration_tab().payment_runs_tab().payment_history_tab()
        return self

    def navigate_to_period_end_history(self):
        MyDashboardNavigation(self.config).income() \
            .income_administration_tab().payment_runs_tab().period_end_history_tab()
        return self

    def start_payment_run(self):
        PaymentRunsPage(self.config).click_generate_payment_run()\
            .click_advisers_check_box()\
            .click_introducers_check_box()\
            .click_clients_check_box()\
            .click_staff_check_box()\
            .click_start_button()\
            .click_confirm_button()\
            .close_io_dialog()
        return self

    def run_month_end(self):
        self.config.month_end_description = fakedata.rand_text(6)
        PaymentRunsPage(self.config).click_close_month_end()\
            .fill_in_description_text_box(self.config.month_end_description)\
            .click_start_button()\
            .click_confirm_button()\
            .close_io_dialog()
        return self

    def verify_payment_run_presence_in_payment_history(self):
        assert PaymentRunsPage(self.config).get_payment_run_date_value() == datetime.datetime.today().strftime('%d/%m/%Y'),\
            "Payment run not successful, " \
            "EXPECTED: " + datetime.datetime.today().strftime('%d/%m/%Y') + "  " +\
            "ACTUAL: " + PaymentRunsPage(self.config).get_payment_run_date_value()
        return self

    def verify_month_end_presence_in_period_end_history(self):
        time.sleep(10)
        assert PaymentRunsPage(self.config).get_month_end_description_value() == self.config.month_end_description, \
            "Month end run not successful, " \
            "EXPECTED: " + self.config.month_end_description + "  " +\
            "ACTUAL: " + PaymentRunsPage(self.config).get_month_end_description_value()
        return self
