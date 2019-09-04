from selenium.common.exceptions import TimeoutException

import utils
from dsl.search import SearchClient
from ioffice.clients.base import GenerateMenu
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.generate_document_dialog import GenerateDocumentDialog
from ioffice.clients.documents.document_queue import ClientDocumentQueuePage, BaseDocumentsPage
from utils import *
import time
import datetime
from datetime import date, datetime


class GenerateDocument(SearchClient):
    def __init__(self, config):
        super().__init__(config)

    def using_generate_menu(self):
        return GenerateDocument._GenerateMenu(ClientDashboardPage(self.config), self)

    def using_document_generation_dialog(self):
        return GenerateDocument._GenerateTemplateDialog(ClientDashboardPage(self.config), self)

    def assert_if_document_queue_open(self):
        assert ClientDocumentQueuePage(self.config).is_title_matches()
        return self

    def refresh_document_queue(self):
        ClientDocumentQueuePage(self.config).click_refresh().wait_until_please_wait_spinner_present()
        return self

    def assert_if_pdf_doc_generated(self):
        client_document_queue_page = ClientDocumentQueuePage(self.config)
        documents_list = client_document_queue_page.get_documents_table_str_list()
        data = get_common_data(self.config)["test_data"]["document_data"]
        assert utils.is_string_present(documents_list, data["PDF_TYPE"]), "PDF document is not found"

    @retry(AssertionError)
    def wait_until_document_completed(self):
        data = get_common_data(self.config)["test_data"]["document_data"]
        self.refresh_document_queue()\
            .verify_if_document_status_is(data["COMPLETED_STATUS"])
        return self

    @retry(TimeoutException)
    def download_document_once_ready(self):
        self.refresh_document_queue()
        ClientDocumentQueuePage(self.config).click_download()
        return self

    def verify_if_document_status_is(self, status):
        doc_queue_page = ClientDocumentQueuePage(self.config)
        docs_details = get_str_list_from_list_of_webelements(doc_queue_page.get_documents_table_rows())
        assert utils.is_string_present(docs_details, status),\
            "Expected document status is {0}. Actual documents details are {1}".format(status, docs_details)
        return self

    def open_document_once_completed(self):
        self.download_document_once_ready()
        time.sleep(30)
        self.config.file_path = get_file_path(self.config, get_files_in_folder(self.config.temp_download_folder)[0])
        self.document = open_docx_file(self.config.file_path)
        return self

    def verify_joint_client_populated_on_first_page(self):
        first_client = get_temp_data(self.config, "client")
        first_page = get_text_from_docx_section(self.document, '//w:txbxContent//w:t/text()')
        assert first_client["person"]["firstName"] in first_page, \
            f"Client 1 First Name {first_client['person']['firstName']} is not found in {first_page}."
        assert first_client["person"]["lastName"] in first_page, \
            f"Client 1 Last Name {first_client['person']['lastName']} is not found in {first_page}."
        second_client = get_temp_data(self.config, "client", 1)
        assert second_client["person"]["firstName"] in first_page, \
            f"Client 2 First Name {second_client['person']['firstName']} is not found in {first_page}."
        assert second_client["person"]["lastName"] in first_page, \
            f"Client 2 Last Name {second_client['person']['lastName']} is not found in {first_page}."
        return self

    def verify_published_date_equals_to_current_date(self):
        first_page = get_text_from_docx_section(self.document, '//w:txbxContent//w:t/text()')
        assert date.today().strftime('%d/%m/%Y') in first_page, "Current Date {0} is not found in {1}".format(date.today().strftime('%d/%m/%Y'), first_page)
        return self

    def verify_client_address_captured(self):
        address = get_temp_data(self.config, "address")
        first_page = get_text_from_docx_section(self.document, '//w:t/text()')
        assert address["address"]["line1"] in first_page, \
            f"Client address line 1 {address['address']['line1']} is not found in {first_page}."
        assert address["address"]["line2"] in first_page, \
            f"Client address line 2 {address['address']['line2']} is not found in {first_page}."
        assert address["address"]["postalCode"] in first_page, \
            f"Client postcode {address['address']['postalCode']} is not found in {first_page}."
        return self

    def verify_wrap_policy_number_captured(self):
        wrap_policy_number = get_text_from_docx_section(self.document, "(//w:r/w:t[contains(text(),'Wrap')]/ancestor::w:r/following-sibling::w:r[4]//w:t/text())[1]")
        assert self.config.plan_wrap["policyNumber"] in wrap_policy_number,\
            f"Expected Wrap Policy Number is {self.config.plan_wrap['policyNumber']}. " \
            f"Actual Wrap Policy Number is {wrap_policy_number}"
        return self

    def verify_investment_policy_number_captured(self):
        investment_policy_number = get_text_from_docx_section(self.document, "(//w:r/w:t[contains(text(),'ISA (Stocks And Shares)')]/ancestor::w:r/following-sibling::w:r[3]//w:t/text())[1]")
        assert self.config.plan["policyNumber"] in investment_policy_number,\
            f"Expected Investment Policy Number is {self.config.plan['policyNumber']}. " \
            f"Actual Investment Policy Number is {investment_policy_number}"
        return self

    def verify_wrap_policy_start_date_captured(self):
        current_wrap_values = get_text_from_docx_section(self.document, "(//w:tbl//w:r/w:t[contains(text(),'Commenced Date')]/ancestor::w:tc/following-sibling::w:tc//w:r//w:t/text())[1]")
        expected_wrap_policy_start_date = datetime.strptime(self.config.plan_wrap["startsOn"], '%Y-%m-%d').strftime("%d/%m/%Y")
        assert expected_wrap_policy_start_date in current_wrap_values,\
            f"Expected Wrap Start Date is {expected_wrap_policy_start_date}. " \
            f"Actual Wrap Start Date is {current_wrap_values}"
        return self

    def assert_contribution_amount_captured(self, path):
        contribution = get_temp_data(self.config, "contribution")
        current_contribution_amount = get_text_from_docx_section(self.document, path)
        expected_contribution_amount = '£' + '{:,.2f}'.format(float(contribution["value"]["amount"]))
        assert expected_contribution_amount in current_contribution_amount, \
            f"Expected Contribution Amount is {expected_contribution_amount}. " \
            f"Actual Contribution Amount is {current_contribution_amount}"
        return self

    def verify_wrap_contribution_amount_captured(self):
        self.assert_contribution_amount_captured("//w:p[@w:rsidP='00E6133C']//w:t/text()")
        return self

    def verify_investment_contribution_amount_captured(self):
        self.assert_contribution_amount_captured("(//w:tbl//w:r/w:t[contains(text(),'Total Investment')]/ancestor::w:tc/following-sibling::w:tc//w:r//w:t/text())[1]")
        return self

    def assert_withdrawal_amount_captured(self, path):
        withdrawal = get_temp_data(self.config, "withdrawal")
        current_withdrawal_amount = get_text_from_docx_section(self.document, path)
        expected_withdrawal_amount = '£' + '{:,.2f}'.format(float(withdrawal["value"]["amount"]))
        assert expected_withdrawal_amount in current_withdrawal_amount, \
            f"Expected Withdrawal Amount is {expected_withdrawal_amount}. " \
            f"Actual Withdrawal Amount is {current_withdrawal_amount}"
        return self

    def verify_wrap_withdrawal_amount_captured(self):
        self.assert_withdrawal_amount_captured("//w:p[@w:rsidP='00E6133C']//w:t/text()")
        return self

    def verify_investment_withdrawal_amount_captured(self):
        self.assert_withdrawal_amount_captured("(//w:tbl//w:r/w:t[contains(text(),'Total Withdrawals')]/ancestor::w:tc/following-sibling::w:tc//w:r//w:t/text())[1]")
        return self

    def verify_wrap_valuation_details_captured(self):
        valuation = get_temp_data(self.config, "valuation")
        current_wrap_valuation_date = get_text_from_docx_section(self.document, "(//w:tbl//w:r/w:t[contains(text(),'Valuation Date')]/ancestor::w:tc/following-sibling::w:tc//w:r//w:t/text())[1]")
        expected_wrap_valuation_date = datetime.strptime(valuation["valuedOn"][:10], '%Y-%m-%d').strftime("%d/%m/%Y")
        assert expected_wrap_valuation_date in current_wrap_valuation_date,\
            f"Expected Wrap Valuation Date is {expected_wrap_valuation_date}. " \
            f"Actual Wrap Valuation Date is {current_wrap_valuation_date}"
        current_wrap_values = get_text_from_docx_section(self.document, "//w:r[@w:rsidRPr='000D7C50']//w:t/text()")
        expected_wrap_current_value = '£' + '{:,.2f}'.format(float(valuation["value"]["amount"]))
        assert expected_wrap_current_value in current_wrap_values,\
            f"Expected Wrap Valuation Amount is {expected_wrap_current_value}. " \
            f"Actual Wrap Valuation Amount is {current_wrap_values}"
        return self

    def verify_investment_valuation_details_captured(self):
        valuation = get_temp_data(self.config, "valuation")
        current_investment_valuation_date = get_text_from_docx_section(self.document, "(//w:tbl//w:r/w:t[contains(text(),'Valuation Date')]/ancestor::w:tc/following-sibling::w:tc//w:r//w:t/text())[1]")
        expected_investment_valuation_date = datetime.strptime(valuation["valuedOn"][:10], "%Y-%m-%d").strftime("%d/%m/%Y")
        assert expected_investment_valuation_date in current_investment_valuation_date, \
            f"Expected Investment Valuation Date is {expected_investment_valuation_date}. " \
            f"Actual Investment Valuation Date is {current_investment_valuation_date}"
        current_investment_values = get_text_from_docx_section(self.document, "(//w:tbl//w:r/w:t[contains(text(),'Current Value')]/ancestor::w:tc/following-sibling::w:tc//w:r//w:t/text())[1]")
        expected_investment_current_value = '£' + '{:,.2f}'.format(float(valuation["value"]["amount"]))
        assert expected_investment_current_value in current_investment_values, \
            f"Expected Investment Valuation Amount is {expected_investment_current_value}. " \
            f"Actual Investment Valuation Amount is {current_investment_values}"
        return self

    def verify_wrap_note_captured(self):
        current_wrap_values = get_text_from_docx_section(self.document, "//w:r[@w:rsidRPr='000D7C50']//w:t/text()")
        assert self.config.plan_report_note in current_wrap_values,\
            f"Expected Wrap Note is {self.config.plan_report_note}. " \
            f"Actual Wrap Note is {current_wrap_values}"
        return self

    def verify_sub_plan_policy_number_captured(self):
        current_sub_plan_policy_number = get_text_from_docx_section(self.document, "//w:p[@w:rsidRPr='00B02049']//w:t/text()")
        assert self.config.plan["policyNumber"] in current_sub_plan_policy_number,\
            f"Expected Sub-Plan Policy Number is {self.config.plan['policyNumber']}. " \
            f"Actual Sub-Plan Policy Number is {current_sub_plan_policy_number}"
        return self

    def verify_sub_plan_valuation_details_captured(self):
        valuation = get_temp_data(self.config, "valuation", 1)
        current_sub_plan_details = get_text_from_docx_section(self.document, "//w:p[@w:rsidRPr='00B02049']//w:t/text()")
        expected_sub_plan_valuation_date = datetime.strptime(valuation["valuedOn"][:10], '%Y-%m-%d').strftime("%d/%m/%Y")
        assert expected_sub_plan_valuation_date in current_sub_plan_details,\
            f"Expected Sub-Plan Valuation Date is {expected_sub_plan_valuation_date}. " \
            f"Actual Sub-Plan Details is {current_sub_plan_details}"
        expected_sub_plan_value = '£' + '{:,.2f}'.format(float(valuation["value"]["amount"]))
        assert expected_sub_plan_value in current_sub_plan_details,\
            f"Expected Sub-Plan Value is {expected_sub_plan_value}. " \
            f"Actual Sub-Plan Details is is {current_sub_plan_details}"
        return self

    def assert_fund_details_captured(self, path):
        fund_holding = get_temp_data(self.config, "fund_holding")
        current_fund_details = get_text_from_docx_section(self.document, path)
        assert fund_holding["fund"]["name"] in current_fund_details, \
            f"Expected Fund Name is {fund_holding['fund']['name']}. " \
            f"Actual Fund Details are {current_fund_details}"
        expected_fund_holding_price_date = datetime.strptime(fund_holding["units"]["priceUpdatedOn"],
                                                             '%Y-%m-%dT%H:%M:%SZ').strftime("%d/%m/%Y")
        assert expected_fund_holding_price_date in current_fund_details, \
            f"Expected Fund Price Date is {expected_fund_holding_price_date}. " \
            f"Actual Fund Details are {current_fund_details}"
        expected_units_number = '{:.2f}'.format(float(fund_holding["units"]["number"]))
        assert expected_units_number in current_fund_details, \
            f"Expected Fund Units Number is {expected_units_number}. " \
            f"Actual Fund Details are {current_fund_details}"
        expected_units_price = '£' + '{:.2f}'.format(float(fund_holding["units"]["price"]["amount"]))
        assert expected_units_price in current_fund_details, \
            f"Expected Fund Units Number is {expected_units_price}. " \
            f"Actual Fund Details are {current_fund_details}"
        return self

    def verify_sub_plan_fund_details_captured(self):
        self.assert_fund_details_captured("//w:tbl//w:p[@w:rsidP='00F878B1']//w:t/text()")
        return self

    def verify_investment_fund_details_captured(self):
        self.assert_fund_details_captured("//w:tbl//w:p[@w:rsidP='005662A8']//w:t/text()")
        return self

    def verify_wrap_plan_details_captured(self):
        self.verify_wrap_policy_number_captured()\
            .verify_wrap_policy_start_date_captured()\
            .verify_wrap_contribution_amount_captured()\
            .verify_wrap_withdrawal_amount_captured()\
            .verify_wrap_valuation_details_captured()\
            .verify_wrap_note_captured()
        return self

    def verify_sub_plan_details_captured(self):
        self.verify_sub_plan_policy_number_captured()\
            .verify_sub_plan_valuation_details_captured()\
            .verify_sub_plan_fund_details_captured()
        return self

    def verify_investment_plan_details_captured(self):
        self.verify_investment_policy_number_captured()\
            .verify_investment_contribution_amount_captured()\
            .verify_investment_withdrawal_amount_captured() \
            .verify_investment_valuation_details_captured()\
            .verify_investment_fund_details_captured()
        return self

    def open_document_queue(self):
        ClientDashboardPage(self.config).level3_menu().click_documents()
        BaseDocumentsPage(self.config).click_document_queue()
        return self

    def clear_document_queue(self):
        doc_queue_page = ClientDocumentQueuePage(self.config)
        doc_queue_page.check_select_all_documents()\
            .click_delete()\
            .click_ok_in_browser_confirmation_dialog()
        doc_queue_page.wait_until_please_wait_spinner_present()
        return self

    class _GenerateMenu:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.menu = GenerateMenu(parent_page)

        def select_category(self, category):
            client_dashboard_page = ClientDashboardPage(self.config)
            categorieslist = client_dashboard_page.hover_over_generate().get_categories_list()
            client_dashboard_page\
                .hover_over_generate()\
                .click_category(get_web_element_from_list_by_text(categorieslist, category))
            return self.journey

        def generate_pdf_basic_template(self):
            data = get_common_data(self.config)["test_data"]["basic_template"]
            self.select_category(data["CATEGORY_NAME"])\
                .using_document_generation_dialog()\
                .select_template(data["TEMPLATE_NAME"])\
                .generate_pdf_doc()
            return self.journey

        def generate_portfolio_report_system_based_template_for_joint_client(self):
            data = get_common_data(self.config)["test_data"]["portfolio_report_system_based_template"]
            second_client = get_temp_data(self.config, "client", 1)
            self.select_category(data["CATEGORY_NAME"])\
                .using_document_generation_dialog()\
                .select_template(data["TEMPLATE_NAME"])\
                .select_relationships(second_client["name"])\
                .skip_step()\
                .generate_word_doc()
            return self.journey

        def generate_address_template_for_client(self):
            data = get_common_data(self.config)["test_data"]["test_automation_address_template"]
            self.select_category(data["CATEGORY_NAME"])\
                .using_document_generation_dialog()\
                .select_template(data["TEMPLATE_NAME"]) \
                .generate_word_doc()
            return self.journey

        def generate_portfolio_report_system_based_template_with_wrap_investments(self):
            data = get_common_data(self.config)["test_data"]["portfolio_report_system_based_template"]
            self.select_category(data["CATEGORY_NAME"])\
                .using_document_generation_dialog()\
                .select_template(data["TEMPLATE_NAME"])\
                .skip_step()\
                .select_prompt_option()\
                .generate_word_doc()
            return self.journey

        def generate_portfolio_report_system_based_template_with_investments(self):
            data = get_common_data(self.config)["test_data"]["portfolio_report_system_based_template"]
            self.select_category(data["CATEGORY_NAME"]) \
                .using_document_generation_dialog() \
                .select_template(data["TEMPLATE_NAME"]) \
                .skip_step() \
                .skip_step() \
                .generate_word_doc()
            return self.journey
            
    class _GenerateTemplateDialog:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = GenerateDocumentDialog(parent_page)

        def select_template(self, template):
            templateslist = self.dialog.template_step().get_templates_list()
            radiobuttonslist = self.dialog.template_step().get_radiobuttons_list()
            for i in range(len(templateslist)):
                if template in templateslist[i].text:
                    radiobuttonslist[i].click()
            self.dialog.click_next()
            return self

        def select_relationships(self, relationships):
            self.dialog.context_step().\
                select_relationships(relationships)\
                .wait_until_please_wait_spinner_present()
            self.dialog.click_next()
            return self

        def skip_step(self):
            time.sleep(3)
            self.dialog.click_next()
            return self

        def select_prompt_option(self):
            self.dialog.prompt_step()\
                .check_first_checkbox()
            self.dialog.click_next()
            return self

        def generate_word_doc(self):
            self.dialog.click_finish()
            self.dialog.close_io_dialog()
            return self.journey

        def generate_pdf_doc(self):
            self.dialog.finish_step().select_pdf_type()
            self.dialog.click_finish()
            self.dialog.close_io_dialog()
            return self.journey
