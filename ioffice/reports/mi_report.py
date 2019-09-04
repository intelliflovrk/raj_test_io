import time
from selenium.webdriver.common.by import By
from ioffice.reports.base import BaseReportsPage


class MiReportPage(BaseReportsPage):

    def fill_in_report_name(self, data):
        return self.clear_and_fill_in_field(self.Locators.REPORT_NAME, data)

    def click_filter_button(self):
        return self.click(self.Locators.FILTER_BUTTTON)

    def click_run_report_link(self):
        self.wait_until_please_wait_spinner_present()
        return self.click(self.Locators.RUN_REPORT_LINK)

    def click_pdf_report(self):
        return self.click(self.Locators.PDF_REPORT)

    def fill_in_client_tag_name(self, data):
        return self.clear_and_fill_in_field(self.Locators.CLIENT_TAG_NAME_FIELD, data)

    def click_csv_export(self):
        return self.click(self.Locators.CSV_EXPORT)

    def click_html_import(self):
        return self.click(self.Locators.HTML_REPORT)

    def get_client_first_name(self):
        return self.get_text(self.Locators.FIRST_FIRST_NAME_TEXT)

    class Locators(object):
        REPORT_NAME = (By.ID, "id___filterIdentifier")
        FILTER_BUTTTON = (By.XPATH, "//a[@class='jq-filter button button-enabled']")
        RUN_REPORT_LINK = (By.XPATH, "//table[@id='grid_ReportList']/tbody/tr[2]//a[@title='Run Report']")
        PDF_REPORT = (By.ID, "id_root_2_2_3_3")
        HTML_REPORT = (By.XPATH, "//a[contains(text(),'HTML Report')]")
        CSV_EXPORT = (By.ID, "id_root_2_2_3_4")
        CLIENT_TAG_NAME_FIELD = (By.ID, "id_condition_1")
        FIRST_FIRST_NAME_TEXT = (By.CSS_SELECTOR, "tbody tr:nth-of-type(2) td:nth-of-type(2) span")
