from ioffice.add_client_wizard import *
from ioffice.provider_search_dialog import *
from ioffice.producttype_search_dialog import *
from ioffice.adviser_search_dialog import *


class AddClientAndPlanWizard(AddClientWizard):

    def __init__(self, config):
        super().__init__(config, "Add Client And Plan")
        self.frame_locator = AddClientAndPlanWizard.Locators.FRAME

    def plan_stage(self):
        return AddClientAndPlanWizard.PlanStage(self)

    class Locators(object):
        FRAME = (By.XPATH, "//iframe[@src='/nio/clientactions/addclientandplan']")
   
    class PlanStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Plan")
            self.is_preexting_plan = False
        
        def tick_is_preexisting_plan_checkbox(self):
            self.page.click(AddClientAndPlanWizard.PlanStage.Locators.IS_PRE_EXISTING_PLAN_CHECKBOX)
            self.is_preexting_plan = True
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(IOFrameDialog.Locators.BLOCK_UI))
            WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(IOFrameDialog.Locators.BLOCK_UI))

        def open_adviser_search_dialog(self):
            self.page.click(AddClientAndPlanWizard.PlanStage.Locators.SELECT_ADVISER_BUTTON)
            return AdviserSearchDialog(self.page, self.page.frame_locator, "id_PlanDetailsStep_SellingAdviserId")

        def select_advicetype(self, advice_type_text=None):
            el = self.driver.find_element(*AddClientAndPlanWizard.PlanStage.Locators.ADVICETYPE_SELECT_BOX)
            for option in el.find_elements_by_tag_name('option'):
                if not text and not option.text == "Select...":
                    option.click()
                    break
                elif option.text == advice_type_text:
                    option.click()
                    break

        def open_provider_search_dialog(self):
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(IOFrameDialog.Locators.BLOCK_UI))
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AddClientAndPlanWizard.PlanStage.Locators.SELECT_PROVIDER_BUTTON))).click()
            if self.is_preexting_plan:
                return FullProviderSearchDialog(self.page, self.page.frame_locator)
            else:
                return ProviderSearchDialog(
                    self.page, self.page.frame_locator)
        
        def open_producttype_search_dialog(self):
            WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(IOFrameDialog.Locators.BLOCK_UI))
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AddClientAndPlanWizard.PlanStage.Locators.SELECT_PRODUCT_TYPE_BUTTON)).click()
            if self.is_preexting_plan:
                return ProductTypeSearchDialog(
                    self.page, self.page.frame_locator)
            else:
                return GatedProductTypeSearchDialog(
                    self.page, self.page.frame_locator)

        class Locators(BaseWizardPage.Locators):
            IS_PRE_EXISTING_PLAN_CHECKBOX = (By.ID, "id_PlanDetailsStep_IsPreExistingPlan")
            SELECT_PROVIDER_BUTTON = (By.XPATH, "//*[@id='__display_id_PlanDetailsStep_ProductProviderId']//following-sibling::*/a[@class='hpick']")
            SELECT_PRODUCT_TYPE_BUTTON = (By.XPATH, "//*[@id='__display_ProdType']//following-sibling::*/a[@class='hpick']")
            ADVICETYPE_SELECT_BOX = (By.ID, "id_PlanDetailsStep_AdviceTypeId")
            SELECT_ADVISER_BUTTON = (By.XPATH, "//*[@id='__display_id_PlanDetailsStep_SellingAdviserId']//following-sibling::*/a[@class='hpick']")





