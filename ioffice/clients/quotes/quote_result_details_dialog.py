from ioffice.base import BasePageSection, IOFrameDialog, WebDriverWait, EC
from selenium.webdriver.common.by import By


class QuoteResultDetailsDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = self.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_close_button(self):
        return self.page.click(QuoteResultDetailsDialog.Locators.CLOSE_BUTTON)

    def get_first_column_title(self):
        return self.page.get_text(self.Locators.TABLE_FIRST_TITLE_TEXT)

    def get_second_column_title(self):
        return self.page.get_text(self.Locators.TABLE_SECOND_TITLE_TEXT)

    def get_third_column_title(self):
        return self.page.get_text(self.Locators.TABLE_THIRD_TITLE_TEXT)

    def get_first_row_values(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_all_elements_located(QuoteResultDetailsDialog.Locators.TABLE_FIRST_ROW))

    def get_second_row_values(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_all_elements_located(QuoteResultDetailsDialog.Locators.TABLE_SECOND_ROW))

    def get_third_row_values(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_all_elements_located(QuoteResultDetailsDialog.Locators.TABLE_THIRD_ROW))

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe")
        TABLE_FIRST_TITLE_TEXT = (By.XPATH, "//*[contains(@id, 'DetailsGrid')]/thead/tr/th[1]/span")
        TABLE_SECOND_TITLE_TEXT = (By.XPATH, "//*[contains(@id, 'DetailsGrid')]/thead/tr/th[2]/span")
        TABLE_THIRD_TITLE_TEXT = (By.XPATH, "//*[contains(@id, 'DetailsGrid')]/thead/tr/th[3]/span")
        CLOSE_BUTTON = (By.XPATH, "//*[@id='form_id_root_2_2_2']/div[2]/div/a")
        TABLE_FIRST_ROW = (By.XPATH, "//*[contains(@id, 'DetailsGrid')]/tbody/tr[1]")
        TABLE_SECOND_ROW = (By.XPATH, "//*[contains(@id, 'DetailsGrid')]/tbody/tr[2]")
        TABLE_THIRD_ROW = (By.XPATH, "//*[contains(@id, 'DetailsGrid')]/tbody/tr[3]")
