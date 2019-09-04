from selenium.webdriver.common.by import By
from ioffice.file_checking import FileCheckingPage


class PreSearchPage(FileCheckingPage):

    def click_search(self):
        return self.click(PreSearchPage.Locators.SEARCH_BUTTON)

    def get_first_search_result(self):
        return self.get_text(PreSearchPage.Locators.SEARCH_RESULTS_TABLE_ROWS)

    class Locators(object):
        SEARCH_BUTTON = (By.CSS_SELECTOR, "a[onclick*='viewpresalesearch']")
        SEARCH_RESULTS_TABLE_ROWS = (By.CSS_SELECTOR, 'table tbody tr:not(.filter)[id]')
