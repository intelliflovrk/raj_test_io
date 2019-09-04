from ioffice.clients.base import *


class BaseFeesPage(BaseClientPage):

    def get_fee_id(self):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(BaseFeesPage.Locators.BAR_INFO))
        return re.search(r'(?<=viewrecord/)\d+', self.driver.current_url, flags=re.IGNORECASE).group(0)

    def get_fee_ref(self):
        result = re.search(r'(?<=IOF)\d+', self.get_text(BaseFeesPage.Locators.STATUS_AND_REF_BAR_INFO)).group(0)
        return "IOF"+result

    def is_title_matches(self):
        return "Client Fee Details | Intelligent Office" == self.driver.title

    def get_fee_charging_type(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.Locators.FEE_CHARGING_TYPE_VALUE)).text

    def get_total_amount(self):
        return self.get_text(self.Locators.TOTAL_AMOUNT_VALUE).replace("£", "")

    def get_fee_status(self):
        return self.get_text(self.Locators.FEE_STATUS_VALUE)

    def get_fee_category(self):
        return self.get_text(self.Locators.FEE_CATEGORY)

    class Locators(object):
        FEE_CATEGORY_FIELD = (By.ID, "id_RefAdviseFeeTypeName_ro")
        FEE_CHARGING_TYPE_VALUE = (By.XPATH, "//*[@id='AdviseFeeChargingTypeDropDown']//*[@selected='selected']")
        TOTAL_AMOUNT_VALUE = (By.CSS_SELECTOR, "#id_TotalAmount_ro")
        FEE_STATUS_VALUE = (By.CSS_SELECTOR, "#id_FeeStatus_ro")
        BAR_INFO = (By.XPATH, "//div[@class='bar-info']")
        STATUS_AND_REF_BAR_INFO = (By.XPATH, "//div[@class='bar-info']")
        FEE_CATEGORY = (By.ID, "id_RefAdviseFeeTypeName_ro")


class FeeActionsMenuSection(BaseFeesPage):

    def hover_over_fee_actions(self):
        return self.hover_over(self.Locators.ACTIONS_MENU)

    def change_fee_status(self):
        return self.click(self.Locators.CHANGE_STATUS_ACTION)
        
    class Locators(object):
        CHANGE_STATUS_ACTION = (By.XPATH, "//ul[@class='droplist-items group']//*[contains(text(), 'Change Status')]")
        ACTIONS_MENU = (By.ID, "secondary")
