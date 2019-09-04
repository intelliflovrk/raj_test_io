from selenium.webdriver.common.by import By
from ioffice.clients.factfind.base import BaseFactFindPage


class ExportClientDataSection(BaseFactFindPage):

    def click_go_button(self):
        return self.click(ExportClientDataSection.Locators.GO_BUTTON)

    class Locators(object):
        GO_BUTTON = (By.ID, "id_root_2_2_3_4")
