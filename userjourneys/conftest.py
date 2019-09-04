import pytest
from api import leads, fees, clients_documents
from api import clients
from api import relationships
from api import plans
from api import workflow
from api import contributions
from api import withdrawals
from api import valuations
from api import holdings
from api import quotes
from api import securemessaging
from api import leads_documents
from api import tags
from api import client_dependants
from api import factfind
from api import tasks
from api import imps
from api import models
from dsl.fee_actions import FeeActions
from dsl.lead_activities import AddLeadTask
from dsl.provider_statement import ElectronicImports, ProviderStatement
from dsl.search import SearchPlan, SearchFee, SearchClient
from dsl.plan_actions import PlanActions
from dsl.set_up_needs_and_priorities_questions import *
from dsl.set_up_user_delegation import *
from dsl.cash_receipts import CashReceipts
from dsl.client_activities import ClientActivities
from api.published_apps import *
from dsl.generate_document import GenerateDocument
from dsl.login_to_pfp import LogIn as PFPLogin
from dsl.upload_document import ClientDocuments
from dsl.get_client_quote import GetClientQuote
from dsl.client_opportunities import ClientOpportunities
from dsl.client_service_case import ClientServiceCase
from dsl.advice_planning import PlanningOpportunities
from dsl.rebalance import StartRebalanceCommunication
from dsl.pfp_recommendations import AcceptRecommendation
import fakedata
from datetime import datetime


# <editor-fold desc="api fixtures">
from dsl.user_tasks import UserTasks
from ioffice.income.statement_search import StatementSearchPage


@pytest.fixture
def api_create_client(config):
    client = clients.create_client(config)
    utils.add_temp_data(config, "client", client)


@pytest.fixture
def api_search_default_client_and_save_details(config):
    client_details = clients.search_client(config, get_common_data(config)["clients"]["default"]["lastname"])
    utils.add_temp_data(config, "client", {"id": client_details["items"][0]["partyId"],
                                           "name": client_details["items"][0]["party"]["name"]})
    config.access_token = None


@pytest.fixture
def api_search_pfp_imps_client_and_save_details(config):
    client_details = clients.search_client(config, get_common_data(config)["clients"]["pfp_imps_client"]["lastname"])
    utils.add_temp_data(config, "client", {"id": client_details["items"][0]["partyId"],
                                           "name": client_details["items"][0]["party"]["name"]})
    config.access_token = None


@pytest.fixture
def api_create_lead(config):
    lead = leads.create_lead(config)
    utils.add_temp_data(config, "lead", lead)


@pytest.fixture
def api_delete_lead(config):
    yield
    leads.delete_lead(config,  utils.get_temp_data(config, "lead")['id'])


@pytest.fixture
def api_add_lead_address(config):
    lead = get_temp_data(config, "lead")
    address = leads.add_address_for_lead(config, lead["id"])
    utils.add_temp_data(config, "address", address)


@pytest.fixture
def api_add_client_address(config):
    client = get_temp_data(config, "client")
    address = clients.add_address_for_client(config, client["id"])
    utils.add_temp_data(config, "address", address)


@pytest.fixture
def api_create_client_relationship(config):
    client_list = get_temp_data_collection(config, "client")
    client_relationship = relationships.create_relationships_for_client(config, client_list[0]["id"], client_list[1]["id"])
    add_temp_data(config, "client_relationship", client_relationship)


@pytest.fixture
def api_create_employee_relationship(config):
    client_list = get_temp_data_collection(config, "client")
    client_relationship = relationships.create_relationships_for_client(config, client_list[0]["id"], client_list[1]["id"],
    "Employee")
    add_temp_data(config, "client_relationship", client_relationship)


@pytest.fixture
def api_create_corporate_client(config):
    client = clients.create_corporate_client(config)
    add_temp_data(config, "client", client)


@pytest.fixture
def api_create_client_fee(config):
    client = get_temp_data(config, "client")
    fee = fees.create_fee_for_client(config, client["id"])
    utils.add_temp_data(config, "fee", fee)


@pytest.fixture
def api_install_uninstall_app(config):
    install_app(config, config.variables["environments"][config.env]["data"]["automation_test_app"]["app_id"])
    yield
    uninstall_app(config, config.variables["environments"][config.env]["data"]["automation_test_app"]["app_id"])


