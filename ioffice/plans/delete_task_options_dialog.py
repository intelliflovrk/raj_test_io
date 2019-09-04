from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class DeleteTaskOptionsDialog(BasePageSection, IOFrameDialog):

    def __init__(self, client_id, plan_id, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, DeleteTaskOptionsDialog.Locators._FRAME.format(client_id, plan_id))
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_ok(self):
        self.page.click(DeleteTaskOptionsDialog.Locators.OK_BUTTON)
        return self

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/plan/{0}/OpenYesNoDialog/{1}']"
        OK_BUTTON = (By.LINK_TEXT, "Ok")
