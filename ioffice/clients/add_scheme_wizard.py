from ioffice.add_scheme_adviser_search_dialog import AddSchemeAdviserSearchDialog
from ioffice.provider_search_dialog import FullProviderSearchDialog
from ioffice.wizard import *
from ioffice.adviser_search_dialog import *


class AddSchemeWizard(BaseWizardPage):

    def __init__(self, config):
        super().__init__(config, "Add Scheme")
        self.frame_locator = AddSchemeWizard.Locators.FRAME

    def basic_details_stage(self):
        return AddSchemeWizard.BasicDetailsStage(self)

    def category_details_stage(self):
        return AddSchemeWizard.CategoryDetailsStage(self)

    def click_finish(self):
        self.click(self.Locators.FINISH_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='groupscheme']")
        FINISH_BUTTON = (By.XPATH, "//*[@class='wizard-buttons']//a[@innertext='Finish']")

    class BasicDetailsStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Basic Details")

        def open_adviser_dialog(self):
            self.page.click(AddSchemeWizard.BasicDetailsStage.Locators.SELECT_ADVISER_BUTTON)
            return AddSchemeAdviserSearchDialog(self.page, self.page.frame_locator)

        def open_provider_search_dialog(self):
            self.page.click(AddSchemeWizard.BasicDetailsStage.Locators.SELECT_PROVIDER_BUTTON)
            return FullProviderSearchDialog(self.page, self.page.frame_locator)

        def select_scheme_type(self, data):
            self.page.select_by_visible_text(self.Locators.SCHEME_TYPE, data)
            return self

        def select_plan_type(self, data):
            self.page.select_by_visible_text(self.Locators.PLAN_TYPE, data)
            return self

        def fill_in_scheme_name(self, data):
            self.page.fill_in_field(self.Locators.SCHEME_NAME, data)
            return self

        class Locators(object):
            SELECT_ADVISER_BUTTON = (By.XPATH, "//div[@id='AdviserContainer']/div//div[@class='handle handle2']/a[1]")
            SELECT_PROVIDER_BUTTON = (By.XPATH, "//div[@id='ProviderContainer']/div//div[@class='handle handle2']/a[1]")
            SCHEME_TYPE = (By.ID, "SchemeCategory")
            PLAN_TYPE = (By.ID, "id_BasicDetails_RefPlanTypeProductSubTypeId")
            SCHEME_NAME = (By.ID, "SchemeName")

    class CategoryDetailsStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Category Details")

        def fill_in_category_name(self, data):
            self.page.fill_in_field(self.Locators.CATEGORY_NAME, data)
            return self

        class Locators(object):
            CATEGORY_NAME = (By.ID, "id_GPPCategoryContainer_CategoryName")