@pytest.fixture
def api_delete_plan(config):
    yield
    client = get_temp_data(config, "client")
    plan = get_temp_data(config, "plan")
    plans.change_plan_status_to(config, client["id"], plan["id"], "Deleted")


@pytest.fixture
def api_delete_clients_plans(config):
    yield
    clients_list = utils.get_temp_data_collection(config, "client")
    for client in clients_list:
        plans_list = plans.get_plans_for_a_client(config, client["id"])
        for plan in plans_list["items"]:
            plans.change_plan_status_to(config, client["id"], plan["id"], "Deleted")


@pytest.fixture
def api_delete_sub_plan(config):
    yield
    client = get_temp_data(config, "client")
    plans.change_plan_status_to(config, client["id"], config.sub_plan_id, "Deleted")


@pytest.fixture
def api_change_plan_status_to_compliance_sign_off(config):
    plan = get_temp_data(config, "plan")
    plans.change_plan_status_to(config, plan["owners"][0]["id"], plan["id"], "Compliance Sign off")


@pytest.fixture
def api_change_plan_status_to_submitted_to_provider(config):
    plan = get_temp_data(config, "plan")
    plans.change_plan_status_to(config, plan["owners"][0]["id"], plan["id"], "Submitted to Provider")


@pytest.fixture
def api_delete_workflow(config):
    yield
    workflow.delete_workflow(config, config.workflow_id)


@pytest.fixture
def api_archive_workflow(config):
    yield
    workflow.change_workflow_status_to(config, config.workflow_id, "Archived")


@pytest.fixture
def api_create_workflow_category(config):
    workflow_category = workflow.create_workflow_category(config)
    utils.add_temp_data(config, "workflow_category", workflow_category)


@pytest.fixture
def api_delete_category(config):
    yield
    workflow_category = get_temp_data(config, "workflow_category")
    workflow.delete_category(config, workflow_category["templateCategoryId"])


@pytest.fixture
def api_delete_plans_contributions(config):
    yield
    client = get_temp_data(config, "client")
    contributions_list = utils.get_temp_data_collection(config, "contribution")
    for contribution in contributions_list:
        contributions.delete_contribution(config, client["id"], contribution["plan"]["id"], contribution["id"])


@pytest.fixture
def api_delete_plans_withdrawals(config):
    yield
    client = get_temp_data(config, "client")
    withdrawals_list = utils.get_temp_data_collection(config, "withdrawal")
    for withdrawal in withdrawals_list:
        withdrawals.delete_withdrawal(config, client["id"], withdrawal["plan"]["id"], withdrawal["id"])


@pytest.fixture
def api_create_joint_client(config):
    first_client = clients.create_client(config)
    utils.add_temp_data(config, "client", first_client)
    second_client = clients.create_client(config)
    utils.add_temp_data(config, "client", second_client)
    client_relationship = relationships.create_relationships_for_client(config, first_client["id"], second_client["id"])
    add_temp_data(config, "client_relationship", client_relationship)


@pytest.fixture
def api_delete_client_relationship(config):
    yield
    client = get_temp_data(config, "client")
    client_relationship = get_temp_data(config, "client_relationship")
    relationships.delete_relationship_for_client(config, client["id"], client_relationship["id"])


@pytest.fixture
def api_delete_client_documents(config):
    yield
    client = get_temp_data(config, "client")
    client_documents = clients_documents.get_client_documents(config, client["id"])
    for document in client_documents["items"]:
        clients_documents.delete_client_document(config, client["id"], document["id"])


@pytest.fixture
def api_delete_lead_documents(config):
    yield
    lead = get_temp_data(config, "lead")
    lead_documents = leads_documents.get_leads_documents(config, lead["id"])
    for document in lead_documents["items"]:
        leads_documents.delete_leads_document(config, lead["id"], document["id"])


@pytest.fixture
def api_delete_lead_relationship(config):
    yield
    lead = get_temp_data(config, "lead")
    lead_relationship = get_temp_data(config, "lead_relationship")
    relationships.delete_relationship_for_lead(config, lead["id"], lead_relationship["id"])


