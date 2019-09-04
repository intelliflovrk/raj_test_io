import pytest
from dsl.set_up_user_delegation import *

pytestmark = [pytest.mark.delegation, pytest.mark.io_all]


@pytest.mark.usefixtures("ui_remove_delegate_from_user_account")
@pytest.mark.usefixtures("ui_login_logout")
def test_user_delegation(config):
    """ Test Description: Configuring a user to have delegation permissions and then checking that the
     user can delegate into another user's account"""
    test = (SetUpUserDelegation(config)
                .navigate_to_manage_users()
                    .find_user()
                .using_add_delegate_dialog()
                    .search_for_user()
                    .click_save_button()
                .logout()
                .navigate_to_home_page()
                .login_as("delegate_user")
                .using_delegate_in_dialog()
                    .search_for_delegate_user()
                    .click_delegate_in_button()
                .enter_delegation_user_password()
                .assert_user_is_delegated_in()
            )