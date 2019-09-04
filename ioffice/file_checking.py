from selenium.webdriver.common.by import By
from ioffice.base import IOBasePage, IOFrameDialog
from pageobjects import BasePageSection


class FileCheckingPage(IOBasePage):

    def click_post_search(self):
        self.click(self.Locators.POST_SEARCH)
        return self

    def click_pre_search(self):
        self.click(self.Locators.PRE_SEARCH)
        return self

    def select_search_type(self, data):
        self.select_by_visible_text(self.Locators.SEARCH_TYPE, data)
        return self

    def click_clear_button(self):
        self.click(self.Locators.CLEAR_BUTTON)
        return self

    def click_search_button(self):
        self.click(self.Locators.SEARCH_BUTTON)
        return self

    def get_io_ref(self):
        return self.get_text(self.Locators.IO_REF)

    def using_select_client_dialog(self):
        self.click(self.Locators.CLIENT_TEXT_BOX)
        return FileCheckingPage._SelectClientDialog(self)

    class Locators(object):
        POST_SEARCH = (By.CSS_SELECTOR, '.menu_node_filecheck_post_sale_search')
        PRE_SEARCH = (By.CSS_SELECTOR, '.menu_node_filecheck_pre_sale_search')
        SEARCH_TYPE = (By.XPATH, "//select[@name='searchList']")
        CLIENT_TEXT_BOX = (By.CSS_SELECTOR, ".formgroupbody .width33:nth-of-type(2) .handle2container:nth-of-type(2) .hpick")
        CLEAR_BUTTON = (By.XPATH, "//a[contains(text(),'Clear')]")
        SEARCH_BUTTON = (By.XPATH, "//*[@id='form_id_root_2_2_3_2_4']/div[2]/div/a")
        IO_REF = (By.XPATH, "//span[contains(text(),'IOB')]")

    class _SelectClientDialog(BasePageSection, IOFrameDialog):

            def __init__(self, parent_page):
                super().__init__(parent_page)
                self.FRAME = (By.XPATH, self.Locators._FRAME)
                self.frame_locator = self.FRAME
                self._switch_to_frame()

            def click_clear_button(self):
                self.page.click(self.Locators.CLEAR_BUTTON)
                return self

            def fill_in_first_name(self, data):
                self.page.fill_in_field(self.Locators.FIRST_NAME, data)
                return self

            def fill_in_last_name(self, data):
                self.page.fill_in_field(self.Locators.LAST_NAME, data)
                return self

            def click_search(self):
                self.page.click(self.Locators.SEARCH_BUTTON)
                return self

            def click_first_result(self):
                self.page.click(self.Locators.FIRST_RESULT)
                return FileCheckingPage(self.config)

            class Locators(object):
                _FRAME = "//iframe[@src='/nio/clientsearch/searchdialog?popup_control=id_FileCheck_ClientId']"
                SEARCH_BUTTON = (By.XPATH, "//a[text()='Search']")
                FIRST_RESULT = (By.XPATH, "//*[@id='grid_id_root_2_2_2_3']/tbody/tr/td/a")
                CLEAR_BUTTON = (By.XPATH, "//a[text()='Clear']")
                FIRST_NAME = (By.CSS_SELECTOR, "#id_Client_FirstName")
                LAST_NAME = (By.CSS_SELECTOR, "#id_Client_LastName")