from ioffice.leads.base import *
import re


class LeadDetailsPage(BaseLeadPage):

    def is_title_matches(self):
        return "Lead Details Summary | Intelligent Office" == self.driver.title

    def get_lead_id(self):
        url = self.get_attribute(self.Locators.ONCLICK_ATTRIBUTE, "onclick")
        WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(LeadDetailsPage.Locators.LEAD_NAME_FIELD))
        return re.search(r'(?<=leadaddaddress/)\d+', url, flags=re.IGNORECASE).group(0)

    def get_full_name_value(self):
        return self.get_text(LeadDetailsPage.Locators.FULL_NAME)

    def click_relationships_tab(self):
        self.click(self.Locators.RELATIONSHIPS_TAB )
        return self

    class Locators(object):
        LEAD_NAME_FIELD = (By.ID, "id_Name_ro")
        ONCLICK_ATTRIBUTE = (By.CSS_SELECTOR, "a[onclick*='leadaddaddress']")
        FULL_NAME = (By.CSS_SELECTOR, ".bar-info > strong")
        RELATIONSHIPS_TAB = (By.XPATH, "//div[contains(text(),'Relationships')]")