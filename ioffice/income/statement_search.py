from ioffice.income.allocatelineitemdialog import AllocateLineItemDialog
from ioffice.income.base import IncomeBasePage, By
from ioffice.income.income_provider_search_dialog import IncomeProviderSearchDialog


class StatementSearchPage(IncomeBasePage):

    def fill_in_amount(self, data):
        return self.clear_and_fill_in_field(self.Locators.AMOUNT_FIELD, data)

    def open_provider_search_dialog(self):
        self.click(self.Locators.SELECT_PROVIDER_BUTTON)
        return IncomeProviderSearchDialog(self)

    def click_create(self):
        self.click(self.Locators.CREATE_BUTTON)
        return self

    def click_search(self):
        self.click(self.Locators.SEARCH_BUTTON)
        return self

    def select_statement_search_type(self, data):
        self.select_by_visible_text(self.Locators.SEARCH_TYPE, data)
        return self

    def click_clear(self):
        self.click(self.Locators.CLEAR_BUTTON)
        return self

    def fill_in_high_state_amount(self, data):
        self.clear_and_fill_in_field(self.Locators.HIGH_STATE_AMOUNT_FIELD, data)
        return self

    def select_matched(self, data):
        self.select_by_visible_text(self.Locators.MATCHED_SELECT_BOX, data)
        return self

    def select_result_per_page(self, data):
        self.select_by_visible_text(self.Locators.RESULT_PER_PAGE_SELECT_BOX, data)
        return self

    def fill_in_low_state_amount(self, data):
        self.clear_and_fill_in_field(self.Locators.LOW_STATE_AMOUNT_FIELD, data)
        return self

    def select_fee_type(self, data):
        self.select_by_visible_text(self.Locators.FEE_TYPE_SELECT_BOX, data)
        return self

    def fill_in_client_name(self, data):
        self.clear_and_fill_in_field(self.Locators.CLIENT_NAME_FIELD, data)
        return self

    def fill_in_fee_amount(self, data):
        self.clear_and_fill_in_field(self.Locators.FEE_AMOUNT_FIELD, data)
        return self

    def click_allocate(self):
        self.click(self.Locators.ALLOCATE_BUTTON)
        return AllocateLineItemDialog(self)

    def click_save(self):
        self.click(self.Locators.SAVE_BUTTON)
        return self

    def click_close(self):
        self.click(self.Locators.CLOSE_BUTTON)
        return self

    def select_first_statement(self):
        self.click(self.Locators.FIRST_RADIO_BUTTON)
        return self

    def click_delete(self):
        self.click(self.Locators.DELETE_BUTTON)
        return self

    def click_open(self):
        self.click(self.Locators.OPEN_LINK)
        return self

    def get_statement_count_on_first_page(self):
        statement_list = self.driver.find_elements_by_xpath(self.Locators.STATEMENTS)
        return len(statement_list)

    class Locators(object):
        AMOUNT_FIELD = (By.CSS_SELECTOR, "#id_ProviderStatement_Amount")
        SELECT_PROVIDER_BUTTON = (By.XPATH, "//span[@class='control handle2container']//a[@class='hpick']")
        CREATE_BUTTON = (By.CSS_SELECTOR, r"[onclick='return ioUiGridButtonSubmit\(this\)\;']")
        HIGH_STATE_AMOUNT_FIELD = (By.CSS_SELECTOR, "#id_HiStatementAmount")
        LOW_STATE_AMOUNT_FIELD = (By.CSS_SELECTOR, "#id_LoStatementAmount")
        CLEAR_BUTTON = (By.XPATH, "//a[text()='Clear']")
        SEARCH_BUTTON = (By.XPATH, "//a[text()='Search']")
        OPEN_LINK = (By.XPATH, "//table[@id='grid_ProviderStatementGrid']/tbody/tr[1]/td[14]/a")
        STATEMENTS = ("//tr[starts-with(@id, 'ProviderStatementGrid__') and not (contains(@class,'create'))]")
        FEE_TYPE_SELECT_BOX = (By.CSS_SELECTOR, "#id_LineItemView_RefComTypeId")
        CLIENT_NAME_FIELD = (By.CSS_SELECTOR, "#id_LineItemView_ClientName")
        FEE_AMOUNT_FIELD = (By.CSS_SELECTOR, "#id_LineItemView_Amount")
        SAVE_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_4_2")
        ALLOCATE_BUTTON = (By.XPATH, "//a[@class='button button-enabled'][contains(text(),'Allocate')]")
        CLOSE_BUTTON = (By.XPATH, "//a[text()='Close']")
        FIRST_RADIO_BUTTON = (By.XPATH, "//table[@id='grid_ProviderStatementGrid']/tbody/tr[1]//input")
        DELETE_BUTTON = (By.CSS_SELECTOR, "#ProviderStatementGrid_16")
        SEARCH_TYPE = (By.XPATH, "//select[@name='searchList']")
        MATCHED_SELECT_BOX = (By.ID, "id_ProviderStatement_IsMatched")
        RESULT_PER_PAGE_SELECT_BOX = (By.XPATH, "//*[@id='grid_ProviderStatementGrid']/tfoot/tr/th/div[2]/span[1]/select")
