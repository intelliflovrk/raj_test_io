from dsl.search import SearchClient
from dsl.create_plan_from_quote import CreatePlanFromQuote
from dsl.upload_document import ClientDocuments
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.documents.documents import ClientDocumentsPage
from ioffice.clients.quotes.get_quote_for_client import GetQuoteForClientPage
from ioffice.clients.quotes.get_illustration_for_client import GetIllustrationForClientPage
from ioffice.clients.quotes.quotes_apps import QuotesAppsPage
from ioffice.clients.quotes.quotes_illustrations import QuotesIllustrationsPage
from ioffice.clients.quotes.quote_result_summary import QuoteResultSummaryPage
from ioffice.clients.quotes.quote_result_documents import QuoteResultDocumentsPage
from ioffice.clients.quotes.quote_result_document_dialog import QuoteResultDocumentDialog
from ioffice.clients.quotes.quote_result_details_dialog import QuoteResultDetailsDialog
import utils
from utils import *


class GetClientQuote(SearchClient, CreatePlanFromQuote):

    def navigate_to_quotes_and_apps(self):
        ClientDashboardPage(self.config).level3_menu().click_quotes_apps()
        QuotesAppsPage(self.config).click_quotes_apps()
        return GetClientQuote._QuotesAndApps(self)

    def navigate_to_quotes_and_illustrations(self):
        ClientDashboardPage(self.config).level3_menu().click_quotes_apps()
        QuotesAppsPage(self.config).click_quotes_illustrations()
        return self

    def open_quote(self):
        self.navigate_to_quotes_and_illustrations().open_quote_by_reference()
        return self

    def navigate_to_quote_documents_tab(self):
        QuoteResultSummaryPage(self.config).click_documents_tab()
        return self

    def using_get_new_quote_window(self):
        ClientDashboardPage(self.config) \
            .client_actions_menu() \
            .hover_over_client_actions() \
            .click_get_quote()
        utils.switch_to_window_by_name(self, "legacyPopup")
        return self

    def select_quote_product_area(self, product):
        GetQuoteForClientPage(self.config).click_product_area(product).wait_until_please_wait_spinner_present()
        return self

    def verify_quote_app_exists(self, app_name):
        assert GetQuoteForClientPage(self.config).get_app(app_name), "App does not exist"
        return self

    def open_quote_app(self, app_name):
        GetQuoteForClientPage(self.config).click_quote_app(app_name)
        return self

    def get_assureweb_quote(self):
        data = utils.get_common_data(self.config)["test_data"]["assureweb_quote"]
        GetQuoteForClientPage(self.config).click_next() \
            .select_product_type(data["PRODUCT_TYPE"]) \
            .fill_in_age_field(data["AGE"]) \
            .fill_in_min_life_amount_field(data["MIN_COVER"]) \
            .click_next() \
            .click_next() \
            .check_all_checkboxes() \
            .click_next() \
            .click_complete()
        utils.switch_to_parent_window(self)
        return self

    def using_get_new_illustration_window(self):
        ClientDashboardPage(self.config) \
            .client_actions_menu() \
            .hover_over_client_actions() \
            .click_get_illustration()
        utils.switch_to_window_by_name(self, "legacyPopup")
        return self

    def select_illustration_product_area(self, product):
        GetIllustrationForClientPage(self.config).click_product_area(product)
        return self

    def verify_illustration_app_exists(self, app_name):
        assert GetIllustrationForClientPage(self.config).get_app(app_name), "App does not exist"
        return self

    def close_get_new_ilustration_window(self):
        utils.close_current_window(self)
        utils.switch_to_parent_window(self)
        return self

    @retry(AssertionError, 60)
    def wait_until_quote_illustration_completed(self):
        quote = get_temp_data(self.config, "quote")
        QuotesIllustrationsPage(self.config).fill_in_reference_filter(quote["reference"])\
            .click_filter()\
            .click_refresh() \
            .wait_until_please_wait_spinner_present()
        self.verify_quote_illustration_status_is("Complete")
        return self

    def verify_quote_illustration_status_is(self, status):
        current_status = QuotesIllustrationsPage(self.config).get_quote_status()
        assert current_status == status, f"Expected quote status is '{status}'. Actual quote status is '{current_status}'."
        return self

    def verify_quote_illustration_product_type_is(self, product_type):
        observed_product_type = QuotesIllustrationsPage(self.config).get_product_type()
        assert observed_product_type == product_type, \
            f"Expected product type is {product_type}. Observed product type is {observed_product_type}"
        return self

    def verify_provider_is_app_name(self):
        provider = QuotesIllustrationsPage(self.config).get_provider()
        assert provider == "App for Automated API Testing", "Provider does not match the app name"
        return self

    def verify_quote_reference(self):
        quote_reference = QuotesIllustrationsPage(self.config).get_quote_reference()
        assert quote_reference == get_api_data(self.config, "create_quote")[
            "customReference"], "Quote reference is not correct"
        return self

    def open_quote_by_reference(self):
        QuotesIllustrationsPage(self.config).click_first_reference()
        return self

    def verify_joint_quote_result_created(self):
        expected_joint_state = get_common_data(self.config)["test_data"]["quote_result_summary"]["joint"]
        observed_joint_state = QuoteResultSummaryPage(self.config).get_joint_state()
        assert expected_joint_state == observed_joint_state, \
            f"Expected JointState is {expected_joint_state}. Observed Joint State is {observed_joint_state}"
        return self

    def verify_document_has_been_uploaded_for_quote(self):
        assert QuoteResultDocumentsPage(self.config).get_document_title() == \
               get_api_data(self.config, "create_quote_document")["title"], "Document title is incorrect."
        assert QuoteResultDocumentsPage(self.config).get_document_description() == \
               get_api_data(self.config, "create_quote_document")[
                   "description"], "Document description is incorrect."
        assert QuoteResultDocumentsPage(self.config).get_document_category() == \
               get_api_data(self.config, "create_quote_document")["properties"][
                   "_category.name"], "Document category is incorrect."
        assert QuoteResultDocumentsPage(self.config).get_document_subcategory() == \
               get_api_data(self.config, "create_quote_document")["properties"][
                   "_subCategory.name"], "Document subcategory is incorrect."
        return self

    def download_quote_document(self):
        QuoteResultDocumentsPage(self.config).click_view_button()
        return self

    def verify_quote_document_downloaded(self):
        time.sleep(5)
        url = get_download_folder(self.config)
        verify_file_is_downloaded(url, "Test Automation Quote Document.pdf")
        return self

    def verify_columns_are_present_for_protection_quote_results(self):
        self.verify_provider_column_present() \
            .verify_total_single_contributions_column_present() \
            .verify_total_regular_contributions_column_present() \
            .verify_total_transfer_contributions_column_present() \
            .verify_joint_column_present()
        return self

    def verify_provider_column_present(self):
        assert QuoteResultSummaryPage(
            self.config).get_first_column_name() == "Provider/Product", "column is not present or incorrect"
        return self

    def verify_total_single_contributions_column_present(self):
        assert QuoteResultSummaryPage(
            self.config).get_second_column_name() == "Total Single Contributions", "column is not present or incorrect"
        return self

    def verify_total_regular_contributions_column_present(self):
        assert QuoteResultSummaryPage(
            self.config).get_third_column_name() == "Total Regular Contributions", "column is not present or incorrect"
        return self

    def verify_total_transfer_contributions_column_present(self):
        assert QuoteResultSummaryPage(
            self.config).get_forth_column_name() == "Total Transfer Contributions", "column is not present or incorrect"
        return self

    def verify_joint_column_present(self):
        assert QuoteResultSummaryPage(
            self.config).get_fifth_column_name() == "Joint", "column is not present or incorrect"
        return self

    def verify_contribution_amounts_are_correct(self):
        assert QuoteResultSummaryPage(self.config).get_second_column_value() == '£' + '{:,.2f}'.format(
            float(get_api_data(self.config, "create_quote_result")["contributions"][0]["value"][
                      "amount"])), "Single contribution amount is incorrect"
        assert QuoteResultSummaryPage(self.config).get_third_column_value() == '£' + '{:,.2f}'.format(
            float(get_api_data(self.config, "create_quote_result")["contributions"][1]["value"][
                      "amount"])), "Regular contribution amount is incorrect"
        assert QuoteResultSummaryPage(self.config).get_forth_column_value() == '£' + '{:,.2f}'.format(
            float(get_api_data(self.config, "create_quote_result")["contributions"][2]["value"][
                      "amount"])), "Transfer contribution amount is incorrect"
        return self

    def verify_quote_id(self):
        observed_quote_id = QuoteResultSummaryPage(self.config).get_quote_id_from_url()
        expected_quote_id = str(get_temp_data(self.config, "quote")["id"])
        assert observed_quote_id == expected_quote_id, \
            f"Incorrect Quote ID. Expected Result is {expected_quote_id}. Actual result is {observed_quote_id}"
        return self

    def using_quote_result_details_dialog(self):
        QuoteResultSummaryPage(self.config).click_details_button()
        return GetClientQuote._QuoteResultDetailsDialog(QuoteResultSummaryPage(self.config), self)

    def using_quote_result_document_dialog(self):
        QuoteResultSummaryPage(self.config).click_docs_button()
        return GetClientQuote._QuoteResultDocumentDialog((QuoteResultSummaryPage(self.config)), self)

    def navigate_to_client_document(self):
        ClientDocuments(self.config).open_client_documents()
        return self

    def verify_quote_document_present(self):
        assert "Test Automation Quote Document" in ClientDocumentsPage(
            self.config).get_first_table_row(), "Quote Document not found"
        return self

    def verify_quote_result_document_present(self):
        assert get_api_data(self.config, "create_quote_result_document")["title"] in ClientDocumentsPage(
            self.config).get_first_table_row(), "Quote result document not found"
        return self

    def open_second_life(self):
        self.open_client_by_url(get_temp_data(self.config, "client", 1)["id"])
        return self

    class _QuoteResultDocumentDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = QuoteResultDocumentDialog(current_page)

        def verify_document_has_been_uploaded_for_quote_result(self):
            assert self.dialog.get_document_title() == \
                   get_api_data(self.config, "create_quote_result_document")[
                       "title"], "Document title is incorrect."
            assert self.dialog.get_document_description() == \
                   get_api_data(self.config, "create_quote_result_document")[
                       "description"], "Document description is incorrect."
            assert self.dialog.get_document_category() == \
                   get_api_data(self.config, "create_quote_result_document")["properties"][
                       "_category.name"], "Document category is incorrect."
            assert self.dialog.get_document_subcategory() == \
                   get_api_data(self.config, "create_quote_result_document")["properties"][
                       "_subCategory.name"], "Document subcategory is incorrect."
            return self

        def download_quote_result_document(self):
            self.dialog.click_view_button()
            return self

        def verify_quote_result_document_downloaded(self):
            time.sleep(5)
            url = get_download_folder(self.config)
            verify_file_is_downloaded(url, "Test Automation Quote Result Document.pdf")
            return self

        def close_dialog(self):
            self.dialog.click_close_button()
            return self.journey

    class _QuoteResultDetailsDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = QuoteResultDetailsDialog(current_page)

        def verify_columns_for_investment_quote_are_correct(self):
            assert self.dialog.get_first_column_title() == "Contribution Type(s)", "column is not present or incorrect"
            assert self.dialog.get_second_column_title() == "Amount", "column is not present or incorrect"
            assert self.dialog.get_third_column_title() == "Frequency", "column is not present or incorrect"
            return self

        def verify_contributions_are_correct_for_investment_quote(self):
            lump_sum_contribution_values = get_str_list_from_list_of_webelements(
                self.dialog.get_first_row_values())
            data = get_api_data(self.config, "create_quote_result")["contributions"][0]["type"]
            expected_result = data[:4] + " " + data[-3:]
            assert utils.is_string_present(lump_sum_contribution_values,
                                           expected_result), "Contribution type is incorrect"
            assert utils.is_string_present(lump_sum_contribution_values, '£' + '{:,.2f}'.format(float(
                get_api_data(self.config, "create_quote_result")["contributions"][0]["value"][
                    "amount"]))), "Contribution amount is incorrect"
            assert utils.is_string_present(lump_sum_contribution_values,
                                           get_api_data(self.config, "create_quote_result")["contributions"][
                                               0]["frequency"]), "Contribution frequency is incorrect"

            regular_contribution_values = get_str_list_from_list_of_webelements(
                self.dialog.get_second_row_values())
            assert utils.is_string_present(regular_contribution_values,
                                           get_api_data(self.config, "create_quote_result")["contributions"][
                                               1]["type"]), "Contribution type is incorrect"
            assert utils.is_string_present(regular_contribution_values, '£' + '{:,.2f}'.format(float(
                get_api_data(self.config, "create_quote_result")["contributions"][1]["value"][
                    "amount"]))), "Contribution amount is incorrect"
            assert utils.is_string_present(regular_contribution_values,
                                           get_api_data(self.config, "create_quote_result")["contributions"][
                                               1]["frequency"]), "Contribution frequency is incorrect"

            transfer_contribution_values = get_str_list_from_list_of_webelements(
                self.dialog.get_third_row_values())
            assert utils.is_string_present(transfer_contribution_values,
                                           get_api_data(self.config, "create_quote_result")["contributions"][
                                               2]["type"]), "Contribution type is incorrect"
            assert utils.is_string_present(transfer_contribution_values, '£' + '{:,.2f}'.format(float(
                get_api_data(self.config, "create_quote_result")["contributions"][2]["value"][
                    "amount"]))), "Contribution amount is incorrect"
            assert utils.is_string_present(transfer_contribution_values,
                                           get_api_data(self.config, "create_quote_result")["contributions"][
                                               2]["frequency"]), "Contribution frequency is incorrect"
            return self

        def close_dialog(self):
            self.dialog.click_close_button()
            return self.journey

    class _QuotesAndApps:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = QuotesAppsPage(self.config)

        def open_quote(self):
            self.page.click_first_open_link()
            return self.journey

        @retry(AssertionError, 60)
        def wait_until_quote_completed(self):
            QuotesAppsPage(self.config).click_refresh() \
                .wait_until_please_wait_spinner_present()
            self.verify_quote_status_is("Complete")
            return self

        def delete_quote(self):
            self.page.select_first_row()\
                .click_delete()
            utils.switch_and_accept_alert(self.config)
            return self

        def verify_quote_status_is(self, status):
            current_status = QuotesAppsPage(self.config).get_quote_status()
            assert current_status == status, f"Expected quote status is '{status}'. Actual quote status is '{current_status}'."
            return self

        def verify_quote_product_type_is_term(self):
            product_type = QuotesAppsPage(self.config).get_product_type()
            assert product_type == "Term", "Product Type is not correct"
            return self
