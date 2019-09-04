from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CashReceiptMatchingDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = CashReceiptMatchingDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def fill_in_io_ref(self, io_ref):
        self.page.clear_and_fill_in_field(CashReceiptMatchingDialog.Locators.IO_REF_TEXT_BOX, io_ref)
        return self

    def fill_high_amount(self, data):
        self.page.clear_and_fill_in_field(CashReceiptMatchingDialog.Locators.HIGH_AMOUNT, data)
        return self

    def select_provider_statement_match_search_type(self, data):
        self.page.select_by_visible_text(CashReceiptMatchingDialog.Locators.SELECT_SEARCH_TYPE, data)
        return self

    def click_search(self):
        self.search_element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(CashReceiptMatchingDialog.Locators.SEARCH_BUTTON))
        self.page.click(CashReceiptMatchingDialog.Locators.SEARCH_BUTTON)
        return self

    def select_first_search_result_record(self):
        self.page.click(CashReceiptMatchingDialog.Locators.SEARCH_RESULT_RADIO_BUTTON)
        return self

    def click_match(self):
        self.page.click(CashReceiptMatchingDialog.Locators.MATCH_BUTTON)
        return self

    def click_unmatch(self):
        self.page.click(CashReceiptMatchingDialog.Locators.UNMATCH_BUTTON)
        return self

    def wait_search_results_appear(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.staleness_of(self.search_element))
        return self

    def click_clear(self):
        self.page.click(CashReceiptMatchingDialog.Locators.CLEAR_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='CashReceipt']")
        HIGH_AMOUNT = (By.CSS_SELECTOR, "#id_HiAmount")
        SELECT_SEARCH_TYPE = (By.CSS_SELECTOR, " #id_root_2_2_3_2_3 > div > div.ux-ctl-search-options > select")
        IO_REF_TEXT_BOX = (By.CSS_SELECTOR, "#id_CashReceiptMatch_IORef")
        SEARCH_BUTTON = (By.XPATH, "//a[text() ='Search' and contains(@onclick, 'CashReceipt')]")
        SEARCH_RESULT_RADIO_BUTTON = (By.CSS_SELECTOR, "#grid_id_root_2_2_3_3 [type='radio']")
        MATCH_BUTTON = (By.XPATH, "//div[@id='id_root_2_2_3_3']//a[text() ='Match']")
        UNMATCH_BUTTON = (By.XPATH, "//div[@id='id_root_2_2_4']//a[text() ='Unmatch']")
        CLEAR_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_3_2_3  a[onclick*='doClear']")
