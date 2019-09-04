import pytest

from dsl.client_relationship import AddRelationship
from dsl.create_client import *
from dsl.create_client_quick import AddClientQuick

pytestmark = [pytest.mark.client, pytest.mark.io_all]


@pytest.mark.usefixtures("api_delete_client_contact")
@pytest.mark.usefixtures("api_delete_client_address")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_basic_client(config):
    """ Test Description: Add a client with basic details and verify it in summary. """
    test = (CreateClient(config)
            .using_add_client_wizard()
                .add_basic_client_details()
                .add_address()
                .add_contact()
                .finish()
            .open_created_client_by_search()
            .navigate_to_summary_tab()
                .verify_address_and_contacts_added()
            )


@pytest.mark.usefixtures("ui_login_logout")
def test_add_basic_client_quick(config):
    """ Test Description: Adding a basic client by using Quick Add Client link
    and verifying that the client is saved and can be located in the search. """
    test = (AddClientQuick(config)
            .using_quick_add_client_form()
                .add_basic_client_details()
                .add_client_address_details()
                .add_client_contact_details()
                .select_adviser()
                .add_client_notes()
                .save()
            .search_for_client()
                .verify_client_created()
            .navigate_to_details()
            .navigate_to_personal_tab()
                .verify_client_personal_details_saved()
            .navigate_to_addresses_tab()
                .verify_client_address_details_saved()
            .navigate_to_contact_tab()
                .verify_client_contact_details_saved()
            .navigate_to_notes_tab()
                .verify_client_note_details_saved()
            )


@pytest.mark.usefixtures("api_delete_client_relationship")
@pytest.mark.usefixtures("ui_login_logout")
def test_create_corporate_client_and_relationship(config):
    """ Test Description: Add corporate client with relationship and verify """
    test = (AddRelationship(config)
            .using_add_client_wizard()
                .add_basic_corporate_client()
                .finish_corporate()
            .using_add_relationship_wizard()
                .add_employee_relationship()
                .finish()
            .verify_corporate_client_relationship()
            )