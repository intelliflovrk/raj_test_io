from selenium.webdriver.common.by import By
from ioffice.leads.base import BaseLeadPage


class LeadDocumentsPage(BaseLeadPage):

    def click_first_profile_link(self):
        return self.click(self.Locators.FIRST_PROFILE_LINK)

    def get_category_text(self):
        return self.get_drop_down_selected_value(self.Locators.SELECTED_CATEGORY_TEXT)

    def get_subcategory_text(self):
        return self.get_drop_down_selected_value(self.Locators.SELECTED_SUBCATEGORY_TEXT)

    def get_created_on_date(self):
        return self.get_text(self.Locators.CREATED_ON_TEXT)

    class Locators(object):
        CREATED_ON_TEXT = (By.ID, "id_CreatedDate_ro")
        SELECTED_CATEGORY_TEXT = (By.ID, "id_Document_Category")
        SELECTED_SUBCATEGORY_TEXT = (By.ID, "id_Document_SubCategory")
        FIRST_PROFILE_LINK = (By.CSS_SELECTOR, "a[href*='DocumentProfile']")
