from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection,IOFrameDialog


class ChangeStatusDialog(BasePageSection, IOFrameDialog):

    def __init__(self, template_id, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, ChangeStatusDialog.Locators._FRAME.format(template_id))
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_status(self, status):
        self.page.select_by_visible_text(ChangeStatusDialog.Locators.STATUS_SELECT_BOX, status)
        return self

    def click_save(self):
        self.page.click(ChangeStatusDialog.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/WorkflowAdministration/{0}/ChangeStatus']"
        STATUS_SELECT_BOX = (By.ID, "id_Status")
        SAVE_BUTTON = (By.LINK_TEXT, 'Save')
