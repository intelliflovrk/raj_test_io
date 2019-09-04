from selenium.common.exceptions import TimeoutException
from dsl.create_client import CreateClient
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.details.base import BaseDetailsPage
from ioffice.clients.details.personal import ViewPersonalPage
from ioffice.reports.base import BaseReportsPage
from ioffice.reports.mi_report import MiReportPage
from ioffice.reports.portfolio_report import PortfolioReportPage
from utils import *


class Reporting(CreateClient):
    def __init__(self, config):
        super().__init__(config)
        self.dialog = {}
        self.page = {}

    def navigate_to_portfolio_report_page(self):
        ClientDashboardPage(self.config).level3_menu().click_reports()
        BaseReportsPage(self.config).click_run_protfolio_report()
        return self

    def navigate_to_personal_tab(self):
        ClientDashboardPage(self.config).level3_menu().click_details()
        BaseDetailsPage(self.config).details_navigation_menu().click_personal_tab()
        return self

    def add_tag_to_client(self):
        client_tag = f"TestAutomationTag{fakedata.rand_int(5)}"
        add_temp_data(self.config, "tag", {"tag": client_tag})
        ViewPersonalPage(self.config)\
            .click_edit_button()\
            .fill_in_tags(client_tag + " ")\
            .click_save_button()
        return self

    def navigate_to_mi_report(self):
        ClientDashboardPage(self.config).level1_menu().hover_over_navigation_menu().click_mi_reports()
        return self

    def go_to_client_list_report(self):
        self.go_to_report(get_common_data(self.config)["test_data"]["mi_report_data"]["report_name"])
        return self

    def go_to_report(self, report_name):
        MiReportPage(self.config)\
            .fill_in_report_name(report_name)\
            .click_filter_button()\
            .click_run_report_link()
        return self

    def download_pdf_report(self):
        MiReportPage(self.config).click_pdf_report()
        return self

    def download_csv_export(self):
        MiReportPage(self.config).click_csv_export()
        return self

    def run_word_report(self):
        PortfolioReportPage(self.config).click_run_word_report()
        return self

    def run_pdf_report(self):
        PortfolioReportPage(self.config).click_run_pdf_report()
        return self

    def verify_mi_reports_downloaded(self):
        time.sleep(30)
        verify_file_is_downloaded(get_download_folder(self.config), "ClientList.csv")
        verify_file_is_downloaded(get_download_folder(self.config), "ClientList.pdf")
        return self

    def verify_portfolio_reports_downloaded(self):
        time.sleep(30)
        verify_file_is_downloaded(get_download_folder(self.config), "PortfolioReport.docx")
        verify_file_is_downloaded(get_download_folder(self.config), "PortfolioReport.pdf")
        return self

    def generate_html_report(self):
        self.navigate_to_mi_report()
        self.go_to_report("UDMI Report")
        MiReportPage(self.config).fill_in_client_tag_name(get_temp_data(self.config, "tag")["tag"]).click_html_import()
        return self

    @retry(TimeoutException, 5)
    def verify_tagged_client_in_html_report(self):
        self.generate_html_report()
        assert MiReportPage(self.config).get_client_first_name() == get_temp_data(
            self.config, "client")["person"]["firstName"], \
            "Client not found in HTML report."
        return self