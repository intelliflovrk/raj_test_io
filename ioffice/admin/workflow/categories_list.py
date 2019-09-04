from ioffice.admin.workflow.base import WorkflowBasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TemplateCategoriesPage(WorkflowBasePage):

    def fill_in_category_name(self, category_name):
        return self.fill_in_field(TemplateCategoriesPage.Locators.CATEGORY_NAME_FIELD, category_name)

    def click_create(self):
        return self.click(TemplateCategoriesPage.Locators.CREATE_BUTTON)

    def clear_category_name_filter(self):
        return self.clear(TemplateCategoriesPage.Locators.CATEGORY_NAME_FILTER_FIELD)

    def fill_in_category_name_filter(self, category_name):
        return self.fill_in_field(TemplateCategoriesPage.Locators.CATEGORY_NAME_FILTER_FIELD, category_name)

    def click_filter(self):
        return self.click(TemplateCategoriesPage.Locators.FILTER_BUTTON)

    def get_category_id(self):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.Locators.FIRST_CATEGORY_RADIO_BUTTON)).get_attribute("value")

    class Locators(object):
        CREATE_BUTTON = (By.LINK_TEXT, "Create")
        CATEGORY_NAME_FIELD = (By.ID, "id_Name")
        CATEGORY_NAME_FILTER_FIELD = (By.ID, "id___filterName")
        FILTER_BUTTON = (By.CSS_SELECTOR, "[class='jq-filter button button-enabled']")
        DELETE_BUTTON = (By.ID, "id_root_2_2_3_3_2_2_6")
        FIRST_CATEGORY_RADIO_BUTTON = (By.CSS_SELECTOR, "[class='rowselect first'] [type='radio']")