@pytest.fixture
def api_delete_second_life_documents(config):
    yield
    client_id_second_life = get_temp_data(config, "client", 1)["id"]
    client_documents = clients_documents.get_client_documents(config, client_id_second_life)
    for document in client_documents["items"]:
        clients_documents.delete_client_document(config, client_id_second_life, document["id"])


@pytest.fixture
def api_delete_client_plans(config):
    yield
    client = get_temp_data(config, "client")
    plans_list = plans.get_plans_for_a_client(config, client["id"])
    for plan in plans_list["items"]:
        plans.change_plan_status_to(config, client["id"], plan["id"], "Deleted")


@pytest.fixture
def api_create_client_quote(config):
    client = get_temp_data(config, "client")
    quote = quotes.create_quote(config, client["id"])
    add_temp_data(config, "quote", quote)


@pytest.fixture
def api_set_quote_status_to_complete(config):
    client = get_temp_data(config, "client")
    quote = get_temp_data(config, "quote")
    quotes.set_quote_status(config, client["id"], quote["id"], "Complete")


@pytest.fixture
def api_create_client_quote_result(config):
    client = get_temp_data(config, "client")
    quote = get_temp_data(config, "quote")
    quote_result = quotes.create_quote_result(config, client["id"], quote["id"])
    add_temp_data(config, "quote_result", quote_result)


@pytest.fixture
def api_create_client_joint_quote_result(config):
    quote = get_temp_data(config, "quote")
    quote_result = quotes.create_quote_result(config, get_temp_data(
        config, "client", 0)["id"], quote["id"], get_temp_data(config, "client", 1)["id"])
    add_temp_data(config, "quote_result", quote_result)


@pytest.fixture
def api_upload_documents_to_quote(config):
    client = get_temp_data(config, "client")
    quote = get_temp_data(config, "quote")
    clients_documents.create_client_quote_document(config, client["id"], quote["id"])
    clients_documents.upload_client_document(config.document_location, open(utils.get_test_documents_file_url(
        "Test Automation Quote Document.pdf"),'rb'))
    return config


@pytest.fixture
def api_upload_documents_to_quote_result(config):
    client = get_temp_data(config, "client")
    quote_result = get_temp_data(config, "quote_result")
    clients_documents.create_client_quote_result_document(config, client["id"], quote_result["id"])
    clients_documents.upload_client_document(config.document_location, open(
        utils.get_test_documents_file_url("Test Automation Quote Result Document.pdf"), 'rb'))


@pytest.fixture
def api_upload_quote_documents_to_joint_client(config):
    clients_documents.create_client_quote_document(config, get_temp_data(config, "client")["id"], get_temp_data(config, "quote")
    ["id"])
    clients_documents.create_client_quote_document(config, get_temp_data(config, "client", 1)["id"], get_temp_data(config,
    "quote")["id"])


@pytest.fixture
def api_upload_quote_result_documents_to_joint_client(config):
    clients_documents.create_client_quote_result_document(config, get_temp_data(config, "client")["id"],
                                                          get_temp_data(config, "quote_result")["id"])
    clients_documents.create_client_quote_result_document(config, get_temp_data(config, "client", 1)["id"],
                                                          get_temp_data(config, "quote_result")["id"])
    return config


@pytest.fixture
def api_upload_client_document(config):
    clients_documents.create_client_document(config, get_temp_data(config, "client")["id"])
    clients_documents.upload_client_document(config.document_location,
                                             open(utils.get_test_documents_file_url("UploadDocument.pdf"), 'rb'))


@pytest.fixture
def api_create_pre_existing_wrap_plan(config):
    config.plan_wrap = {"policyNumber": fakedata.rand_int(5), "startsOn": datetime.now().strftime("%Y-%m-%d"),
                        "planType": {"name": "Wrap"}}
    plan = plans.create_plan(config, get_temp_data(config, "client")["id"], "pension", True, config.plan_wrap)
    utils.add_temp_data(config, "plan", plan)


@pytest.fixture
def api_create_pre_existing_pension_plan(config):
    config.plan = {"policyNumber": fakedata.rand_int(5)}
    client = get_temp_data(config, "client")
    plan = plans.create_plan(config, client["id"], "pension", True, config.plan)
    utils.add_temp_data(config, "plan", plan)


