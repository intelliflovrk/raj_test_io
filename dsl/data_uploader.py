import utils
from dsl.create_lead import CreateLead
from ioffice.leads.lead_details_page import LeadDetailsPage
from utils import *
from ioffice.base import IOBasePage
from ioffice.data_upload_dialogs import DownloadTemplateDialog, ImportCompleteTemplateDialog
from ioffice.uploads import UploadsPage
from utils import get_download_folder, verify_file_is_downloaded


class DataUpload(CreateLead):

    def using_download_template_dialog(self):
        IOBasePage(self.config).level2_menu().click_uploads()
        UploadsPage(self.config).click_data_uploader().click_download_template()
        self.dialog = DataUpload._DownloadTemplates(self)
        return self.dialog

    def using_import_completed_template_dialog(self):
        IOBasePage(self.config).level2_menu().click_uploads()
        UploadsPage(self.config).click_data_uploader().click_import_completed_template()
        self.dialog = DataUpload._ImportCompletedTemplate(self)
        return self.dialog

    def verify_documents_downloaded(self):
        time.sleep(30)
        verify_file_is_downloaded(get_download_folder(self.config), "LeadsImport.csv")
        return self

    def save_lead_data(self):
        utils.add_temp_data(self.config, "lead", {"person": {
            "firstName": get_common_data(self.config)["test_data"]["lead_template_csv_data"]["lead_firstname"],
            "lastName": get_common_data(self.config)["test_data"]["lead_template_csv_data"]["lead_lastname"]}})
        return self

    def verify_uploaded_file(self):
        self.save_lead_data()
        time.sleep(30)
        UploadsPage(self.config).clear_file_name_field().fill_in_file_name_field("LeadsImport.csv").click_search_button()
        assert UploadsPage(self.config).get_status_value() == "Complete", "File not uploaded successfully"
        assert UploadsPage(self.config).get_failed_count_value() == "0", "File import failed"
        return self

    def verify_uploaded_data_synced(self):
        utils.update_temp_data(self.config, "lead", 0, "id", LeadDetailsPage(self.config).get_lead_id())
        assert LeadDetailsPage(self.config).get_full_name_value() == utils.get_temp_data(
            self.config, "lead")["person"]["firstName"] + " " + utils.get_temp_data(
            self.config, "lead")["person"]["lastName"], "Lead not found"
        return self

    class _DownloadTemplates:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = DownloadTemplateDialog(self.config)

        def download_import_leads_template(self):
            self.dialog\
                .click_import_leads()\
                .click_close_button()
            return self.journey

    class _ImportCompletedTemplate:

        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ImportCompleteTemplateDialog(self.config)

        def upload_template(self, template):
            self.dialog\
                .select_import_type(template)\
                .send_file_url()\
                .click_upload_button()
            return self.journey
