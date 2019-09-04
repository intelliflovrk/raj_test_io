from utils import *
from dsl.add_mortgage_plan import AddMortgagePlan
from dsl.client_activities import ClientActivities
from fakedata import rand_text
from ioffice.admin.admin import AdministrationPage, IOBasePage
from ioffice.admin.workflow.add_new_step_dialog import AddNewStepDialog
from ioffice.admin.workflow.add_new_workflow_template_dialog import AddNewWorkflowTemplateDialog
from ioffice.admin.workflow.categories_list import TemplateCategoriesPage
from ioffice.admin.workflow.change_status_dialog import ChangeStatusDialog
from ioffice.admin.workflow.templates import WorkflowTemplatesPage, WorkflowBasePage
from ioffice.admin.workflow.workflow_template import WorkflowTemplateBasePage, \
    WorkflowTemplateRolesPage, WorkflowTemplateAutomationPage
from ioffice.clients.activities.client_workflows import ViewClientWorkflowsPage
from ioffice.clients.activities.open_activities import TasksAndApptsPage
from ioffice.plans.activities import PlanActivitiesPage, BasePlanPage
from ioffice.plans.view_workflow import ViewWorkflowPage


class WorkflowActions:
    def __init__(self, config):
        self.config = config

    def using_add_new_step_dialog(self):
        template_page = WorkflowTemplateBasePage(self.config)
        template_page.hover_over_workflow_actions_menu() \
            .select_add_step()
        return WorkflowActions._AddNewStep(self.config.workflow_id, template_page, self)

    def assign_all_roles_to_workflow(self):
        WorkflowTemplateBasePage(self.config) \
            .template_navigation_menu() \
            .click_roles_tab()
        WorkflowTemplateRolesPage(self.config) \
            .tick_on_demand() \
            .click_all_available_roles() \
            .click_move_all_right() \
            .click_save()
        return self

    def set_start_workflow_on(self, start_on):
        WorkflowTemplateBasePage(self.config) \
            .template_navigation_menu() \
            .click_automation_tab()
        WorkflowTemplateAutomationPage(self.config) \
            .select_start_workflow_on(start_on) \
            .click_save()
        return self

    def using_change_status_dialog(self):
        template_page = WorkflowTemplateBasePage(self.config)
        template_page.hover_over_workflow_actions_menu() \
            .select_change_status()
        return WorkflowActions._ChangeStatus(self.config.workflow_id, template_page, self)

    def verify_if_template_status_is(self, status):
        assert status in WorkflowTemplateBasePage(self.config).get_template_bar_info(), \
            "Workflow status is not {}".format(status)
        return self

    class _AddNewStep:
        def __init__(self, template_id, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddNewStepDialog(template_id, current_page)

        def add_task(self):
            self.dialog.select_step_type(get_common_data(self.config)["test_data"]["workflow_data"]["select_step_task"]) \
                .select_first_task_category() \
                .select_first_task_type()
            return self

        def set_transition_to_next_step_when_to(self, when_value):
            self.dialog.select_transition_to_next_step_when(when_value)
            return self

        def assign_to_logged_in_user(self):
            self.dialog.select_assign_to(
                get_common_data(self.config)["test_data"]["workflow_data"]["assign_to_logged_in_user"])
            return self

        def set_context_role_to(self, context_role):
            self.dialog.select_assign_to(
                get_common_data(self.config)["test_data"]["workflow_data"]["assign_to_context_role"]) \
                .select_context_role(context_role)
            return self

        def add_new_step(self):
            self.dialog.click_add() \
                .close_io_dialog()
            return self.journey

    class _ChangeStatus:
        def __init__(self, template_id, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ChangeStatusDialog(template_id, current_page)

        def change_status_to(self, status):
            self.dialog.select_status(status) \
                .click_save() \
                .close_io_dialog()
            return self.journey


class Workflow(WorkflowActions):

    def navigate_to_workflow_categories(self):
        IOBasePage(self.config).level1_menu() \
            .hover_over_navigation_menu() \
            .click_administration()
        AdministrationPage(self.config).level2_menu() \
            .click_workflow()
        WorkflowTemplatesPage(self.config).click_categories()
        return self

    def create_category(self):
        category_name = get_common_data(self.config)["test_data"]["workflow_data"]["category_name"] + rand_text()
        add_temp_data(self.config, "workflow_category", {"name": category_name})
        TemplateCategoriesPage(self.config) \
            .fill_in_category_name(category_name) \
            .click_create() \
            .wait_until_please_wait_spinner_present()
        self.save_category_id()
        return self

    def save_category_id(self):
        category = get_temp_data(self.config, "workflow_category")
        TemplateCategoriesPage(self.config).clear_category_name_filter() \
            .fill_in_category_name_filter(category["name"]) \
            .click_filter() \
            .wait_until_please_wait_spinner_present()
        category_id = TemplateCategoriesPage(self.config).get_category_id()
        update_temp_data(self.config, "workflow_category", 0, "templateCategoryId", category_id)
        return self

    def using_add_new_workflow_template_dialog(self):
        workflow_page = WorkflowBasePage(self.config)
        workflow_page.click_add_new_workflow_templates()
        return Workflow._AddNewWorkflowTemplate(workflow_page, self)

    def save_workflow_id(self):
        self.config.workflow_id = WorkflowTemplateBasePage(self.config).get_template_id()
        return self

    class _AddNewWorkflowTemplate:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddNewWorkflowTemplateDialog(current_page)

        def add_new_workflow_template_related_to(self, related_to):
            add_temp_data(self.config, "workflow_template", {"name": get_common_data(self.config)["test_data"]["workflow_data"]["template_name"] + rand_text()})
            self.dialog.fill_in_template_name(get_temp_data(self.config, "workflow_template")["name"]) \
                .select_related_to(related_to) \
                .select_category(get_temp_data(self.config, "workflow_category")["name"])
            return self

        def set_owner_to(self, owner):
            self.dialog.open_user_search_dialog() \
                .click_clear_button() \
                .fill_in_user(owner) \
                .click_search() \
                .click_first_result() \
                .close_io_dialog()
            return self

        def save_new_workflow_template(self):
            self.dialog.click_save_button() \
                .close_io_dialog()
            self.journey.save_workflow_id()
            return self.journey


class TriggerWorkflow(Workflow, AddMortgagePlan, ClientActivities):

    def open_plan_workflow_instance(self):
        time.sleep(10)
        BasePlanPage(self.config).click_activities()
        PlanActivitiesPage(self.config).fill_in_workflow_name_filter(get_temp_data(self.config, "workflow_template")["name"]) \
            .click_filter() \
            .wait_until_please_wait_spinner_present() \
            .open_first_workflow()
        return self

    def verify_task_owner(self):
        viewworkflowpage = ViewWorkflowPage(self.config)
        stepsdetailslist = get_str_list_from_list_of_webelements(viewworkflowpage.get_steps_table_rows())
        assert is_string_present(stepsdetailslist, get_common_data(
            self.config)["test_data"]["workflow_data"]["task_owner"]), "Task Owner is not found"
        return self

    def verify_workflow_visible_on_client_workflows(self):
        client_workflows_page = ViewClientWorkflowsPage(self.config)
        client_workflow_details_list = get_str_list_from_list_of_webelements(
            client_workflows_page.get_workflow_table_rows())
        assert is_string_present(
            client_workflow_details_list, get_temp_data(self.config, "workflow_template")["name"]), "Workflow entry is not found"
        return self