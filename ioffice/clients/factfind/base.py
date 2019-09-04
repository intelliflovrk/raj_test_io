from ioffice.base import *
from ioffice.userdashboard import *
from selenium.webdriver.common.by import By
import re


class BaseFactFindPage(IOBasePage):

    def is_title_matches(self):
        return "Adviser Workplace | Clients | Fact Find | Intelligent Office" == self.driver.title

    def click_protection_tab(self):
        return self.click(BaseFactFindPage.Locators.PROTECTION_TAB)

    def factfind_actions_menu(self):
        return FactFindActionsMenuSection(self)

    def _get_factfind_ref(self):
        return re.search(
            r'(?<=factfind/)(\{){0,1}[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}(\}){0,1}',
            self.driver.current_url).group(0)

    def click_next_button(self):
        return self.click(BaseFactFindPage.Locators.NEXT_BUTTON)

    def click_save_button(self):
        return self.click(BaseFactFindPage.Locators.SAVE_BUTTON)

    def click_employment_tab(self):
        return self.click(BaseFactFindPage.Locators.EMPLOYMENT_TAB)

    def click_asset_and_liabilities_tab(self):
        return self.click(BaseFactFindPage.Locators.ASSET_LIABILITIES_TAB)

    def click_budget_tab(self):
        return self.click(BaseFactFindPage.Locators.BUDGET_TAB)

    def click_retirement_tab(self):
        return self.click(BaseFactFindPage.Locators.RETIREMENT_TAB)

    def click_estate_planning_tab(self):
        return self.click(BaseFactFindPage.Locators.ESTATE_PLANNING)

    def click_summary_tab(self):
        return self.click(BaseFactFindPage.Locators.SUMMARY_TAB)

    def click_profile_tab(self):
        return self.click(BaseFactFindPage.Locators.PROFILE_TAB)

    def click_mortgage_tab(self):
        return self.click(BaseFactFindPage.Locators.MORTGAGE_TAB)

    def click_save_form_button(self):
        return self.click(BaseFactFindPage.Locators.SAVE_FORM_BUTTON)

    class Locators(object):
        NEXT_BUTTON = (By.ID, "ff-form-next")
        SAVE_BUTTON = (By.ID, "ff-form-savebar")
        SAVE_FORM_BUTTON = (By.ID, "ff-form-save")
        FACTFIND_ACTIONS_MENU = (By.ID, "secondary")
        PROFILE_TAB = (By.ID, "profile")
        EMPLOYMENT_TAB = (By.ID, "employment")
        ASSET_LIABILITIES_TAB = (By.ID, "assetsandliabilities")
        BUDGET_TAB = (By.ID, "budget")
        RETIREMENT_TAB = (By.ID, "retirement")
        ESTATE_PLANNING = (By.ID, "estateplanning")
        SUMMARY_TAB = (By.ID, "declaration")
        PROTECTION_TAB = (By.ID, "protection")
        MORTGAGE_TAB = (By.ID, "mortgage")


class FactFindActionsMenuSection(BasePageSection, BasePage):

    def hover_over_factfind_actions_menu(self):
        return self.hover_over(BaseFactFindPage.Locators.FACTFIND_ACTIONS_MENU)

    def click_view_linked_documents(self):
        return self.click(FactFindActionsMenuSection.Locators.VIEW_LINKED_DOCUMENTS_ACTION)

    def click_view_pdfs(self):
        return self.click(FactFindActionsMenuSection.Locators.VIEW_PDFS_ACTION)

    def click_add_remove_partner(self):
        return self.click(FactFindActionsMenuSection.Locators.ADD_REMOVE_PARTNER)

    class Locators(object):
        VIEW_LINKED_DOCUMENTS_ACTION = (
            By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'View Linked Documents')]")
        VIEW_PDFS_ACTION = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'View PDFs')]")
        ADD_REMOVE_PARTNER = (By.XPATH,
                              "//ul[@class='droplist-items group']//*[contains(text(), 'Add/Remove Partner')]")
