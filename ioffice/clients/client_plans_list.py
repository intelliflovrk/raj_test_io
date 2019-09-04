from ioffice.clients.base import *
from selenium.webdriver.common.by import By


class ClientListPlansPage(BaseClientPage):

    def click_open_first_link(self):
        self.click(self.Locators.FIRST_REF)
        return self

    class Locators(object):
        FIRST_REF = (By.XPATH, "//table[@id='grid_ClientPlansGrid']/tbody/tr[2]/td//a")
