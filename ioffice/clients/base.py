from ioffice.adviserworkplace import AdviserWorkplacePage
from ioffice.base import BasePageSection, BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class BaseClientPage(AdviserWorkplacePage):

    def get_client_bar_info(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(BaseClientPage.Locators.BAR_INFO)).text

    def get_client_id(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(BaseClientPage.Locators.BAR_INFO))
        return re.search(r'(?<=./)\d+', self.driver.current_url, flags=re.IGNORECASE).group(0)

    def client_actions_menu(self):
        return ClientActionsMenuSection(self)

    def hover_over_generate(self):
        self.hover_over(BaseClientPage.Locators.GENERATE_MENU)
        return GenerateMenu(self)

    """a method to get access to Dashboard, Details, etc... menu tabs"""

    def level3_menu(self):
        return IoLevel3NavigationMenuSection(self)

    class Locators(object):
        BAR_INFO = (By.XPATH, "//div[@class='bar-info']/strong")
        ACTIONS_MENU = (By.ID, "primary")
        GENERATE_MENU = (By.ID, "generate")
        DASHBOARD = (By.XPATH, "//*[@class='dashboard-tabs-on']/a[contains(text(), 'Client')]")


class ClientActionsMenuSection(BasePageSection, BaseClientPage):

    def hover_over_client_actions(self):
        return self.hover_over(BaseClientPage.Locators.ACTIONS_MENU)

    def add_plan(self):
        return self.click(ClientActionsMenuSection.Locators.ADD_PLAN)

    def click_upload_document(self):
        return self.click(ClientActionsMenuSection.Locators.UPLOAD_DOCUMENT_LINK)

    def add_relationship(self):
        return self.click(ClientActionsMenuSection.Locators.ADD_RELATIONSHIP)

    def add_scheme(self):
        return self.click(ClientActionsMenuSection.Locators.ADD_SCHEME)

    def client_share(self):
        return self.click(ClientActionsMenuSection.Locators.CLIENT_SHARE)

    def add_fee(self):
        return self.click(ClientActionsMenuSection.Locators.ADD_FEE_ACTION)

    def select_restrict_processing(self):
        return self.click(ClientActionsMenuSection.Locators.RESTRICT_PRCESSING_ACTION)

    def merge_client(self):
        return self.click(ClientActionsMenuSection.Locators.MERGE_CLIENT)

    def export_client_data(self):
        return self.click(ClientActionsMenuSection.Locators.EXPORT_CLIENT_DATA)

    def get_io_store_apps_links(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_all_elements_located(
            ClientActionsMenuSection.Locators.IO_STORE_APPS_LINK))

    def click_get_quote(self):
        return self.click(ClientActionsMenuSection.Locators.GET_NEW_QUOTE_LINK)

    def click_get_illustration(self):
        return self.click(ClientActionsMenuSection.Locators.GET_NEW_ILLUSTRATION_LINK)

    def add_source_mortgage(self):
        return self.click(ClientActionsMenuSection.Locators.SOURCE_MORTGAGE)

    def click_add_opportunity(self):
        self.page.click(ClientActionsMenuSection.Locators.ADD_OPPORTUNITY_LINK)
        return self

    def click_add_task(self):
        self.page.click(ClientActionsMenuSection.Locators.ADD_TASK_LINK)
        return self

    class Locators(object):
        ADD_RELATIONSHIP = (
            By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Add Relationship')]")
        ADD_PLAN = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Add Plan')]")
        UPLOAD_DOCUMENT_LINK = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Upload Document')]")
        CLIENT_SHARE = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Share Client')]")
        ADD_FEE_ACTION = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Add Fee')]")
        RESTRICT_PRCESSING_ACTION = (
            By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Restrict Processing')]")
        MERGE_CLIENT = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Merge Client')]")
        ADD_SCHEME = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Add Scheme')]")
        EXPORT_CLIENT_DATA = (
            By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Export Client Data')]")
        IO_STORE_APPS_LINK = (By.XPATH, "//li[@id='primary']//div[text() ='iO Store Apps']/parent::li//a")
        GET_NEW_QUOTE_LINK = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Get New Quote')]")
        GET_NEW_ILLUSTRATION_LINK = (
        By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Get New Illustration')]")
        SOURCE_MORTGAGE = (By.XPATH, "//a[contains(text(),'Source Mortgage')]")
        ADD_OPPORTUNITY_LINK = (By.XPATH, "//a[text()='Add Opportunity']")
        ADD_TASK_LINK = (By.XPATH, "//a[text()='Add Task']")


class IoLevel3NavigationMenuSection(BasePageSection, BasePage):

    def click_dashboard(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.DASHBOARD_TAB)

    def click_details(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.DETAILS_TAB)

    def click_factfind(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.FACTFIND_TAB)

    def click_schemes(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.SCHEMES_TAB)

    def click_plans(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.PLANS_TAB)

    def click_documents(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.DOCUMENTS_TAB)

    def click_opportunities(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.OPPORUTNITIES_TAB)

    def click_reports(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.REPORTS_TAB)

    def click_activities(self):
        self.page.click(IoLevel3NavigationMenuSection.Locators.ACTIVITIES_TAB)
        return self

    def click_quotes_apps(self):
        self.page.click(IoLevel3NavigationMenuSection.Locators.QUOTES_APPS_TAB)
        return self

    def click_service_case(self):
        self.page.click(IoLevel3NavigationMenuSection.Locators.SERVICE_CASE)
        return self

    def click_advice(self):
        self.page.click(IoLevel3NavigationMenuSection.Locators.ADVICE_TAB)
        return self

    class Locators(object):
        DASHBOARD_TAB = (By.CLASS_NAME, "menu_node_client_dashboard")
        DETAILS_TAB = (By.CLASS_NAME, "menu_node_client_detail")
        FACTFIND_TAB = (By.CLASS_NAME, "menu_node_client_fullfactfind")
        PLANS_TAB = (By.CLASS_NAME, "menu_node_clients_plans")
        SCHEMES_TAB = (By.CLASS_NAME, "menu_node_schemes  ")
        DOCUMENTS_TAB = (By.CLASS_NAME, "menu_node_client_documents ")
        OPPORUTNITIES_TAB = (By.CLASS_NAME, "menu_node_opportunities")
        REPORTS_TAB = (By.CLASS_NAME, "menu_node_client_reports")
        ACTIVITIES_TAB = (By.CLASS_NAME, "menu_node_clients_clientactivity")
        QUOTES_APPS_TAB = (By.CLASS_NAME, "menu_node_quotes")
        SERVICE_CASE = (By.CSS_SELECTOR, ".menu_node_advice  ")
        ADVICE_TAB = (By.CSS_SELECTOR, ".menu_node_clients_planning")


class GenerateMenu(BasePageSection):

    def get_categories_list(self):
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_all_elements_located(GenerateMenu.Locators.CATEGORIES_LIST))

    def click_category(self, category_element):
        return WebDriverWait(self.driver, self.page.TIMEOUT).until(EC.visibility_of(category_element)).click()

    class Locators(object):
        CATEGORIES_LIST = (By.XPATH, "//*[@id='generate']//*[@class='droplist-items group']/li/a")
