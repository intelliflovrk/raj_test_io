from ioffice.wizard import *
from ioffice.admin.manageusers.user.user_search_dialog import *


class AddDelegateDialog(BasePageSection, IOFrameDialog, BasePage):
    def __init__(self, user_id, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, AddDelegateDialog.Locators._FRAME.format(user_id))
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def open_user_search_dialog(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AddDelegateDialog.Locators.SEARCH)).click()
        return UserSearchDialog(self, self.frame_locator, "id_Party_Id")

    def click_save_button(self):
        return self.page.click(AddDelegateDialog.Locators.SAVE)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/user/{0}/adddelegate']"
        SEARCH = (By.CSS_SELECTOR, "#id_root_2_2_2_2 > div.formgroupbody > div > div > span > div > a.hpick")
        SAVE = (By.ID, "id_root_2_2_2_3")
