from ioffice.wizard import *
from ioffice.adviser_search_dialog import *
from ioffice.provider_search_dialog import *
from ioffice.producttype_search_dialog import *
from selenium.webdriver.support.ui import Select


class AddPlanWizard(BaseWizardPage):
    def __init__(self, config, title="Add Plan"):
        super().__init__(config, title)
        self.frame_locator = AddPlanWizard.Locators.FRAME

    def plan_stage(self):
        return AddPlanWizard.BasePlanStage(self)

    def investment_plan_stage(self):
        return AddPlanWizard.InvestmentPlanStage(self)

    def mortgage_plan_stage(self):
        return AddPlanWizard.MortgagePlanStage(self)

    def protection_plan_stage(self):
        return AddPlanWizard.ProtectionPlanStage(self)

    def retirement_plan_stage(self):
        return AddPlanWizard.RetirementPlanStage(self)

    class Locators(object):
        FRAME = (By.XPATH, "// iframe[contains(@src,'/nio/')]")

    class BasePlanStage(BaseWizardStage):
        def __init__(self, parent_page):
            super().__init__(parent_page, "Plan")
            self.is_preexting_plan = False

        def tick_is_preexisting_plan_checkbox(self):
            self.is_preexting_plan = True
            return self.page.click(AddPlanWizard.BasePlanStage.Locators.IS_PRE_EXISTING_PLAN_CHECKBOX)

        def open_adviser_search_dialog(self):
            self.page.click(AddPlanWizard.BasePlanStage.Locators.SELECT_ADVISER_BUTTON)
            return AdviserSearchDialog(self.page, self.page.frame_locator, "id_PlanDetailsStep_SellingAdviserId")

        def select_advicetype(self, advice_type_text):
            return self.page.select_by_visible_text(AddPlanWizard.BasePlanStage.Locators.ADVICETYPE_SELECT_BOX,
                                                    advice_type_text)

        def open_provider_search_dialog(self):
            WebDriverWait(self.driver, self.page.TIMEOUT).until(
                EC.element_to_be_clickable(AddPlanWizard.BasePlanStage.Locators.SELECT_PROVIDER_BUTTON)).click()
            if self.is_preexting_plan:
                return FullProviderSearchDialog(self.page, self.page.frame_locator)
            else:
                return ProviderSearchDialog(self.page, self.page.frame_locator)

        def open_producttype_search_dialog(self):
            WebDriverWait(self.driver, self.page.TIMEOUT).until(
                EC.element_to_be_clickable(
                    AddPlanWizard.BasePlanStage.Locators.SELECT_PRODUCT_TYPE_BUTTON)).click()
            if self.is_preexting_plan:
                return ProductTypeSearchDialog(self.page, self.page.frame_locator)
            else:
                return GatedProductTypeSearchDialog(
                    self.page, self.page.frame_locator)

        class Locators(object):
            IS_PRE_EXISTING_PLAN_CHECKBOX = (By.ID, "id_PlanDetailsStep_IsPreExistingPlan")
            SELECT_PROVIDER_BUTTON = (By.XPATH, "//*[@id='__display_id_PlanDetailsStep_ProductProviderId']//following-sibling::*/a[@class='hpick']")
            SELECT_PRODUCT_TYPE_BUTTON = (By.XPATH, "//*[@id='__display_ProdType']//following-sibling::*/a[@class='hpick']")
            ADVICETYPE_SELECT_BOX = (By.ID, "id_PlanDetailsStep_AdviceTypeId")
            SELECT_ADVISER_BUTTON = (By.XPATH, "//*[@id='__display_id_PlanDetailsStep_SellingAdviserId']//following-sibling::*/a[@class='hpick']")

    class InvestmentPlanStage(BasePlanStage):
        def fill_in_lump_sum_amount(self, amount):
            return self.page.fill_in_field(AddPlanWizard.InvestmentPlanStage.Locators.LUMP_SUM_AMOUNT_FIELD, amount)

        def fill_in_effective_date(self, date):
            return self.page.fill_in_field(AddPlanWizard.InvestmentPlanStage.Locators.EFFECTIVE_DATE, date)

        class Locators(object):
            LUMP_SUM_AMOUNT_FIELD = (By.ID, "id_PlanDetailsStep_LumpSumAmount")
            EFFECTIVE_DATE = (By.ID, "id_PlanDetailsStep_EffectiveDate")

    class MortgagePlanStage(BasePlanStage):

        def is_mortgage_details_section_present(self):
            return "Mortgage Details" == WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    AddPlanWizard.MortgagePlanStage.Locators.MORTGAGE_DETAILS_SECTION_LABEL)).text

        def select_second_owner(self, data):
            self.page.select_by_visible_text(self.Locators.SECOND_OWNER, data)
            return self

        def fill_in_price_valuation(self, data):
            self.page.clear_and_fill_in_field(self.Locators.PRICE_VALUATION, data)
            return self

        def fill_in_deposit_equity(self, data):
            self.page.clear_and_fill_in_field(self.Locators.DEPOSIT_EQUITY, data)
            return self

        class Locators(object):
            MORTGAGE_DETAILS_SECTION_LABEL = (By.XPATH, "//div[@id='MortgageDetails_Others']//div[@class='label']")
            SECOND_OWNER = (By.ID, "MortgageOwner2")
            PRICE_VALUATION = (By.ID, "Price")
            DEPOSIT_EQUITY = (By.ID, "Deposit")

    class ProtectionPlanStage(BasePlanStage):

        def fill_in_life_cover_sum_assured(self, amount):
            self.page.clear_and_fill_in_field(self.Locators.LIFE_COVER_SUM_ASSURED_FIELD, amount)
            return self

        def fill_in_life_cover_term(self, amount):
            self.page.clear_and_fill_in_field(self.Locators.LIFE_COVER_TERM_FIELD, amount)
            return self

        def fill_in_premium_amount(self, amount):
            self.page.clear_and_fill_in_field(self.Locators.PREMIUM_AMOUNT_FIELD, amount)
            return self

        def fill_in_premium_start_date(self, amount):
            self.page.clear_and_fill_in_field(self.Locators.PREMIUM_START_DATE_FIELD, amount)
            return self

        def select_premium_frequency(self, premuim_frequency):
            el = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AddPlanWizard.ProtectionPlanStage.Locators.PREMIUM_FREQUENCY_SELECT_BOX))
            Select(el).select_by_visible_text(premuim_frequency)

        class Locators(object):
            LIFE_COVER_SUM_ASSURED_FIELD = (By.ID, "id_TermProtectionDetails_LifeCoverSumAssured")
            LIFE_COVER_TERM_FIELD = (By.ID, "id_TermProtectionDetails_LifeCoverTerm")
            PREMIUM_AMOUNT_FIELD = (By.ID, "id_TermProtectionDetails_RegularContributionDetails_Amount")
            PREMIUM_START_DATE_FIELD = (By.ID, "id_TermProtectionDetails_RegularContributionDetails_StartDate")
            PREMIUM_FREQUENCY_SELECT_BOX = (By.ID, "id_TermProtectionDetails_RegularContributionDetails_RefFrequencyId")

    class RetirementPlanStage(BasePlanStage):
        def fill_in_lump_sum(self, amount):
            self.page.fill_in_field(AddPlanWizard.RetirementPlanStage.Locators.LUMP_SUN_AMOUNT_FIELD, amount)
            return self

        def fill_in_effective_date(self, date):
            return self.page.fill_in_field(AddPlanWizard.RetirementPlanStage.Locators.EFFECTIVE_DATE, date)

        class Locators(object):
            LUMP_SUN_AMOUNT_FIELD = (By.ID, "id_PlanDetailsStep_LumpSumAmount")
            EFFECTIVE_DATE = (By.ID, "id_PlanDetailsStep_EffectiveDate")
