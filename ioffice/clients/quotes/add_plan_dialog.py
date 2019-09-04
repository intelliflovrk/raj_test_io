from ioffice.base import BasePageSection, BasePage, IOFrameDialog
from selenium.webdriver.common.by import By


class AddPlanDialog(BasePageSection, IOFrameDialog, BasePage):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, AddPlanDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_yes_radiobutton(self):
        return self.click(AddPlanDialog.Locators.YES_RADIOBUTTON)

    def click_continue(self):
        self.click(AddPlanDialog.Locators.CONTINUE_BUTTON)
        return self

    class Locators(object):
        _FRAME = "//iframe[contains(@src, 'SubmitOnLineApplication')]"
        YES_RADIOBUTTON = (By.ID, "AddPlanOptions_2")
        CONTINUE_BUTTON = (By.ID, "id_root_2_2_3_3")
