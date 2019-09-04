from ioffice.wizard import *
from ioffice.adviser_search_dialog import *
from ioffice.producttype_search_dialog import *


class AddSubPlanWizard(BaseWizardPage):
    def __init__(self, config, title="Add Sub Plan"):
        super().__init__(config, title)
        self.frame_locator = AddSubPlanWizard.Locators.FRAME

    def plan_stage(self):
        return AddSubPlanWizard.PlanStage(self)

    class Locators(object):
        FRAME = (By.XPATH, "// iframe[contains(@src,'/nio/planactions')]")

    class PlanStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Plan")
            self.is_preexting_plan = False

        def open_adviser_search_dialog(self):
            self.page.click(AddSubPlanWizard.PlanStage.Locators.SELECT_ADVISER_BUTTON)
            return AdviserSearchDialog(self.page, self.page.frame_locator, "id_PlanDetailsStep_SellingAdviserId")

        def open_producttype_search_dialog(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    AddSubPlanWizard.PlanStage.Locators.SELECT_PRODUCT_TYPE_BUTTON)).click()
            if self.is_preexting_plan:
                return WrapperProductTypeSearchDialog(self)
            else:
                return GatedWrapperProductTypeSearchDialog(self.page, self.page.frame_locator)

        def select_advicetype(self, advice_type_text):
            return self.page.select_by_visible_text(AddSubPlanWizard.PlanStage.Locators.ADVICETYPE_SELECT_BOX,
                                                    advice_type_text)

        class Locators(BaseWizardPage.Locators):
            SELECT_ADVISER_BUTTON = (By.XPATH,
                    "//*[@id='__display_id_PlanDetailsStep_SellingAdviserId']//following-sibling::*/a[@class='hpick']")
            SELECT_PRODUCT_TYPE_BUTTON = (By.XPATH,
                    "//*[@id='__display_ProdType']//following-sibling::*/a[@class='hpick']")
            SELLLING_ADVISER_ID = (By.ID, "__id_PlanDetailsStep_SellingAdviserId")
            ADVICETYPE_SELECT_BOX = (By.ID, "id_PlanDetailsStep_AdviceTypeId")
