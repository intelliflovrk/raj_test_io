import utils
from dsl.search import SearchUser
from ioffice.admin.manageusers.user.base import BaseUserPage
from ioffice.admin.manageusers.user.add_delegate_dialog import AddDelegateDialog
from ioffice.admin.manageusers.user.user_search_dialog import UserSearchDialog
from ioffice.admin.manageusers.user.delegates import DelegatesPage
from dsl.login_to_io import *
from ioffice.base import IOBasePage
from ioffice.delegate_in_dialog import DelegateInDialog
from ioffice.select_delegate_dialog import SelectDelegateDialog
from identity.login import LoginPage
from ioffice.home import HomePage
from ioffice.userdashboard import UserDashboardPage
from utils import *


class SetUpUserDelegation(SearchUser, LogIn):
    def __init__(self, config):
        super().__init__(config)
        self.dialog = {}
        self.page = {}
        self.journey = {}

    def using_add_delegate_dialog(self):
        user = BaseUserPage(self.config)
        user.user_actions_menu().hover_over_user_actions_menu().click_add_delegate()
        self.user_id = user.get_user_id()
        self.dialog = SetUpUserDelegation._AddDelegateJourney(self.user_id, user, self)
        return self.dialog

    def navigate_to_delegate_tab(self):
        BaseUserPage(self.config).level4_menu().click_delegates_tab()
        return self

    def remove_delegate_from_user_account(self):
        DelegatesPage(self.config).click_first_result_checkbox().click_delete_button()\
            .click_ok_in_browser_confirmation_dialog()
        return self

    def remove_previous_delegate_user(self):
        self.navigate_to_delegate_tab().remove_delegate_from_user_account()
        return self

    def navigate_to_home_page(self):
        HomePage(self.config) \
            .load() \
            .click_login()
        return self

    def using_delegate_in_dialog(self):
        UserDashboardPage(self.config).level1_menu().hover_over_user_navigation_menu().click_delegate_in()
        self.dialog = SetUpUserDelegation._DelegateIntoAccount(UserDashboardPage(self.config), self)
        return self.dialog

    def assert_user_is_delegated_in(self):
        usermenutext = IOBasePage(self.config).get_selected_area_text()
        list = usermenutext.split()
        assert str(list[0]) == "Delegated", "User is not delegated in"
        assert str(list[1]) == "as:", "User is not delegated in"
        return self

    class _AddDelegateJourney:
        def __init__(self, user_id, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddDelegateDialog(user_id, current_page)

        def search_for_user(self):
            dialog = self.dialog.open_user_search_dialog()
            data = utils.get_common_data(self.config)["advisers"]
            usersearch = UserSearchDialog(self.dialog, dialog.FRAME, "id_Party_Id").click_clear_button()
            time.sleep(5)
            usersearch.fill_in_user_firstname_field(data["delegation_user"]["first_name"])\
                .fill_in_user_lastname_field(data["delegation_user"]["last_name"])\
                .click_search()\
                .click_first_result()
            return self

        def click_save_button(self):
            self.dialog = AddDelegateDialog(self.config.user_id, self.dialog)
            time.sleep(5)
            self.dialog.click_save_button()
            return self.journey

    class _DelegateIntoAccount:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = DelegateInDialog(current_page)

        def search_for_delegate_user(self):
            dialog = self.dialog.open_delegate_search_dialog()
            SelectDelegateDialog(self.dialog, dialog.FRAME, "id_DelegatePartyId").click_first_result()
            return self

        def click_delegate_in_button(self):
            self.dialog = DelegateInDialog(self.dialog, self.dialog)
            time.sleep(5)
            self.dialog.click_delegate_in_button()
            return self

        def enter_delegation_user_password(self):
            LoginPage(self.config) \
                .fill_in_password_field(get_user_by_type(self.config, "delegate_user")["password"]) \
                .click_login_button()
            return self.journey