@pytest.fixture
def api_create_mortgage_plan(config):
    client = get_temp_data(config, "client")
    plan = plans.create_plan(config, client["id"], "mortgage")
    utils.add_temp_data(config, "plan", plan)


@pytest.fixture
def api_create_investment_plan(config):
    client = get_temp_data(config, "client")
    plan = plans.create_plan(config, client["id"], "investment")
    utils.add_temp_data(config, "plan", plan)


@pytest.fixture
def api_create_sipp_plan(config):
    config.plan = {"planType": {"name": "SIPP"}}
    client = get_temp_data(config, "client")
    plan = plans.create_plan(config, client["id"], "pension", False, config.plan)
    utils.add_temp_data(config, "plan", plan)


@pytest.fixture
def api_create_pre_existing_investment_plan(config):
    config.plan = {"policyNumber": fakedata.rand_int(5)}
    client = get_temp_data(config, "client")
    plan = plans.create_plan(config, client["id"], "investment", True, config.plan)
    utils.add_temp_data(config, "plan", plan)


@pytest.fixture
def api_create_pre_existing_investment_plan_for_all_clients(config):
    clients_list = get_temp_data_collection(config, "client")
    for client in clients_list:
        plan = plans.create_plan(config, client["id"], "investment", True, {"policyNumber": fakedata.rand_int(5)})
        utils.add_temp_data(config, "plan", plan)


@pytest.fixture
def api_create_contribution(config):
    plan = get_temp_data(config, "plan")
    contribution = contributions.create_contribution(config, plan["owners"][0]["id"], plan["id"])
    utils.add_temp_data(config, "contribution", contribution)


@pytest.fixture
def api_create_withdrawal(config):
    plan = get_temp_data(config, "plan")
    withdrawal = withdrawals.create_withdrawal(config, plan["owners"][0]["id"], plan["id"])
    utils.add_temp_data(config, "withdrawal", withdrawal)


@pytest.fixture
def api_create_valuation_for_client_plans(config):
    plans_list = get_temp_data_collection(config, "plan")
    for plan in plans_list:
        valuation = valuations.create_valuation(config, plan["owners"][0]["id"], plan["id"], fakedata.rand_int(4))
        utils.add_temp_data(config, "valuation", valuation)


@pytest.fixture
def api_create_fund(config):
    plan = get_temp_data(config, "plan")
    fund_holding = holdings.create_fund_holding(config, plan["owners"][0]["id"], plan["id"])
    utils.add_temp_data(config, "fund_holding", fund_holding)


@pytest.fixture
def api_create_fund_for_all_plans(config):
    plans_list = get_temp_data_collection(config, "plan")
    for plan in plans_list:
        fund_holding = holdings.create_fund_holding(config, plan["owners"][0]["id"], plan["id"])
        utils.add_temp_data(config, "fund_holding", fund_holding)


@pytest.fixture
def api_create_fund_for_sub_plan(config):
    plan = get_temp_data(config, "plan", 1)
    fund_holding = holdings.create_fund_holding(config, plan["owners"][0]["id"], plan["id"])
    utils.add_temp_data(config, "fund_holding", fund_holding)


@pytest.fixture
def api_create_joint_client_quote(config):
    first_life = clients.create_client(config)
    utils.add_temp_data(config, "client", first_life)
    second_life = clients.create_client(config)
    utils.add_temp_data(config, "client", second_life)
    client_relationship = relationships.create_relationships_for_client(config, first_life["id"], second_life["id"])
    add_temp_data(config, "client_relationship", client_relationship)
    quote = quotes.create_quote(config, first_life["id"])
    utils.add_temp_data(config, "quote", quote)
    quotes.add_second_life_to_quote(config, second_life["id"], quote["id"])


@pytest.fixture
def api_send_secure_message(config):
    secure_message = securemessaging.create_secure_message(config)
    add_temp_data(config, "secure_message", secure_message)
    securemessaging.send_secure_message(config, secure_message["messageId"])


