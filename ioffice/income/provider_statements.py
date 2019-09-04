from ioffice.income.base import IncomeBasePage, By


class ProviderStatementsBasePage(IncomeBasePage):

    def click_statement_search_tab(self):
        self.click(self.Locators.STATEMENT_SEARCH_TAB)
        return self

    def click_electronic_imports_tab(self):
        self.click(self.Locators.ELECTRONIC_STATEMENTS)
        return self

    class Locators(object):
        STATEMENT_SEARCH_TAB = (By.CSS_SELECTOR, ".menu_node_commissions_providerstatements_search")
        ELECTRONIC_STATEMENTS = (By.CSS_SELECTOR, ".menu_node_commissions_providerstatements_electronicimports")
