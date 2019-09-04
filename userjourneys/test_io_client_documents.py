import pytest
from dsl.upload_document import UploadDocument, ClientDocuments

pytestmark = [pytest.mark.document, pytest.mark.client, pytest.mark.io_all]


@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='IP-52890')
@pytest.mark.uploaddocument
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_upload_client_document(config):
    """ Upload pdf document and verify it"""
    test = (UploadDocument(config)
            .open_client_by_url()
            .using_upload_document_dialog()
                .upload_pdf_document()
            .verify_document_uploaded()
            )


@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("ui_create_delete_binder")
@pytest.mark.usefixtures("api_upload_client_document")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_document_to_binder(config):
    """Test Description: Adding a document to a binder and verify it."""
    test = (ClientDocuments(config)
            .open_client_by_url()
            .open_client_documents()
            .add_documents_to_binder()
            .verify_document_added_to_binder()
            )


@pytest.mark.usefixtures("api_upload_client_document")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_delete_document(config):
    """Test Description: Deleting a document and verify it."""
    test = (ClientDocuments(config)
            .open_client_by_url()
            .open_client_documents()
            .delete_documents()
            .verify_documents_deleted()
            )


@pytest.mark.usefixtures("file_delete_test_automation_document")
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("api_upload_client_document")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_open_client_document(config):
    """Test Description: Uploading a pdf document and verify it can be opened."""
    test = (ClientDocuments(config)
            .open_client_by_url()
            .open_client_documents()
            .open_document()
            .verify_document_opened()
            )