@pytest.fixture
def api_delete_client_tag(config):
    yield
    tags.delete_tag_for_client(config, get_temp_data(config, "client")["id"], get_temp_data(config, "tag")["tag"])


@pytest.fixture
def api_add_delete_client_goal(config):
    goal = factfind.create_client_goal(config, get_temp_data(config, "client")["id"])
    utils.add_temp_data(config, "goal", goal)
    yield
    factfind.delete_client_goal(config, get_temp_data(config, "client")["id"], get_temp_data(config, "goal")["goalId"])


@pytest.fixture
def api_create_task(config):
    client = get_temp_data(config, "client")
    task = tasks.create_task(config, client["id"])
    utils.add_temp_data(config, "task", task)


@pytest.fixture
def api_delete_client_address(config):
    yield
    client_address = clients.get_addresses_for_client(config, get_temp_data(config, "client")["id"])
    update_temp_data(config, "client", 0, "client_address", client_address)
    clients.delete_address_for_client(config, get_temp_data(config, "client")["id"], get_temp_data(config, "client")["client_address"]["items"][0]["id"])


@pytest.fixture
def api_delete_client_employment(config):
    yield
    client_employment = clients.get_employment_for_client(config, get_temp_data(config, "client")["id"])
    update_temp_data(config, "client", 0, "client_employment", client_employment)
    clients.delete_employment_for_client(config, get_temp_data(config, "client")["id"], client_employment['items'][0]["id"])


@pytest.fixture
def api_delete_client_contact(config):
    yield
    client_contact = clients.get_contacts_for_client(config, get_temp_data(config, "client")["id"])
    update_temp_data(config, "client", 0, "client_contacts", client_contact)
    clients.delete_contact_for_client(config, get_temp_data(config, "client")["id"], get_temp_data(config, "client")["client_contacts"]["items"][0]["id"])


@pytest.fixture
def api_add_client_contact(config):
    contact = clients.add_contact_for_client(config, get_temp_data(config, "client")["id"], "Mobile")
    utils.add_temp_data(config, "client_contacts", contact)


@pytest.fixture
def api_delete_fund_proposal_for_all_plans(config):
    yield
    plans_list = get_temp_data_collection(config, "plan")
    for plan in plans_list:
        holdings.delete_fundproposal_for_plan(config, plan["owners"][0]["id"], plan["id"])


@pytest.fixture
def api_create_active_imps_model(config):
    imps_model = imps.create_model_portfolio(config)
    utils.add_temp_data(config, "imps_model", imps_model)
    imps.accept_model_portfolio(config, imps_model["id"])


@pytest.fixture
def api_add_imps_model_to_fund_proposal_for_all_plans(config):
    imps_models = models.get_portfolio_models(config)["items"]
    active_imps_model = utils.find_active_model_by_code(imps_models, utils.get_temp_data(config, "imps_model")["code"])
    utils.add_temp_data(config, "portfolio_model", active_imps_model)
    plans_list = get_temp_data_collection(config, "plan")
    for plan in plans_list:
        fund_proposal = holdings.add_model_to_plan_fundproposal(config, plan["owners"][0]["id"], plan["id"], active_imps_model["id"])
        add_temp_data(config, "fund_proposal", fund_proposal)


@pytest.fixture
def api_deactivate_portfolio_model(config):
    yield
    models.deactivate_portfolio_model(config, utils.get_temp_data(config, "portfolio_model")["id"])

# </editor-fold>

# <editor-fold desc="ui fixtures">


@pytest.fixture
def ui_delete_fee(config):
    yield
    SearchFee(config).open_fee()
    FeeActions(config).open_change_fee_status_dialog().change_fee_status_to(
        get_common_data(config)["test_data"]["change_plan_status_data"]["deleted"])


@pytest.fixture
def ui_login_logout(config):
    LogIn(config).navigate_to_login_page().login().assert_user_logged_in()
    yield
    LogIn(config).logout()


@pytest.fixture
def ui_login(config):
    LogIn(config).navigate_to_login_page().login().assert_user_logged_in()


@pytest.fixture
def ui_logout_login(config):
    yield
    LogIn(config).logout()
    LogIn(config).navigate_to_login_page().login().assert_user_logged_in()


