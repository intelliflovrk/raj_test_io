import datetime
import utils
from dsl.create_lead import CreateLead
from dsl.search import SearchLead
from ioffice.leads.documents import LeadDocumentsPage
from ioffice.leads.lead_details_page import LeadDetailsPage
from ioffice.leads.upload_document_dialog import UploadDocumentToLeadDialog


class UploadLeadDocument(CreateLead, SearchLead):

    def using_upload_document_dialog(self):
        lead_details_page = LeadDetailsPage(self.config)
        lead_details_page.lead_actions_menu()\
            .hover_over_lead_actions()\
            .click_upload_document()
        return UploadLeadDocument._UploadDocument(lead_details_page, self)

    def open_document(self):
        LeadDocumentsPage(self.config).click_first_profile_link()
        return self

    def verify_uploaded_document(self):
        assert utils.get_temp_data(self.config, "document")["category"] == LeadDocumentsPage(self.config).get_category_text(), \
            "Incorrect document category name"
        assert utils.get_temp_data(self.config, "document")['subcategory'] == LeadDocumentsPage(self.config).get_subcategory_text(), \
            "Incorrect document subcategory name"
        assert datetime.datetime.now().strftime("%d/%m/%Y") in LeadDocumentsPage(self.config).get_created_on_date(), \
            "Incorrect created on date"

    class _UploadDocument:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = UploadDocumentToLeadDialog(parent_page)

        def upload_pdf_document(self):
            utils.add_temp_data(self.config, "document", {"category": utils.get_common_data(
                self.config)["test_data"]["document_data"]["document_category"]})
            utils.update_temp_data(self.config, "document", 0, "subcategory", utils.get_common_data(
                self.config)["test_data"]["document_data"]["document_subcategory"])
            self.dialog \
                .click_file_type() \
                .select_document_category(utils.get_temp_data(self.config, "document")["category"]) \
                .select_document_subcategory(utils.get_temp_data(self.config, "document")['subcategory']) \
                .send_file_url() \
                .click_upload_button()
            return self.journey
