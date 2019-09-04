from selenium.webdriver.common.by import By

from ioffice.reports.base import BaseReportsPage


class PortfolioReportPage(BaseReportsPage):

    def click_run_pdf_report(self):
        return self.click(PortfolioReportPage.Locators.RUN_PDF_REPORT)

    def click_run_word_report(self):
        return self.click(PortfolioReportPage.Locators.RUN_WORD_REPORT)

    class Locators(object):
        RUN_PDF_REPORT = (By.ID, "pdfButton")
        RUN_WORD_REPORT = (By.ID, "wordButton")