@pytest.fixture
def ui_delete_needs_priorities_question(config):
    yield
    SetupNeedsAndPrioritiesQuestions(config).navigate_to_needs_questions().delete_question()


@pytest.fixture
def ui_delete_needs_priorities_answer(config):
    yield
    SetupNeedsAndPrioritiesQuestions(config).open_client_by_url().go_to_fact_find()\
        .navigate_to_needs_and_priorities_tab().clear_need_and_priorities_answer()


@pytest.fixture
def ui_delete_risk_tolerance_data(config):
    yield
    SearchClient(config).open_client_by_url()
    CompleteFactFind(config).go_to_fact_find() \
        .clear_risk_subtab_data() \
        .clear_risk_replay_subtab_data()


@pytest.fixture
def ui_delete_plan_tasks(config):
    yield
    SearchPlan(config).open_plan_by_url()
    PlanActions(config).delete_plan_tasks()


@pytest.fixture
def ui_remove_delegate_from_user_account(config):
    yield
    SearchUser(config).navigate_to_manage_users().find_user()
    SetUpUserDelegation(config).navigate_to_delegate_tab().remove_delegate_from_user_account()


@pytest.fixture
def ui_remove_factfind_partner(config):
    yield
    CompleteFactFind(config).go_to_fact_find().using_add_remove_partner_wizard().remove_partner()


@pytest.fixture
def ui_create_client_plan_fee(config):
    ProviderStatement(config).add_plan_and_plan_fee()


@pytest.fixture
def ui_delete_cash_receipt(config):
    yield
    CashReceipts(config).navigate_to_cash_receipts_search().search_cash_receipt() \
        .using_cash_receipt_matching_dialog().unmatch_fee().search_cash_receipt().delete_cash_receipt()


@pytest.fixture
def ui_move_fee_to_cancelled_status(config):
    yield
    SearchFee(config).open_fee()
    FeeActions(config).open_change_fee_status_dialog().change_fee_status_to(
        get_common_data(config)["test_data"]["fee_data"]["fee_cancelled_status"])


@pytest.fixture
def ui_move_fee_to_due_status(config):
    SearchFee(config).open_fee()
    FeeActions(config).open_change_fee_status_dialog().change_fee_status_to(
        get_common_data(config)["test_data"]["fee_data"]["fee_due_status"])


@pytest.fixture
def ui_delete_statements_on_first_page(config):
    ProviderStatement(config).navigate_to_statement_search().search_statement()
    if StatementSearchPage(config).get_statement_count_on_first_page():
        StatementSearchPage(config).select_result_per_page("250")
        statement_count = StatementSearchPage(config).get_statement_count_on_first_page()
        while statement_count > 0:
            ProviderStatement(config).delete_statements()
            StatementSearchPage(config).click_search()
            statement_count -= 1
    yield
    ProviderStatement(config).navigate_to_statement_search().search_statement()
    if StatementSearchPage(config).get_statement_count_on_first_page():
        StatementSearchPage(config).select_result_per_page("250")
        statement_count = StatementSearchPage(config).get_statement_count_on_first_page()
        while statement_count > 0:
            ProviderStatement(config).delete_statements()
            StatementSearchPage(config).click_search()
            statement_count -= 1


@pytest.fixture
def ui_delete_live_statements(config):
    yield
    ElectronicImports(config).delete_live_statements()


@pytest.fixture
def ui_delete_imported_statement(config):
    yield
    ElectronicImports(config).delete_imported_statement()


@pytest.fixture
def ui_delete_client_open_activities(config):
    yield
    SearchClient(config).open_client_by_url()
    ClientActivities(config).navigate_to_client_open_activities().delete_client_open_activities()


@pytest.fixture
def ui_delete_user_open_tasks(config):
    yield
    UserTasks(config).navigate_to_organiser().delete_user_open_tasks()


@pytest.fixture
def ui_move_fee_to_draft_status(config):
    yield
    SearchFee(config).open_fee()
    FeeActions(config).open_change_fee_status_dialog().change_fee_status_to(
        get_common_data(config)["test_data"]["fee_data"]["fee_draft_status"])


@pytest.fixture
def ui_logout(config):
    yield
    LogIn(config).logout().assert_user_logged_out()


