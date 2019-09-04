from selenium.webdriver.common.by import By
from ioffice.clients.factfind.base import BaseFactFindPage


class AssetLiabilitiesStage(BaseFactFindPage):

    def click_assets_subtab(self):
        return self.click(AssetLiabilitiesStage.Locators.ASSETS_SUBTAB)

    def click_liabilities_subtab(self):
        return self.click(AssetLiabilitiesStage.Locators.LIABILITIES_SUBTAB)

    class Locators(BaseFactFindPage):
        ASSETS_SUBTAB = (By.CSS_SELECTOR, "#assetssub > a")
        LIABILITIES_SUBTAB = (By.CSS_SELECTOR, "#liabilitiessub > a")

    class Assets(BaseFactFindPage):

        def fill_in_description_field(self, data):
            return self.fill_in_field(AssetLiabilitiesStage.Assets.Locators.DESCRIPTION_TEXT_BOX, data)

        def fill_in_original_value_field(self, data):
            return self.fill_in_field(AssetLiabilitiesStage.Assets.Locators.ORIGINAL_VALUE_FIELD, data)

        def click_yes_radiobutton(self):
            return self.click(AssetLiabilitiesStage.Assets.Locators.YES_RADIO_BUTTON)

        def click_add_button(self):
            return self.click(AssetLiabilitiesStage.Assets.Locators.ADD_BUTTON)

        def click_save_button(self):
            return self.click(AssetLiabilitiesStage.Assets.Locators.SAVE_BUTTON)

        class Locators(BaseFactFindPage.Locators):
            YES_RADIO_BUTTON = (By.ID, "Yes_603_AnyAssets_0")
            ADD_BUTTON = (By.CSS_SELECTOR, "#assets_grid_0 > a")
            SAVE_BUTTON = (By.ID, "ff-form-save")
            ORIGINAL_VALUE_FIELD = (By.ID, "130_PurchasePrice_0")
            DESCRIPTION_TEXT_BOX = (By.ID, "AssetDescription_Description_0")

    class Liabilities(BaseFactFindPage):

        def select_liability_category_status(self, data):
            return self.select_by_visible_text(AssetLiabilitiesStage.Liabilities.Locators.LIABILITY_CATEGORY, data)

        def fill_in_description_field(self, data):
            return self.fill_in_field(AssetLiabilitiesStage.Liabilities.Locators.DESCRIPTION, data)

        def fill_in_original_amount_field(self, data):
            return self.fill_in_field(AssetLiabilitiesStage.Liabilities.Locators.ORIGINAL_LOAN_AMOUNT, data)

        def click_yes_radiobutton(self):
            return self.click(AssetLiabilitiesStage.Liabilities.Locators.YES_RADIOBUTTON)

        def click_add_button(self):
            return self.click(AssetLiabilitiesStage.Liabilities.Locators.ADD_BUTTON)

        def click_save_button(self):
            return self.click(AssetLiabilitiesStage.Liabilities.Locators.SAVE_BUTTON)

        class Locators(BaseFactFindPage.Locators):
            YES_RADIOBUTTON = (By.ID, "Yes_AnyLiabilities_AnyLiabilities_0")
            ADD_BUTTON = (By.LINK_TEXT, "Add")
            SAVE_BUTTON = (By.ID, "ff-form-save")
            DESCRIPTION = (By.ID, "135_description_0")
            ORIGINAL_LOAN_AMOUNT = (By.ID, "TotalLoanAmount_TotalLoanAmount_0")
            LIABILITY_CATEGORY = (By.XPATH, "//*[@id='1059_CommitedOutgoings_0']")
