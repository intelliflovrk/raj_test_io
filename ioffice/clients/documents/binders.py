from selenium.webdriver.common.by import By
from ioffice.clients.documents.base import BaseDocumentsPage


class BindersPage(BaseDocumentsPage):

    def fill_in_description(self, text):
        return self.fill_in_field(BindersPage.Locators.DESCRIPTION_FIELD, text)

    def click_create(self):
        return self.click(BindersPage.Locators.CREATE_BUTTON)

    def click_delete_first_binder(self):
        return self.click(BindersPage.Locators.FIRST_DELETE_BUTTON)

    class Locators(object):
        DESCRIPTION_FIELD = (By.ID, "id_Description")
        CREATE_BUTTON = (By.XPATH, "//table[@id='grid_BinderGrid']//a[text()='Create']")
        FIRST_DELETE_BUTTON = (By.XPATH, "//table[@id='grid_BinderGrid']//tr[2]//a[text()='Delete']")