@pytest.fixture
def ui_clear_document_queue(config):
    yield
    SearchClient(config).open_client_by_url()
    GenerateDocument(config).open_document_queue().clear_document_queue()


@pytest.fixture
def ui_add_plan_to_wrapper(config):
    SearchPlan(config).open_plan_by_url(get_temp_data(config, 'client')['id'], get_temp_data(config, "plan", 1)["id"])
    PlanActions(config).using_add_to_wrapper_dialog().add_plan_to_wrapper()


@pytest.fixture
def ui_add_plan_report_note(config):
    SearchPlan(config).open_plan_by_url()
    PlanActions(config).add_wrap_report_notes()


@pytest.fixture
def ui_delete_plans_valuations(config):
    yield
    plans_list = utils.get_temp_data_collection(config, "plan")
    for plan in plans_list:
        SearchPlan(config).open_plan_by_url(get_temp_data(config, 'client')['id'], plan["id"])
        PlanActions(config).delete_valuations()


@pytest.fixture
def ui_delete_plan_valuations(config):
    yield
    SearchPlan(config).open_plan_by_url()
    PlanActions(config).delete_valuations()


@pytest.fixture
def ui_delete_funds(config):
    yield
    SearchPlan(config).open_plan_by_url()
    PlanActions(config).delete_funds()


@pytest.fixture
def ui_delete_funds_for_all_plans(config):
    yield
    plans_list = get_temp_data_collection(config, "plan")
    for plan in plans_list:
        SearchPlan(config).open_plan_by_url(plan["owners"][0]["id"], plan["id"])
        PlanActions(config).delete_funds()


@pytest.fixture
def ui_delete_funds_for_sub_plan(config):
    yield
    SearchPlan(config).open_plan_by_url(get_temp_data(config, 'client')['id'], get_temp_data(config, "plan", 1)["id"])
    PlanActions(config).delete_funds()


@pytest.fixture
def ui_create_delete_binder(config):
    ClientDocuments(config).open_client_by_url().open_client_binders().create_binder()
    yield
    ClientDocuments(config).open_client_by_url().open_client_binders().delete_binder()


@pytest.fixture
def ui_delete_quote(config):
    yield
    GetClientQuote(config).open_client_by_url().navigate_to_quotes_and_apps().delete_quote()


@pytest.fixture
def ui_add_delete_opportunity(config):
    SearchClient(config).open_client_by_url()
    ClientOpportunities(config).add_opportunity()
    yield
    SearchClient(config).open_client_by_url()
    ClientOpportunities(config).navigate_to_opportunities().open_opportunity().delete_opportunity()


@pytest.fixture
def ui_delete_service_case(config):
    yield
    SearchClient(config).open_client_by_url()
    ClientServiceCase(config).navigate_to_service_cases().open_service_case().delete_service_case()


@pytest.fixture
def ui_delete_service_case_for_all_clients(config):
    yield
    clients_list = utils.get_temp_data_collection(config, "client")
    for client in clients_list:
        SearchClient(config).open_client_by_url(client["id"])
        ClientServiceCase(config).navigate_to_service_cases().open_service_case().delete_service_case()



@pytest.fixture
def ui_delete_recommendations(config):
    yield
    SearchClient(config).open_client_by_url()
    PlanningOpportunities(config).using_planning_opportunities().open_recommendations()\
        .using_delete_recommendations_dialog().delete_all_recommendations()


@pytest.fixture
def ui_delete_lead_tasks(config):
    yield
    AddLeadTask(config).open_created_lead_by_url()\
        .navigate_to_lead_task_and_appts()\
        .delete_all_lead_tasks()


@pytest.fixture
def ui_add_imps_manual_recommendation(config):
    PlanningOpportunities(config).open_client_by_url()\
        .using_planning_opportunities()\
        .open_recommendations()\
        .using_add_manual_rec_dialog()\
        .add_switch_recommendation_details()\
        .add_model_portfolio("Automation Test iMPS Model")\
        .save_recommendation()


@pytest.fixture
def ui_start_rebalance_communication_process(config):
    StartRebalanceCommunication(config).using_rebalance_communication_options_dialog()\
        .start_rebalance_communication()
    LogIn(config).logout()

