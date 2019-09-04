from selenium.webdriver.common.by import By
from ioffice.admin.admin import AdministrationPage


class WorkflowBasePage(AdministrationPage):

    def click_add_new_workflow_templates(self):
        return self.click(WorkflowBasePage.Locators.ADD_NEW_WORKFLOW_TEMPLATE_LINK)

    class Locators(object):
        ADD_NEW_WORKFLOW_TEMPLATE_LINK = (By.LINK_TEXT, "Add New Workflow Template")
