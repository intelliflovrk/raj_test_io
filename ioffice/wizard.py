from ioffice.base import IOBasePage, IOFrameDialog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageobjects import BasePageSection, BasePage


class BaseWizardPage(IOBasePage, IOFrameDialog):
    def __init__(self, config, title):
        super(BaseWizardPage, self).__init__(config)
        self.prev_frame_locator = None
        self.title = title

    def is_title_matches(self):
        return self.title == self.driver.find_element(*BaseWizardPage.Locators.WIZARD_TITLE).text

    def click_next_button(self, throw=True):
        return self._click_button(BaseWizardPage.Locators.NEXT_BUTTON, throw)

    def click_prev_button(self, throw=True):
        return self._click_button(BaseWizardPage.Locators.PREV_BUTTON, throw)

    def click_cancel_button(self, throw=True):
        return self._click_button(BaseWizardPage.Locators.CANCEL_BUTTON, throw)

    def click_finish_button(self, throw=True):
        return self._click_button(BaseWizardPage.Locators.FINISH_BUTTON, throw)

    def _click_button(self, locator, throw=True):
        self._switch_to_frame()
        try:
            element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator))
            element.click()
            self.wait_until_please_wait_spinner_present()
            return True
        except:
            if throw: raise
            return False

    def move_to_prev_stage(self, stage_name):
        while not self.get_current_stage_name() == stage_name:
            if not self.click_prev_button(False):
                return

    def move_to_next_stage(self, stage_name):
        while not self.get_current_stage_name() == stage_name:
            if not self.click_next_button(False):
                return

    def get_current_stage_name(self):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(BaseWizardPage.Locators.CURRENT_STAGE_NAME))
        return element.text

    class Locators(object):
        WIZARD_TITLE = (By.XPATH, "//div[@class='dleLabel']")
        NEXT_BUTTON = (By.XPATH, "//div[@class='wizard-buttons']//*[@class='next button button-enabled']")
        CANCEL_BUTTON = (By.XPATH, "//div[@class='wizard-buttons']//*[@class='cancel button button-enabled']")
        FINISH_BUTTON = (By.XPATH, "//div[@class='wizard-buttons']//*[@class='complete button button-enabled']")
        PREV_BUTTON = (By.XPATH, "//div[@class='wizard-buttons']//*[@class='prev button button-enabled']")
        BLOCK_UI = (By.XPATH, "//div[@class='blockUI blockOverlay']")
        CURRENT_STAGE_NAME = (By.XPATH, "//div[@class='wizard']/ul/li[starts-with(@class, 'current')]")


class BaseWizardStage(BasePageSection):
    def __init__(self, parent_page, stage_name):
        super().__init__(parent_page)
        self.page._switch_to_frame()
        self.stage_name = stage_name

    def is_current_stage(self):
        return self.stage_name == self.page.get_current_stage_name()

    def stage_name(self):
        return self.stage_name

    def goto_stage(self):
        self.page.move_to_next_stage(self.stage_name)
        self.is_current_stage()
        return self
