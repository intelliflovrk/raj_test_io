import pytest
from dsl.export_client_data import ExportClientData

pytestmark = [pytest.mark.dynamic_planner, pytest.mark.io_all]


@pytest.mark.usefixtures("file_delete_client_data_file")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_export_client_data(config):
    """Test Description: Export client data and verify that the file has been downloaded."""
    test = (ExportClientData(config)
            .open_client_by_url()
            .navigate_to_factfind()
            .click_export_client_data()
            .download_client_data()
            .verify_client_data_document_downloaded()
            )
