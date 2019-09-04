from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ioffice.clients.factfind.protection_tab import ProtectionTab
from pageobjects import EC


class ExistingProvisionTab(ProtectionTab):

    def click_save_existing_protection_plan(self):
        return self.click(ExistingProvisionTab.Locators.SAVE_BUTTON)

    def get_protection_data_table(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ExistingProvisionTab.Locators.TABLE_ROW))

    def get_existing_protection_plans_str_list(self):
        textlist = []
        data = ExistingProvisionTab(self.config).get_data_table_rows()
        for item in data:
            textlist.append(item.text)
        return textlist

    def get_data_table_rows(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ExistingProvisionTab.Locators.TABLE_ROW))
        return self.driver.find_elements_by_css_selector("#sidebar-container table tbody tr:not(.filter)")

    def click_add_protection_plan(self):
        return self.click(ExistingProvisionTab.Locators.ADD_CONTRACT_BUTTON)

    def click_have_existing_policies_yes_radio_button(self):
        return self.click(ExistingProvisionTab.Locators.HAVE_PROVISION_CHECKBOX)

    class Locators(object):
        PRODUCT_NAME = (By.ID, "ProtProductName_ProductName_0")
        TYPE_OF_CONTRACT = (By.ID, "PlanType_RefPlanType2ProdSubTypeId_0")
        SAVE_BUTTON = (By.ID, "ff-form-save")
        DATA_TABLE = (By.ID, "ProtectionPlansTable_0")
        TABLE_ROW = (By.CSS_SELECTOR, "#sidebar-container table tbody tr:not(.filter)")
        CONFIRM_DELETE_BUTTON = (By.ID, "btnid_0")
        LIFE_COVER_SUM = (By.ID, "LifeCoverAmount_LifeCoverAmount_0")
        CRITICAL_ILLNESS_SUM = (By.ID, "CriticalIllnessAmount_CriticalIllnessAmount_0")
        HAVE_PROVISION_CHECKBOX = (By.ID, "Yes_589_HasExistingProvision_0")
        ADD_CONTRACT_BUTTON = (By.XPATH, "//*[@id=\"protectionplans_grid_0\"]/a")
