from selenium.webdriver.common.by import By
from ioffice.base import IOBasePage, BasePageSection


class IncomeBasePage(IOBasePage):
    def level2_menu(self):
        return IncomeLevel2NavigationMenuSection(self)


class IncomeLevel2NavigationMenuSection(BasePageSection):
    def click_cash_receipts(self):
        self.page.click(IncomeLevel2NavigationMenuSection.Locators.CASH_RECEIPTS_MENU_TAB)
        return self

    def click_provider_statements(self):
        self.page.click(IncomeLevel2NavigationMenuSection.Locators.PROVIDER_STATEMENTS_TAB)
        return self

    def click_administration(self):
        self.page.click(IncomeLevel2NavigationMenuSection.Locators.ADMINISTRATION_TAB)
        return self

    class Locators(object):
        CASH_RECEIPTS_MENU_TAB = (By.CSS_SELECTOR, "[href='/nio/cashreceipt/index']")
        PROVIDER_STATEMENTS_TAB = (By.CSS_SELECTOR, ".menu_node_commissions_providerstatements")
        ADMINISTRATION_TAB = (By.CSS_SELECTOR, ".menu_node_commissions_administration")