# </editor-fold>

# <editor-fold desc="file fixtures">


@pytest.fixture
def file_delete_system_based_template(config):
    yield
    remove_file(config, config.file_path)


@pytest.fixture
def file_delete_portfolio_reports(config):
    yield
    remove_file(config, get_file_path(config, get_common_data(config)["test_data"]["portfolio_report_data"]["pdf_name"]))
    remove_file(config, get_file_path(config, get_common_data(config)["test_data"]["portfolio_report_data"]["word_name"]))


@pytest.fixture
def file_delete_test_automation_document(config):
    yield
    remove_file(config, get_file_path(config, "Test Automation Document.pdf"))


@pytest.fixture
def file_delete_mi_reports(config):
    yield
    remove_file(config, get_file_path(config, get_common_data(config)["test_data"]["mi_report_data"]["pdf_name"]))
    remove_file(config, get_file_path(config, get_common_data(config)["test_data"]["mi_report_data"]["csv_name"]))


@pytest.fixture
def file_reset_import_statement_file_1_name(config):
    yield
    ElectronicImports(config).reset_import_statement_file_name("csv_file_1")


@pytest.fixture
def file_reset_import_statement_file_2_name(config):
    yield
    ElectronicImports(config).reset_import_statement_file_name("csv_file_2")


@pytest.fixture
def file_delete_import_statement(config):
    yield
    remove_file(config, get_file_path(config, get_common_data(config)["test_data"]["provider_statement_data"]["xls_name"]))


@pytest.fixture
def file_delete_fact_find_pdf(config):
    yield
    remove_file(config, get_file_path(config, get_common_data(config)["test_data"]["fact_find_data"]["pdf_name"]))


@pytest.fixture
def file_delete_leads_import_csv(config):
    yield
    remove_file(config, get_file_path(config, get_common_data(config)["test_data"]["lead_data"]["leads_import_file_name"]))


@pytest.fixture
def file_delete_client_data_file(config):
    yield
    remove_file(config, get_file_path(config, get_common_data(config)["test_data"]["fact_find_data"]["client_data_file_name"]))


@pytest.fixture
def file_delete_quote_document_pdf(config):
    yield
    remove_file(config, get_file_path(config, get_api_data(config, "create_quote_document")["object"]["original_filename"]))


@pytest.fixture
def file_delete_quote_result_document_pdf(config):
    yield
    remove_file(config, get_file_path(config, get_api_data(config, "create_quote_document")["object"]["original_filename"]))


# </editor-fold>

# <editor-fold desc="pfp fixtures"


@pytest.fixture
def ui_pfp_login_logout(config):
    PFPLogin(config).navigate_to_login_page().login()
    yield
    PFPLogin(config).logout()


@pytest.fixture
def ui_pfp_login(config):
    PFPLogin(config).navigate_to_login_page().login()


@pytest.fixture
def ui_pfp_accept_recommendation(config):
    PFPLogin(config).login_pfp_as_("pfp_imps_client")
    AcceptRecommendation(config).accept_recommendation()
    PFPLogin(config).logout()


@pytest.fixture
def ui_pfp_logout(config):
    yield
    PFPLogin(config).logout()


@pytest.fixture
def api_delete_client_dependants(config):
    yield
    client_id = utils.get_user_by_type(config, "pfp_client")["client_id"]
    dependants = client_dependants.get_dependants(config, client_id)
    for dependant in dependants["items"]:
        client_dependants.delete_dependant(config, client_id, dependant["id"])


@pytest.fixture
def api_add_dependant(config):
    client_id = utils.get_user_by_type(config, "pfp_client")["client_id"]
    client_dependants.add_dependant(config, client_id)


@pytest.fixture
def api_update_cff_client_personal_details(config):
    yield
    client_id = utils.get_user_by_type(config, "pfp_client")["client_id"]
    clients.update_cff_client_personal_data(config, client_id)


@pytest.fixture
def api_fill_in_about_you_segment_with_basic_details(config):
    client_id = utils.get_user_by_type(config, "pfp_client")["client_id"]
    clients.add_personal_details_to_cff_client(config, client_id)

# </editor-fold>