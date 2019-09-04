import pytest
from dsl.reporting import Reporting

pytestmark = [pytest.mark.reports, pytest.mark.io_all]


@pytest.mark.skipif('uat-10' == pytest.config.option.env, reason='Internal Error appears on UAT')
@pytest.mark.usefixtures("file_delete_portfolio_reports")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_portfolio_report(config):
    """Test Description: Verifies that portfolio report can be generated in PDF and Word"""
    test = (
        Reporting(config)
            .open_client_by_url()
            .navigate_to_portfolio_report_page()
            .run_pdf_report()
            .run_word_report()
            .verify_portfolio_reports_downloaded()
    )


@pytest.mark.usefixtures("file_delete_mi_reports")
@pytest.mark.usefixtures("ui_login_logout")
def test_mi_report(config):
    """Test Description: Verifies that MI report can be generated in PDF and CSV"""
    test = (
        Reporting(config)
            .navigate_to_mi_report()
            .go_to_client_list_report()
            .download_pdf_report()
            .download_csv_export()
            .verify_mi_reports_downloaded()
    )


@pytest.mark.tag
@pytest.mark.usefixtures("api_delete_client_tag")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_client_tagging(config):
    """Test Description: Add tag to client and verify client appears in UDMI report"""
    test = (
        Reporting(config)
            .open_client_by_url()
            .navigate_to_personal_tab()
                .add_tag_to_client()
            .verify_tagged_client_in_html_report()
    )