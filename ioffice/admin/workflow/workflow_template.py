from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection
from ioffice.admin.workflow.base import WorkflowBasePage
import re


class WorkflowTemplateBasePage(WorkflowBasePage):

    def hover_over_workflow_actions_menu(self):
        self.hover_over(WorkflowTemplateBasePage.Locators.ACTIONS_MENU)
        return WorkflowActionsMenuSection(self)

    def template_navigation_menu(self):
        return WorkflowTemplateNavigationMenuSection(self)

    def get_template_id(self):
        return re.search(r'(?<=workflowadministration/)\d+', self.driver.current_url, flags=re.IGNORECASE).group(0)

    def get_template_bar_info(self):
        return self.get_text(WorkflowTemplateBasePage.Locators.BAR_INFO)

    class Locators(object):
        ACTIONS_MENU = (By.ID, "primary")
        BAR_INFO = (By.XPATH, "//*[@id='sidebar-container']//*[@class='bar-info']")


class WorkflowTemplateNavigationMenuSection(BasePageSection):

    def click_automation_tab(self):
        self.page.click(WorkflowTemplateNavigationMenuSection.Locators.AUTOMATION_TAB)
        return self

    def click_steps_tab(self):
        self.page.click(WorkflowTemplateNavigationMenuSection.Locators.STEPS_TAB)
        return self

    def click_roles_tab(self):
        self.page.click(WorkflowTemplateNavigationMenuSection.Locators.ROLES_TAB)
        return self

    class Locators(object):
        AUTOMATION_TAB = (By.XPATH, "//div[@id='id_root_2_2_3']//*[text()='Automation']/ancestor::a")
        STEPS_TAB = (By.XPATH, "//div[@id='id_root_2_2_3']//*[text()='Steps']/ancestor::a")
        ROLES_TAB = (By.XPATH, "//div[@id='id_root_2_2_3']//*[text()='Roles']/ancestor::a")


class WorkflowTemplateRolesPage(WorkflowTemplateBasePage):

    def tick_on_demand(self):
        return self.click(WorkflowTemplateRolesPage.Locators.ON_DEMAND_CHECKBOX)

    def click_all_available_roles(self):
        return self.click(WorkflowTemplateRolesPage.Locators.ALL_AVAILABLE_ROLES_BUTTON)

    def click_move_all_right(self):
        return self.click(WorkflowTemplateRolesPage.Locators.MOVE_ALL_RIGHT_BUTTON)

    def click_save(self):
        return self.click(WorkflowTemplateRolesPage.Locators.SAVE_BUTTON)

    class Locators(object):
        ON_DEMAND_CHECKBOX = (By.ID, 'chkOnDemand')
        ALL_AVAILABLE_ROLES_BUTTON = (By.XPATH,
                                      "//span[text()='Available Roles']/following-sibling::span/button[text()='All']")
        MOVE_ALL_RIGHT_BUTTON = (By.CLASS_NAME, 'moveallright')
        SAVE_BUTTON = (By.LINK_TEXT, 'Save')


class WorkflowTemplateAutomationPage(WorkflowTemplateBasePage):
    def select_start_workflow_on(self, trigger_option):
        return self.select_by_visible_text(WorkflowTemplateAutomationPage.Locators.START_WORKFLOW_ON_SELECT_BOX, trigger_option)

    def click_save(self):
        return self.click(WorkflowTemplateAutomationPage.Locators.SAVE_BUTTON)

    class Locators(object):
        START_WORKFLOW_ON_SELECT_BOX = (By.ID, "triggerOption")
        SAVE_BUTTON = (By.LINK_TEXT, 'Save')


class WorkflowActionsMenuSection(BasePageSection):

    def select_add_step(self):
        self.page.click(WorkflowActionsMenuSection.Locators.ADD_STEP_LINK)
        return self

    def select_change_status(self):
        self.page.click(WorkflowActionsMenuSection.Locators.CHANGE_STATUS_LINK)
        return self

    class Locators(object):
        ADD_STEP_LINK = (By.LINK_TEXT, "Add Step")
        CHANGE_STATUS_LINK = (By.LINK_TEXT, "Change Status")
