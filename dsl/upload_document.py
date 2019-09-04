import datetime
import time
import utils
from dsl.search import SearchClient
from ioffice.clients.client_dashboard import ClientDashboardPage, BaseClientPage
from ioffice.clients.documents.documents import ClientDocumentsPage, BaseDocumentsPage
from ioffice.clients.upload_document_dialog import UploadDocumentToClientDialog
from ioffice.leads.upload_document_dialog import UploadDocumentToLeadDialog
from ioffice.clients.documents.add_documents_to_binder_dialog import AddDocumentsToBinderDialog
from ioffice.clients.documents.binders import BindersPage
from ioffice.clients.documents.delete_binder_dialog import DeleteBinderDialog
from ioffice.clients.documents.delete_documents_dialog import DeleteDocumentDialog
from fakedata import rand_text


class UploadDocument(SearchClient):

    def __init__(self, config):
        super().__init__(config)

    def using_upload_document_dialog(self):
        ClientDashboardPage(self.config)\
            .client_actions_menu()\
            .hover_over_client_actions()\
            .click_upload_document()
        return UploadDocument._UploadDocumentDialog(ClientDashboardPage(self.config), self)

    def verify_document_uploaded(self):
        assert datetime.datetime.now().strftime("%d/%m/%Y") in ClientDocumentsPage(self.config).get_last_update_date(),\
            "Incorrect document updated date"
        return self

    class _UploadDocumentDialog:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = UploadDocumentToClientDialog(parent_page)

        def upload_pdf_document(self):
            self.dialog\
                .click_file_type()\
                .send_file_url()\
                .click_upload_button()
            return self.journey


class ClientDocuments(SearchClient):

    def open_client_documents(self):
        BaseClientPage(self.config)\
            .level3_menu()\
            .click_documents()
        return ClientDocuments._Documents(self)

    def open_client_binders(self):
        BaseClientPage(self.config)\
            .level3_menu()\
            .click_documents()
        BaseDocumentsPage(self.config)\
            .click_binders()
        return ClientDocuments._Binders(self)

    class _Documents:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = ClientDocumentsPage(self.config)

        def using_add_documents_to_binder(self):
            self.page.click_add_to_binder()
            return ClientDocuments._AddDocumentsToBinderDialog(self.page, self.journey)

        def add_documents_to_binder(self):
            self.page.click_select_all_documents()
            self.using_add_documents_to_binder()\
                .add_document_to_binder(self.config.binder)
            return self

        def using_delete_document_dialog(self):
            self.page.click_delete()
            return ClientDocuments._DeleteDocumentDialog(self.page, self.journey)

        def delete_documents(self):
            self.page.click_select_all_documents()
            self.using_delete_document_dialog().delete_document()
            return self

        def open_document(self):
            ClientDocumentsPage(self.config).click_open_first_document()
            return self

        def verify_document_added_to_binder(self):
            document_details = ClientDocumentsPage(self.config).get_first_table_row()
            assert self.config.binder in document_details, \
                f"The document {document_details} has not been added to the binder {self.config.binder}"
            return self

        def verify_document_opened(self):
            time.sleep(30)
            assert utils.open_downloaded_file(self, "Test Automation Document.pdf"), "Cannot open given file"
            return self

        def verify_documents_deleted(self):
            document_details = ClientDocumentsPage(self.config).get_first_table_row()
            assert 'There is no data to display' in document_details, \
                f"The Document {document_details} has not been deleted."

    class _AddDocumentsToBinderDialog:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = AddDocumentsToBinderDialog(parent_page)

        def add_document_to_binder(self, binder):
            self.dialog.select_binder(binder)\
                .click_add()\
                .close_io_dialog()
            return self.journey

    class _DeleteDocumentDialog:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = DeleteDocumentDialog(parent_page)

        def delete_document(self):
            self.dialog.click_yes()\
                .close_io_dialog()
            return self.journey

    class _Binders:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = BindersPage(self.config)

        def create_binder(self):
            self.config.binder = rand_text(5)
            self.page.fill_in_description(self.config.binder)\
                .click_create()\
                .wait_until_please_wait_spinner_present()
            return self

        def delete_binder(self):
            self.page.click_delete_first_binder()
            DeleteBinderDialog(self.page).click_yes()\
                .close_io_dialog()
            return self

