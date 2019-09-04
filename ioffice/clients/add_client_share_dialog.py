from ioffice.client_share_adviser_search_dialog import ShareClientAdviserSearchDialog
from ioffice.wizard import *
from ioffice.adviser_search_dialog import *
from ioffice.base import BasePageSection


class ShareClientDialog(BasePageSection, IOFrameDialog, IOBasePage):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def open_client_share_adviser_search_dialog(self):
        self.click(ShareClientDialog.Locators.SELECT_ADVISER_BUTTON)
        return ShareClientAdviserSearchDialog(self, self.frame_locator)

    def click_add_button(self):
        self.page.click(ShareClientDialog.Locators.ADD_BUTTON)
        return self

    def fill_in_notes(self, data):
        self.page.fill_in_field(ShareClientDialog.Locators.ADVISER_NOTES_TEXT_BOX, data)
        return self

    def click_create_task_check_box(self):
        self.page.click(self.Locators.CREATE_TASK_CHECK_BOX)
        return self

    class Locators:
        SELECT_ADVISER_BUTTON = (
            By.XPATH, "//*[@id='__display_id_SharedToCrmContactId']//following-sibling::*/a[@class='hpick']")
        FRAME = (By.XPATH, "// iframe[contains( @ src, 'ShareClient')]")
        FULL_NAME = (By.XPATH, "//*[@id='ClientShareGrid__71510']/td[2]/span")
        ADD_BUTTON = (By.XPATH, "//div[@class='ux-ctl-form-action-buttons']//*[@id='id_root_2_2_5_6']")
        ADVISER_NOTES_TEXT_BOX = (By.ID, "id_SingleNote")
        CREATE_TASK_CHECK_BOX = (By.ID, "id_IsAddTask")
