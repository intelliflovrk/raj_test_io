from ioffice.leads.base import *


class LeadSearchPage(IOBasePage):

    def is_title_matches(self):
        return "Leads | Intelligent Office" == self.driver.title

    def click_add_lead(self):
        return self.click(LeadSearchPage.Locators.ADD_LEAD)

    def clear_first_name(self):
        return self.clear(LeadSearchPage.Locators.FIRST_NAME)

    def clear_last_name(self):
        return self.clear(LeadSearchPage.Locators.LAST_NAME)

    def fill_in_first_name(self, data):
        return self.fill_in_field(LeadSearchPage.Locators.FIRST_NAME, data)

    def fill_in_last_name(self, data):
        return self.fill_in_field(LeadSearchPage.Locators.LAST_NAME, data)

    def click_search_button(self):
        return self.click(LeadSearchPage.Locators.SEARCH)

    def click_open(self):
        return self.click(LeadSearchPage.Locators.OPEN)

    def select_lead_status_by_text(self, text):
        return self.select_by_visible_text(LeadSearchPage.Locators.LEAD_STATUS, text)

    class Locators(object):
        ADD_LEAD = (By.XPATH, "/html/body/div[5]/ul/li/a")
        FIRST_NAME = (By.CSS_SELECTOR, "#id_fname")
        LAST_NAME = (By.CSS_SELECTOR, "#id_lname")
        SEARCH = (By.CSS_SELECTOR, ".ux-ctl-form-action-buttons")
        OPEN = (By.CSS_SELECTOR, "tbody tr:nth-of-type(1) [title]")
        LEAD_STATUS = (By.ID, "id_Lead_LeadStatusId")
