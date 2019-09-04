import pytest
from dsl.workflow import Workflow, TriggerWorkflow
import sys

pytestmark = [pytest.mark.workflow, pytest.mark.io_all,
              pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='fails on tst'),
              pytest.mark.skipif('prd-10' == pytest.config.option.env, reason='IP-56649')]


@pytest.mark.usefixtures("api_archive_workflow")
@pytest.mark.usefixtures("api_delete_workflow")
@pytest.mark.usefixtures("api_delete_category")
@pytest.mark.usefixtures("ui_login_logout")
def test_create_workflow_template(config):
    """Test Description: Creating a new plan workflow template and moving it to Active status"""
    test = (Workflow(config)
            .navigate_to_workflow_categories()
            .create_category()
            .using_add_new_workflow_template_dialog()
                .add_new_workflow_template_related_to("Plan")
                .set_owner_to(config.username)
                .save_new_workflow_template()
            .using_change_status_dialog()
                .change_status_to("Active")
            .verify_if_template_status_is("Active")
            )


@pytest.mark.usefixtures("ui_delete_plan_tasks")
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_archive_workflow")
@pytest.mark.usefixtures("api_create_workflow_category")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_trigger_plan_workflow(config):
    """Test Description: Creating a new plan workflow template and triggering it"""
    test = (TriggerWorkflow(config)
            .navigate_to_workflow_categories()
            .using_add_new_workflow_template_dialog()
                .add_new_workflow_template_related_to("Plan")
                .set_owner_to(config.username)
                .save_new_workflow_template()
            .using_add_new_step_dialog()
                .add_task()
                .set_transition_to_next_step_when_to("Created")
                .set_context_role_to("T&C Coach")
                .add_new_step()
            .set_start_workflow_on("Plan creation")
            .using_change_status_dialog()
                .change_status_to("Active")
            .open_client_by_url()
            .using_add_plan_wizard()
                .add_mortgage_plan_with_basic_details()
                .finish()
            .open_plan_workflow_instance()
            .verify_task_owner()
            )


@pytest.mark.organiser
@pytest.mark.usefixtures("ui_delete_client_open_activities")
@pytest.mark.usefixtures("api_archive_workflow")
@pytest.mark.usefixtures("api_create_workflow_category")
@pytest.mark.usefixtures("ui_login_logout")
def test_trigger_client_workflow(config):
    test = (TriggerWorkflow(config)
            .navigate_to_workflow_categories()
            .using_add_new_workflow_template_dialog()
                .add_new_workflow_template_related_to("Client")
                .set_owner_to(config.username)
                .save_new_workflow_template()
            .using_add_new_step_dialog()
                .add_task()
                .set_transition_to_next_step_when_to("Completed")
                .assign_to_logged_in_user()
                .add_new_step()
            .assign_all_roles_to_workflow()
            .set_start_workflow_on("Client creation")
            .using_change_status_dialog()
                .change_status_to("Active")
            .using_add_client_wizard()
                .add_basic_client_details()
                .finish()
            .navigate_to_client_open_activities()
            .verify_workflow_task_visible_on_client_activities()
            .navigate_to_client_workflows()
            .verify_workflow_visible_on_client_workflows()
            )
