from ioffice.base import IOBasePage
from pageobjects import BasePageSection
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ElectronicImportsPage(IOBasePage, BasePageSection):

    def click_edit_button(self):
        self.click(self.Locators.EDIT_BUTTON)
        return self

    def click_update_button(self):
        self.click(self.Locators.UPDATE_BUTTON)
        return self

    def click_first_radio_button(self):
        self.click(self.Locators.FIRST_STATEMENT_LIVE_RADIO_BUTTON)
        return self

    def click_make_live_button(self):
        self.click(self.Locators.MAKE_LIVE_BUTTON)
        return self

    def click_import_completed_io_template(self):
        return self.click(self.Locators.IMPORT_COMPLETED_IO_TEMPLATE)

    def click_download_blank_io_template(self):
        return self.click(self.Locators.DOWNLOAD_BLANK_IO_TEMPLATE)

    def close_import_provider_statement_dialog(self):
        self.click(self.Locators.CANCEL)
        return self

    def click_first_import_statement_radio_button(self):
        return self.click(self.Locators.FIRST_IMPORT_STATEMENT_RADIO_BUTTON)

    def click_first_import_statement_delete_button(self):
        return self.click(self.Locators.IMPORT_STATEMENT_DELETE_BUTTON)

    def is_abacus_mortgages_statement_present(self):
        return not (WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.invisibility_of_element_located(self.Locators.STATEMENT_WITH_ABACUS_MORTGAGE)))

    def get_live_statement_date_value(self):
        return self.get_text(self.Locators.LIVE_STATEMENT_DATE_VALUE)

    def get_import_amount_value(self):
        return self.get_text(self.Locators.IMPORT_AMOUNT)

    def get_import_date_value(self):
        return self.get_text(self.Locators.IMPORT_DATE)

    class Locators(object):
        IMPORT_COMPLETED_IO_TEMPLATE = (
            By.XPATH, "//body[@class='body']//ul[@class='nav-quicklinks']/li[2]/a[@href='#']")
        DOWNLOAD_BLANK_IO_TEMPLATE = (By.CSS_SELECTOR, "[rel='noopener noreferrer']")
        IMPORT_AMOUNT = (
            By.XPATH, "//table[@id='grid_ImportedProviderStatementsGrid']/tbody/tr/td[4]/span[@class='alignRight']")
        IMPORT_DATE = (By.XPATH, "//table[@id='grid_ImportedProviderStatementsGrid']/tbody/tr/td[3]")
        CANCEL = (By.CSS_SELECTOR, "#id_root_2_2_2_4")
        FIRST_IMPORT_STATEMENT_RADIO_BUTTON = (
        By.XPATH, "//table[@id='grid_ImportedProviderStatementsGrid']/tbody/tr//input[@type='radio']")
        IMPORT_STATEMENT_DELETE_BUTTON = (By.CSS_SELECTOR, "#ImportedProviderStatementsGrid_10")
        EDIT_BUTTON = (By.XPATH, "//table[@id='grid_ImportedProviderStatementsGrid']/tbody/tr//a[@href='#']")
        UPDATE_BUTTON = (By.XPATH, "//a[contains(text(),'Update')]")
        PROVIDER_DIALOG_LINK = (By.CSS_SELECTOR, ".hpick")
        TABLE_VALUE = (By.CSS_SELECTOR, ".first.last")
        FIRST_STATEMENT_LIVE_RADIO_BUTTON = (By.XPATH, "//table[@id='grid_ImportedProviderStatementsGrid']/tbody/tr//input[@name='__s']")
        MAKE_LIVE_BUTTON = (By.CSS_SELECTOR, "#ImportedProviderStatementsGrid_9")
        LIVE_STATEMENT_DATE_VALUE = (By.XPATH, "//table[@id='grid_ProviderStatementGrid']/tbody/tr[1]/td[6]")
        STATEMENT_WITH_ABACUS_MORTGAGE = (By.XPATH, "//*[@id='grid_ImportedProviderStatementsGrid']/tbody//span[text() = 'Abacus Mortgages']")