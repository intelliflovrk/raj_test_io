import datetime
import utils
from ioffice.clients.documents.documents import DocumentProfilePage


class DocumentProfile:
    def __init__(self, config):
        self.config = config
        self.page = DocumentProfilePage(self.config)

    def verify_uploaded_document(self):
        assert utils.get_temp_data(self.config, "document")["category"] == \
               self.page.get_category_text(), "Incorrect document category name"
        assert utils.get_temp_data(self.config, "document")['subcategory'] == \
               self.page.get_subcategory_text(), "Incorrect document subcategory name"
        assert datetime.datetime.now().strftime("%d/%m/%Y") in \
               self.page.get_created_on_date(), "Incorrect created on date"
