from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection, IOFrameDialog
from ioffice.user_search_dialog import UserSearchDialog


class AddNewWorkflowTemplateDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = AddNewWorkflowTemplateDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def fill_in_template_name(self, name):
        self.page.fill_in_field(AddNewWorkflowTemplateDialog.Locators.TEMPLATE_NAME_FIELD, name)
        return self

    def select_related_to(self, related_to_text):
        self.page.select_by_visible_text(AddNewWorkflowTemplateDialog.Locators.RELATED_TO_SELECT_BOX,
                                                related_to_text)
        return self

    def select_category(self, category):
        self.page.select_by_visible_text(AddNewWorkflowTemplateDialog.Locators.CATEGORY_SELECT_BOX, category)
        return self

    def open_user_search_dialog(self):
        self.page.click(AddNewWorkflowTemplateDialog.Locators.USER_SEARCH_BUTTON)
        return UserSearchDialog(self.page, self.frame_locator, "id_OwnerUserPartyId")

    def click_save_button(self):
        self.page.click(AddNewWorkflowTemplateDialog.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        TEMPLATE_NAME_FIELD = (By.ID, "id_Name")
        FRAME = (By.XPATH, "//iframe[@src='/nio/WorkflowAdministration/AddNewWorkflowTemplate']")
        RELATED_TO_SELECT_BOX = (By.ID, "id_RelatedTo")
        CATEGORY_SELECT_BOX = (By.ID, "id_CategoryId")
        USER_SEARCH_BUTTON = (
        By.XPATH, "//*[@id='__display_id_OwnerUserPartyId']//following-sibling::*/a[@class='hpick']")
        SAVE_BUTTON = (By.LINK_TEXT, "Save")
