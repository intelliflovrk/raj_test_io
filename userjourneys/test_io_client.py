import pytest
from dsl.client_management import ClientManagement
from dsl.client_merge import MergeClient
from dsl.client_share import ShareClient
from dsl.client_details import *
from dsl.user_tasks import UserTasks
from dsl.client_activities import ClientActivities

pytestmark = [pytest.mark.client, pytest.mark.io_all]


@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_create_mortgage_plan")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_client_merge(config):
    """ Test Description: Merge client and verify. """
    test = (MergeClient(config)
                .open_existing_merge_client()
                .using_merge_client_dialog()
                    .search_for_created_client_to_merge()
                    .merge_created_client_to_existing_client()
                .open_existing_client_plan()
                .verify_created_client_plan_merged()
            )


@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_client_restriction(config):
    """Test Description: Verifies that when restricted, user is not showing up in searches"""
    test = (ClientManagement(config)
            .open_client_by_url()
            .open_restrict_processing()
                .confirm_restriction()
            .search_for_client()
                .verify_client_not_present_in_result()
                .close_search_result_dialog()
            .navigate_to_home()
                .verify_client_not_present_in_recent_clients()
            )


@pytest.mark.usefixtures("ui_logout_login")
@pytest.mark.usefixtures("ui_delete_client_open_activities")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_client_share(config):
    """ Test Description: Share a client with other user/adviser and verify the entry."""
    test = (ShareClient(config)
            .open_client_by_url()
            .using_client_share_dialog()
                .fill_in_client_share_dialog()
            .logout()
            .login_as("clientshare_user")
            .open_client_by_url()
                .verify_access_to_shared_client()
            .navigate_to_client_open_activities()
                .verify_task_assigned_to_client_share_adviser()
            )


@pytest.mark.organiser
@pytest.mark.usefixtures("ui_delete_user_open_tasks")
@pytest.mark.usefixtures("api_create_task")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_logout")
def test_view_user_task(config):
    """ Test Description: Create a client task, assign it to a user and verify it can be viewed in the user tasks."""
    test = (UserTasks(config)
            .login_as("task_user")
            .navigate_to_home()
            .navigate_my_dashboard()
            .open_my_tasks_widget()
                .change_date_filter()
                .verify_task_exists_in_user_tasks()
            )


@pytest.mark.organiser
@pytest.mark.usefixtures("ui_delete_user_open_tasks")
@pytest.mark.usefixtures("api_create_task")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_logout")
def test_quick_task_view(config):
    """ Test Description: Create a client task, assign it to a user and verify it can be viewed from a widget"""
    test = (UserTasks(config)
            .login_as("task_user")
            .navigate_to_home()
            .navigate_my_dashboard()
            .using_activity_dialog()
                .verify_task_details_in_activity_dialog()
                .close_activity_dialog()
            )


@pytest.mark.usefixtures("api_delete_client_address")
@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_client_address(config):
    """ Test Description: Create an address for a client and verify the address is saved. """
    test = (ClientDetails(config)
            .open_client_by_url()
            .navigate_to_details()
            .navigate_to_addresses_tab()
            .using_add_address_dialog()
                .add_address_details()
            .verify_client_address_details_saved()
            )


@pytest.mark.usefixtures("api_create_client")
@pytest.mark.usefixtures("ui_login_logout")
def test_edit_client_details(config):
    """ Test Description: Verify that it is possible to edit client servicing and personal details. """
    test = (ClientDetails(config)
            .open_client_by_url()
            .navigate_to_details()
            .navigate_to_summary_tab()
                .edit_servicing_details()
                .verify_service_status()
            .navigate_to_personal_tab()
                .edit_personal_details()
                .verify_ni_number())


@pytest.mark.usefixtures("api_add_client_address")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_delete_client_address(config):
    """ Test Description: Delete an address for a client and verify the address deleted. """
    test = (ClientDetails(config)
            .open_client_by_url()
            .navigate_to_details()
            .navigate_to_addresses_tab()
                .delete_client_address()
                .verify_client_address_details_deleted()
            )


@pytest.mark.organiser
@pytest.mark.usefixtures("ui_delete_client_open_activities")
@pytest.mark.usefixtures("api_delete_client_address")
@pytest.mark.usefixtures("api_delete_client_contact")
@pytest.mark.usefixtures("api_add_client_contact")
@pytest.mark.usefixtures("api_add_client_address")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_add_client_task(config):
    """ Test Description: Verify that it is possible to add a task and a note to the task."""
    test = (ClientActivities(config)
            .open_client_by_url()
            .using_add_client_task_dialog()
                .add_task_details()
                .save_task()
            .show_all_tasks_and_appts()
            .open_task()
                .add_task_note()
                .verify_task_details()
            )


@pytest.mark.usefixtures("api_delete_client_address")
@pytest.mark.usefixtures("api_add_client_address")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_edit_client_address(config):
    """ Test Description: Edit an address for a client and verify the address details updated. """
    test = (ClientDetails(config)
            .open_client_by_url()
            .navigate_to_details()
            .navigate_to_addresses_tab()
                .edit_client_address_line_1_and_postcode()
                .verify_client_address_details_updated()
            )


@pytest.mark.organiser
@pytest.mark.usefixtures("api_delete_client_documents")
@pytest.mark.usefixtures("ui_delete_client_open_activities")
@pytest.mark.usefixtures("api_create_task")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_upload_task_document(config):
    """ Test Description: Upload document to a task and verify it"""
    test = (ClientActivities(config)
            .open_task_by_url()
            .using_task_upload_document_dialog()
                .upload_task_document()
            .navigate_to_task_documents()
                .verify_task_documents_uploaded()
            )
