from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ioffice.base import IOFrameDialog
from ioffice.clients.quotes.base import BaseQuotesPage
import time

from pageobjects import BasePageSection


class GetQuoteForClientPage(BaseQuotesPage):

    def click_product_area(self, product):
        element = (By.XPATH, self.Locators.PRODUCT_AREA_RADIO_BUTTON.format(product))
        return self.click(element)

    def get_app(self, app_name):
        element = (By.XPATH, self.Locators.QUOTE_APP_BUTTON.format(app_name))
        return self.get_text(element)

    def click_quote_app(self, app_name):
        time.sleep(1)
        element = (By.XPATH, self.Locators.QUOTE_APP_BUTTON.format(app_name))
        return self.click(element)

    def click_next(self):
        time.sleep(1)
        return self.click(self.Locators.NEXT_BUTTON)

    def select_product_type(self, data):
        return self.fill_in_field(self.Locators.PRODUCT_TYPE_SELECT_BOX, data)

    def fill_in_age_field(self, data):
        return self.fill_in_field(self.Locators.AGE_FIELD, data)

    def fill_in_min_life_amount_field(self, data):
        return self.fill_in_field(self.Locators.MIN_LIFE_FIELD, data)

    def fill_in_max_life_amount_field(self, data):
        return self.fill_in_field(self.Locators.MAX_LIFE_FIELD, data)

    def check_all_checkboxes(self):
        return self.click(self.Locators.ALL_CHECKBOX)

    def click_complete(self):
        time.sleep(1)
        return self.click(self.Locators.COMPLETE_BUTTON)

    class Locators(object):
        PRODUCT_AREA_RADIO_BUTTON = "//*[contains(text(), '{0}')]/input"
        QUOTE_APP_BUTTON = "//*[contains(text(), '{0}')]"
        NEXT_BUTTON = (By.XPATH, "//*[@id='id_root_2_2_3']/div[2]/a[contains(text(), 'Next')]")
        PRODUCT_TYPE_SELECT_BOX = (By.XPATH, "//*[@id='ProductType']")
        AGE_FIELD = (By.XPATH, "//*[@id='TermAge']")
        MIN_LIFE_FIELD = (By.XPATH, "//*[@id='LifeCoverAmount']")
        MAX_LIFE_FIELD = (By.XPATH, "//*[@id='LifeCoverAmountLimit']")
        ALL_CHECKBOX = (By.XPATH, "//*[@id='grid_ProviderGrid']/thead/tr/th[1]/input")
        COMPLETE_BUTTON = (By.XPATH, "//*[@id='id_root_2_2_3']/div[2]/a[contains(text(), 'Complete')]")


class GetNewQuoteDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = GetNewQuoteDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def click_product_area(self, product_area):
        element = (By.XPATH, GetNewQuoteDialog.Locators.PRODUCT_AREA_RADIO_BUTTON.format(product_area))
        self.page.click(element)
        return self

    def get_portals(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_all_elements_located(GetNewQuoteDialog.Locators.PORTAL_APPS))

    def click_cancel(self):
        self.page.click(GetNewQuoteDialog.Locators.CANCEL_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='GetQuoteForClient?opportunityId']")
        PRODUCT_AREA_RADIO_BUTTON = "//*[contains(text(), '{0}')]/input"
        PORTAL_APPS = (By.CSS_SELECTOR, "#WealthLinkQuoteLaunch .formgroupbody div a")
        CANCEL_BUTTON = (By.CSS_SELECTOR, "form a[onclick*='dialogClose']")
