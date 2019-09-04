import pytest
from dsl.data_uploader import DataUpload

pytestmark = [pytest.mark.datauploader, pytest.mark.io_all]


@pytest.mark.lead
@pytest.mark.usefixtures("file_delete_leads_import_csv")
@pytest.mark.usefixtures("ui_login_logout")
def test_download_leads_template(config):
    """ Download import leads template and verify"""
    test = (DataUpload(config)
            .using_download_template_dialog()
                .download_import_leads_template()
            .verify_documents_downloaded()
            )


@pytest.mark.skipif('tst' in pytest.config.option.env, reason='IP-56831')
@pytest.mark.lead
@pytest.mark.usefixtures("api_delete_lead")
@pytest.mark.usefixtures("ui_login_logout")
def test_upload_leads_template(config):
    """ Upload completed template and verify data synced"""
    test = (DataUpload(config)
            .using_import_completed_template_dialog()
                .upload_template("Import Leads")
                .verify_uploaded_file()
            .navigate_to_lead_page()
            .search_and_open_lead()
                .verify_uploaded_data_synced()
            )