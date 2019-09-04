from ioffice.plans.base import *


class PlanActivitiesPage(BasePlanPage):
    def fill_in_workflow_name_filter(self, workflow_name):
        return self.fill_in_field(PlanActivitiesPage.Locators.WORKFLOW_NAME_FILTER_FIELD, workflow_name)

    def click_filter(self):
        return self.click(PlanActivitiesPage.Locators.FILTER_BUTTON)

    def open_first_workflow(self):
        return self.click(PlanActivitiesPage.Locators.FIRST_WORKFLOW_OPEN_LINK)

    def check_select_all_tasks(self):
        return self.click(PlanActivitiesPage.Locators.SELECT_ALL_TASKS_CHECKBOX)

    def click_delete(self):
        return self.click(PlanActivitiesPage.Locators.DELETE_BUTTON)

    class Locators(object):
        FILTER_BUTTON = (By.XPATH, "//*[@id='WorkflowInstanceGrid__']//a[contains(text(), 'Filter')]")
        FIRST_WORKFLOW_COMPLETED_STATUS = (By.XPATH, "//*[@id='grid_WorkflowInstanceGrid']//tr[2]/td/span[contains(text(), 'Completed')]")
        FIRST_WORKFLOW_OPEN_LINK = (By.CSS_SELECTOR, "#grid_WorkflowInstanceGrid tbody [title='Open']")
        WORKFLOW_NAME_FILTER_FIELD = (By.ID, "id___filterTemplateName")
        SELECT_ALL_TASKS_CHECKBOX = (By.CSS_SELECTOR, "#grid_TaskGridPlan thead [type='checkbox']")
        DELETE_BUTTON = (By.LINK_TEXT, "Delete")
