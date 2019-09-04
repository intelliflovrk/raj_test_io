from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By
from ioffice.adviser_search_dialog import AdviserSearchDialog


class BaseAddFeeDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, BaseAddFeeDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def open_adviser_search_dialog(self):
        self.page.click(self.Locators.SELECT_ADVISER_BUTTON)
        return AdviserSearchDialog(self.page, self.frame_locator, "id_AdviserPartyId")

    def select_fee_type(self, fee_type_text):
        self.page.select_by_visible_text(self.Locators.FEE_TYPE_SELECT_BOX, fee_type_text)
        return self

    def select_payment_type(self, payment_type_text):
        self.page.select_by_visible_text(self.Locators.PAYMENT_TYPE_SELECT_BOX, payment_type_text)
        return self

    def select_fee_charging_type(self, fee_charging_type_text):
        self.page.select_by_visible_text(self.Locators.FEE_CHARGING_TYPE_SELECT_BOX, fee_charging_type_text)
        self.wait_until_please_wait_spinner_present()
        return self

    def select_net_amount(self):
        self.page.click(self.Locators.NET_AMOUNT_VALUE)
        return self

    def select_advice_category(self, advice_catogory):
        self.page.select_by_visible_text(self.Locators.ADVICE_CATEGORY_SELECT_BOX, advice_catogory)
        return self

    def fill_in_initial_period(self, initial_period):
        self.page.fill_in_field(self.Locators.INITIAL_PERIOD_FIELD, initial_period)
        return self

    def click_save(self):
        self.page.click(self.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        _FRAME = "// iframe[contains(@src,'/nio/')]"
        SELECT_ADVISER_BUTTON = (
            By.XPATH, "//*[@id='__display_id_AdviserPartyId']//following-sibling::*/a[@class='hpick']")
        FEE_TYPE_SELECT_BOX = (By.ID, "AdviseFeeTypeId")
        PAYMENT_TYPE_SELECT_BOX = (By.ID, "AdvisePaymentTypeId")
        FEE_CHARGING_TYPE_SELECT_BOX = (By.ID, "AdviseChargingTypeDropDown")
        ADVICE_CATEGORY_SELECT_BOX = (By.ID, "FeeAdviseTypeDropDown")
        SAVE_BUTTON = (By.LINK_TEXT, "Save")
        NET_AMOUNT_VALUE = (By.XPATH, "//*[@name='AdviseFeeChargingDetailsId']//option[@value!='0']")
        INITIAL_PERIOD_FIELD = (By.ID, "id_InitialPeriod")