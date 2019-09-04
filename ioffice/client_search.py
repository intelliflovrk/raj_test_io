from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ioffice.base import IOBasePage, IOFrameDialog
from pageobjects import BasePage


class ClientSearch(IOBasePage):

    def clear_firstname(self):
        return self.clear(ClientSearch.Locators.FIRSTNAME_FIELD)

    def clear_lastname(self):
        return self.clear(ClientSearch.Locators.LASTNAME_FIELD)

    def fill_in_firstname(self, name):
        return self.fill_in_field(ClientSearch.Locators.FIRSTNAME_FIELD, name)

    def fill_in_lastname(self, name):
        return self.fill_in_field(ClientSearch.Locators.LASTNAME_FIELD, name)

    def click_search_button(self):
        return self.click(ClientSearch.Locators.SEARCH_BUTTON)

    def click_full_search_button(self):
        return self.click(ClientSearch.Locators.FULL_SEARCH_BUTTON)

    def click_fee_search_button(self):
        return self.click(ClientSearch.Locators.FEE_SEARCH_BUTTON)

    def get_search_results_table_rows(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_all_elements_located(locator))

    def get_result_table(self):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(ClientSearch.Locators.TABLE))

    def select_search_option(self, search_option):
        return self.select_by_visible_text(ClientSearch.Locators.SEARCH_OPTIONS_SELECT_BOX, search_option)

    def select_reference_type(self, type):
        return self.select_by_visible_text(ClientSearch.Locators.REFERENCE_TYPE_SELECT_BOX, type)

    def fill_in_reference(self, reference):
        self.fill_in_field(ClientSearch.Locators.REFERENCE_FIELD, reference)
        return self

    def clear_reference(self):
        return self.clear(ClientSearch.Locators.REFERENCE_FIELD)

    def click_open_first_link(self):
        return self.click(ClientSearch.Locators.OPEN_FIRST_LINK)

    def click_open_first_fee_link(self):
        return self.click(ClientSearch.Locators.FIRST_FEE_LINK)

    def click_clear_button(self):
        return self.click(ClientSearch.Locators.CLEAR_BUTTON)

    def click_open_first_client(self):
        return self.click(ClientSearch.Locators.OPEN_FIRST_CLIENT_LINK)

    class Locators(object):
        FIRSTNAME_FIELD = (By.ID, "id_fname")
        LASTNAME_FIELD = (By.ID, "id_lname")
        SEARCH_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_2_3_2 .ux-ctl-form-action-buttons a")
        FULL_SEARCH_BUTTON = (By.CSS_SELECTOR, "#form_id_root_2_2_2_3_3 .ux-ctl-form-action-buttons a")
        FEE_SEARCH_BUTTON = (By.CSS_SELECTOR, ".ux-ctl-form-action-buttons")
        CLIENT_ROW = "ClientSearchFullGrid__{0}"
        SEARCH_OPTIONS_SELECT_BOX = (By.CSS_SELECTOR, ".ux-ctl-search-options [name='searchList']")
        REFERENCE_TYPE_SELECT_BOX = (By.ID, "id_Plan_SequentialRefType")
        REFERENCE_FIELD = (By.ID, "id_Plan_SequentialRef")
        OPEN_FIRST_LINK = (By.XPATH, "//table[@id='grid_ClientSearchFullGrid']/tbody/tr//a[contains(@title, 'Open')]")
        OPEN_FIRST_CLIENT_LINK = (By.CSS_SELECTOR, "#grid_ClientSearchNameGrid a[title='Open']")
        FIRST_FEE_LINK = (By.XPATH, "//table[@id='grid_ClientFeeSearchGrid']/tbody/tr/td//a[contains(@title, 'Open')]")
        CLEAR_BUTTON = (By.XPATH, "//*[text()[contains(.,'Clear')]]")
        TABLE = (By.CSS_SELECTOR, "#grid_ClientSearchFullGrid > tbody")

    class ClientQuickSearchResult(BasePage, IOFrameDialog):
        def __init__(self, config, current_frame=None):
            self.driver = config.driver
            self.FRAME = (By.XPATH, ClientSearch.ClientQuickSearchResult.Locators.FRAME)
            self.frame_locator = self.FRAME
            self.prev_frame_locator = current_frame
            self._switch_to_frame()

        def get_client_search_result(self):
            return WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(ClientSearch.ClientQuickSearchResult.Locators.RESULT_TABLE)).text

        def close_client_search_dialog(self):
            return self.click(ClientSearch.ClientQuickSearchResult.Locators.CLOSE_BUTTON)

        class Locators(object):
            _FRAME = (By.XPATH, "//iframe[@src='/nio/clientsearch/clientquicksearch?__export=qs&qstext=']")
            FRAME = "//iframe[@src='/nio/clientsearch/clientquicksearch?__export=qs&qstext=']"
            RESULT_TABLE = (By.CSS_SELECTOR, "#grid_id_root_2_2_3 > tbody > tr > td > span")
            CLOSE_BUTTON = (By.CSS_SELECTOR, "div.dleClose > a")
