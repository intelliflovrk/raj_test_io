from ioffice.base import BasePageSection, BasePage, IOFrameDialog
from selenium.webdriver.common.by import By


class UserSearchDialog(BasePageSection, IOFrameDialog, BasePage):
    def __init__(self, parent_page, current_frame,  popup_control):
        super().__init__(parent_page)
        self.popup_control = popup_control
        self.FRAME = (By.XPATH, UserSearchDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_search(self):
        return self.click(UserSearchDialog.Locators.SEARCH_BUTTON)

    def click_first_result(self):
        return self.click(UserSearchDialog.Locators.FIRST_RESULT)

    def click_clear_button(self):
        return self.click(UserSearchDialog.Locators.CLEAR_BUTTON)

    def fill_in_user_firstname_field(self, data):
        return self.fill_in_field(UserSearchDialog.Locators.FIRST_NAME, data)

    def fill_in_user_lastname_field(self, data):
        return self.fill_in_field(UserSearchDialog.Locators.LAST_NAME, data)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/User/SearchDialog?popup_control=id_Party_Id']"
        FIRST_NAME = (By.CSS_SELECTOR, "#id_User_FirstName")
        LAST_NAME = (By.CSS_SELECTOR, "#id_User_LastName")
        CLEAR_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_2_2_2 > div > div.ux-ctl-search-options > a:nth-child(3)")
        SEARCH_BUTTON = (By.CSS_SELECTOR, "#form_id_root_2_2_2_2_2 > div.actions.ux-ctl-form-actions > div > a")
        FIRST_RESULT = (By.XPATH, "//td[@class='first']/a")
