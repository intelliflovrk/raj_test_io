from ioffice.userdashboard import *
from selenium.webdriver.common.by import By


class BaseSchemePage(IOBasePage):

    def click_first_open_link(self):
        return self.click(self.Locators.OPEN_LINK)

    def click_members_tab(self):
        return self.click(BaseSchemePage.Locators.MEMBERS_TAB)

    def click_add_to_scheme(self):
        return self.click(self.Locators.ADD_TO_SCHEME_BUUTON)

    def select_first_member_check_box(self):
        return self.click(self.Locators.FIRST_CHECKBOX)

    class Locators(object):
        MEMBERS_TAB = (By.XPATH, "//div[contains(@class, 'ux-lib-tbody') and text() = 'Members']")
        OPEN_LINK = (By.CSS_SELECTOR, "[title='Open']")
        FIRST_CHECKBOX = (By.XPATH, "//table[@id='grid_MembersGrid']/tbody/tr[2]//td/input")
        ADD_TO_SCHEME_BUUTON = (By.ID, "MembersGrid_14")






