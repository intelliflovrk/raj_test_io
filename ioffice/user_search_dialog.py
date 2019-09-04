from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection, IOFrameDialog


class UserSearchDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame, popup_control):
        super().__init__(parent_page)
        self.popup_control = popup_control
        self.FRAME = (By.XPATH, UserSearchDialog.Locators._FRAME.format(self.popup_control))
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def fill_in_user(self, user_id):
        self.page.clear_and_fill_in_field(UserSearchDialog.Locators.USER_FIELD, user_id)
        return self

    def click_search(self):
        self.page.click(UserSearchDialog.Locators.SEARCH_BUTTON)
        return self

    def click_clear_button(self):
        self.page.click(UserSearchDialog.Locators.CLEAR_BUTTON)
        return self

    def click_first_result(self):
        self.page.click(UserSearchDialog.Locators.FIRST_RESULT)
        return self

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/User/SearchDialog?popup_control={0}']"
        SEARCH_BUTTON = (By.LINK_TEXT, "Search")
        FIRST_RESULT = (By.XPATH, "//td[@class='first']/a")
        CLEAR_BUTTON = (By.XPATH, "//a[text()='Clear']")
        USER_FIELD = (By.ID, "id_User_UserIdentifier")
