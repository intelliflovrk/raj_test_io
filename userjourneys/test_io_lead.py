import pytest
from pytest import mark
from dsl.convert_lead import ConvertLead
from dsl.create_lead import CreateLead
from dsl.lead_activities import AddLeadTask
from dsl.lead_documents import UploadLeadDocument
from dsl.lead_relationship import AddLeadRelationship

pytestmark = [pytest.mark.lead, pytest.mark.io_all]


@pytest.mark.usefixtures("api_delete_lead")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_basic_lead(config):
    """ Test Description: Adding a basic lead and verifying that the data is saved. """
    test = (CreateLead(config)
            .using_add_lead_wizard()
                .add_basic_lead_details()
                .finish()
            .assert_lead_exists()
            )


@pytest.mark.usefixtures("api_add_lead_address")
@pytest.mark.usefixtures("api_create_lead")
@pytest.mark.usefixtures("ui_login_logout")
def test_convert_lead_to_client(config):
    """ Test Description: Convert a lead to a client and verifying the change """
    test = (ConvertLead(config)
            .navigate_to_lead_page()
            .search_and_open_lead()
            .using_change_status_dialog()
                .convert_lead_to_client()
            .assert_lead_converted_to_client_exists()
            )


@mark.organiser
@pytest.mark.usefixtures("ui_delete_lead_tasks")
@pytest.mark.usefixtures("api_delete_lead")
@pytest.mark.usefixtures("api_create_lead")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_lead_task(config):
    """ Test Description: Add task to lead, open and verify it"""
    test = (AddLeadTask(config)
            .open_created_lead_by_url()
            .using_add_lead_task_dialog()
                .add_lead_task()
            .open_lead_task()
                .verify_lead_task_added()
            )


@pytest.mark.skipif('tst' in pytest.config.option.env, reason='IP-56106')
@pytest.mark.uploaddocument
@pytest.mark.usefixtures("api_delete_lead_documents")
@pytest.mark.usefixtures("api_delete_lead")
@pytest.mark.usefixtures("api_create_lead")
@pytest.mark.usefixtures("ui_login_logout")
def test_upload_lead_document(config):
    """ Test Description: Upload document to a lead and and verify it"""
    test = (UploadLeadDocument(config)
            .open_created_lead_by_url()
            .using_upload_document_dialog()
                .upload_pdf_document()
            .open_document()
            .verify_uploaded_document()
            )


@pytest.mark.usefixtures("api_delete_lead_relationship")
@pytest.mark.usefixtures("api_delete_lead")
@pytest.mark.usefixtures("api_create_lead")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_relationship_to_lead(config):
    """ Test Description: Add relationship to lead and verify it"""
    test = (AddLeadRelationship(config)
            .open_created_lead_by_url()
            .using_add_relationship_wizard()
                .add_relationship_to_lead()
            .navigate_to_relationships()
            .verify_relationship_added()
            )