import pytest
from dsl.io_store_apps import IOStoreApps


pytestmark = [pytest.mark.iostore, pytest.mark.io_all]


@pytest.mark.usefixtures("api_install_uninstall_app")
@pytest.mark.usefixtures("ui_login_logout")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
def test_installing_app_with_client_menu_item(config):
    test = (IOStoreApps(config)
            .open_client_by_url()
            .open_client_actions_menu()
            .verify_app_link_is_present_in_client_actions_menu("TestAutomationApp")
            )
