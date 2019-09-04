from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection, IOFrameDialog


class AddNewStepDialog(BasePageSection, IOFrameDialog):

    def __init__(self, template_id, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, AddNewStepDialog.Locators._FRAME.format(template_id))
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select_step_type(self, step):
        self.page.select_by_visible_text(AddNewStepDialog.Locators.SELECT_STEP_SELECT_BOX, step)
        return self

    def select_first_task_category(self):
        self.page.select_by_index(AddNewStepDialog.Locators.TASK_CATEGORY_SELECT_BOX, 0)
        return self

    def select_first_task_type(self):
        self.page.select_by_index(AddNewStepDialog.Locators.TASK_TYPE_SELECT_BOX, 0)
        return self

    def select_transition_to_next_step_when(self, indicator):
        self.page.select_by_visible_text(AddNewStepDialog.Locators.TRANSITION_TO_SELECT_BOX, indicator)
        return self

    def select_assign_to(self, who_value):
        self.page.select_by_visible_text(AddNewStepDialog.Locators.ASSIGN_TO_SELECT_BOX, who_value)
        return self

    # method can be used only if 'assign to = Context Role'
    def select_context_role(self, context_role):
        self.page.select_by_visible_text(AddNewStepDialog.Locators.CONTEXT_ROLE_SELECT_BOX, context_role)
        return self

    def click_add(self):
        self.page.click(AddNewStepDialog.Locators.ADD_BUTTON)
        return self

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/WorkflowAdministration/{0}/AddNewStep']"
        SELECT_STEP_SELECT_BOX = (By.NAME, "StepType")
        TASK_CATEGORY_SELECT_BOX = (By.ID, "activityCategories")
        TASK_TYPE_SELECT_BOX = (By.ID, "ActivityCategoryId")
        TRANSITION_TO_SELECT_BOX = (By.ID, "id_TransitionState")
        ASSIGN_TO_SELECT_BOX = (By.ID, "assignedToSelector")
        CONTEXT_ROLE_SELECT_BOX = (By.ID, "roleContextSelector")
        ADD_BUTTON = (By.LINK_TEXT, 'Add')
