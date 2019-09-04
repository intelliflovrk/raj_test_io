from selenium.webdriver.common.by import By

from ioffice.admin.workflow.base import WorkflowBasePage


class WorkflowTemplatesPage(WorkflowBasePage):

    def click_categories(self):
        return self.click(WorkflowTemplatesPage.Locators.CATEGORIES_TAB)

    def clear_template_name_filter(self):
        return self.clear(WorkflowTemplatesPage.Locators.TEMPLATE_NAME_FILTER_FIELD)

    def fill_in_template_name_filter(self, template_name):
        return self.fill_in_field(WorkflowTemplatesPage.Locators.TEMPLATE_NAME_FILTER_FIELD, template_name)

    def click_filter_button(self):
        return self.click(WorkflowTemplatesPage.Locators.FILTER_BUTTON)

    def select_first_template(self):
        return self.click(WorkflowTemplatesPage.Locators.FIRST_TEMPLATE_RADIO_BUTTON)

    def click_delete_template(self):
        return self.click(WorkflowTemplatesPage.Locators.DELETE_BUTTON)

    def click_archive_template(self):
        return self.click(WorkflowTemplatesPage.Locators.ARCHIVE_BUTTON)

    class Locators(object):
        CATEGORIES_TAB = (By.XPATH, "//a[@href='/nio/workflowadministration/ListTemplateCategories']")
        TEMPLATES_TAB = (By.XPATH, "/nio/workflowadministration/ListTemplates")
        ADD_NEW_WORKFLOW_TEMPLATE_LINK = (By.LINK_TEXT, "Add New Workflow Template")
        TEMPLATE_NAME_FILTER_FIELD = (By.ID, "id___filterName")
        FILTER_BUTTON = (By.CSS_SELECTOR, "#templateGrid__ > td.last > a.jq-filter.button.button-enabled")
        FIRST_TEMPLATE_RADIO_BUTTON = (By.CSS_SELECTOR, "td.rowselect.first > input[type=\"radio\"]")
        DELETE_BUTTON = (By.ID, "templateGrid_11")
        ARCHIVE_BUTTON = (By.ID, "templateGrid_12")
