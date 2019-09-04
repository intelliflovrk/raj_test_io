from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageobjects import BasePageSection, BasePage


class BaseWizardPage(BasePage):

    def click_next_button(self):
        self.click(BaseWizardPage.Locators.NEXT_BUTTON)
        return self

    def get_current_stage_name(self):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(BaseWizardPage.Locators.CURRENT_STAGE_BUTTON))
        return element.get_attribute("Title")

    def move_to_next_stage(self, stage_name):
        while not self.get_current_stage_name() == stage_name:
            if not self.click_next_button():
                return

    class Locators(object):
        NEXT_BUTTON = (By.CSS_SELECTOR, "button[data-nextbutton='nextButton']")
        CURRENT_STAGE_BUTTON = (By.CSS_SELECTOR, "button[class*='current']")


class BaseWizardStage(BasePageSection):
    def __init__(self, stage_name, parent_page):
        super().__init__(parent_page)
        self.stage_name = stage_name

    def is_current_stage(self):
        return self.stage_name == BaseWizardPage(self.config).get_current_stage_name()

    def stage_name(self):
        return self.stage_name

    def goto_stage(self):
        self.page.move_to_next_stage(self.stage_name)
        return self



