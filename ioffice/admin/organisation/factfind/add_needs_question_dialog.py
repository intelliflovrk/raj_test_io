from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection, IOFrameDialog


class AddNeedsQuestionDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page):
        super().__init__(parent_page)
        self.driver = parent_page.driver
        self.FRAME = (By.XPATH, AddNeedsQuestionDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self._switch_to_frame()

    def click_group_in_profile_checkbox(self):
        return self.page.click(AddNeedsQuestionDialog.Locators.GROUP_IN_PROFILE_CHECKBOX)

    def click_save_button(self):
        return self.page.click(AddNeedsQuestionDialog.Locators.SAVE_BUTTON)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/FactFind/AddOrEditNeedsQuestion']"
        GROUP_IN_PROFILE_CHECKBOX = (By.CSS_SELECTOR, "#id_IsForProfile")
        QUESTION_TEXT = (By.CSS_SELECTOR, "#id_Question")
        PERSONAL_FF_DROPDOWN_MENU = (By.CSS_SELECTOR, "#PersonalCategoryId")
        CORPORATE_FF_DROPDOWN_MENU = (By.CSS_SELECTOR, "#CorporateCategoryId")
        ORDER = (By. CSS_SELECTOR, "#id_Ordinal")
        TYPE_OF_ANSWER_DROPDOWN_MENU = (By.CSS_SELECTOR, "#ControlTypeId")
        SAVE_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_3_3")
