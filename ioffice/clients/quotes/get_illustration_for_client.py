from selenium.webdriver.common.by import By
from ioffice.clients.quotes.base import BaseQuotesPage


class GetIllustrationForClientPage(BaseQuotesPage):

    def click_product_area(self, product):
        element = (By.XPATH, self.Locators.PRODUCT_AREA_RADIO_BUTTON.format(product))
        return self.click(element)

    def get_app(self, app_name):
        element = (By.XPATH, self.Locators.ILLUSTRATION_APP_BUTTON.format(app_name))
        return self.get_text(element)

    class Locators(object):
        PRODUCT_AREA_RADIO_BUTTON = "//*[contains(text(), '{0}')]/input"
        ILLUSTRATION_APP_BUTTON = "//*[contains(text(), '{0}')]"
