from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ioffice.base import BasePageSection, IOFrameDialog


class GenerateDocumentDialog(BasePageSection, IOFrameDialog):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = GenerateDocumentDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def template_step(self):
        return GenerateDocumentDialog.TemplateStep(self.page)

    def context_step(self):
        return GenerateDocumentDialog.ContextStep(self.page)

    def prompt_step(self):
        return GenerateDocumentDialog.PromptsStep(self.page)

    def finish_step(self):
        return GenerateDocumentDialog.FinishStep(self.page)

    def click_next(self):
        return self.page.click(GenerateDocumentDialog.Locators.NEXT_BUTTON)

    def click_finish(self):
        return self.page.click(GenerateDocumentDialog.Locators.FINISH_BUTTON)

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src^='/nio/GenerateA/GenerateTemplate?templateCategoryId=']")
        NEXT_BUTTON = (By.NAME, "Next")
        FINISH_BUTTON = (By.NAME, "Finish")

    class TemplateStep(BasePageSection, IOFrameDialog):

        def get_templates_list(self):
            return WebDriverWait(self.driver, self.page.TIMEOUT).until(
                EC.presence_of_all_elements_located(GenerateDocumentDialog.TemplateStep.Locators.TEMPLATES_LIST))

        def get_radiobuttons_list(self):
            return WebDriverWait(self.driver, self.page.TIMEOUT).until(
                EC.presence_of_all_elements_located(GenerateDocumentDialog.TemplateStep.Locators.RADIO_BUTTONS_LIST))

        class Locators(object):
            TEMPLATES_LIST = (By.CSS_SELECTOR, "#author_template_results tbody tr")
            RADIO_BUTTONS_LIST = (By.CSS_SELECTOR, "#author_template_results tbody [type=radio]")

    class ContextStep(BasePageSection, IOFrameDialog):

        def select_relationships(self, relationships):
            self.page.select_by_visible_text(
                GenerateDocumentDialog.ContextStep.Locators.RELATIONSHIPS_SELECT_BOX, relationships)
            return self

        class Locators(object):
            RELATIONSHIPS_SELECT_BOX = (By.ID, "SelectedRelationshipId")

    class PromptsStep(BasePageSection, IOFrameDialog):

        def check_first_checkbox(self):
            self.page.click(GenerateDocumentDialog.PromptsStep.Locators.FIRST_PROMPT_CHECKBOX)
            return self

        class Locators(object):
            FIRST_PROMPT_CHECKBOX = (By.CSS_SELECTOR, ".ff-checklist [type='checkbox']")

    class FinishStep(BasePageSection, IOFrameDialog):
        def get_word_radio_button_state(self):
            return WebDriverWait(self.driver, self.page.TIMEOUT).until(
                EC.element_to_be_clickable(
                    GenerateDocumentDialog.FinishStep.Locators.WORD_RADIO_BUTTON)).is_selected()

        def get_pdf_radio_button_state(self):
            return WebDriverWait(self.driver, self.page.TIMEOUT).until(
                EC.element_to_be_clickable(
                    GenerateDocumentDialog.FinishStep.Locators.PDF_RADIO_BUTTON)).is_selected()

        def select_pdf_type(self):
            return self.page.click(GenerateDocumentDialog.FinishStep.Locators.PDF_RADIO_BUTTON)

        def get_navigate_to_queue_checkbox_state(self):
            return WebDriverWait(self.driver, self.page.TIMEOUT).until(
                EC.element_to_be_clickable(
                    GenerateDocumentDialog.FinishStep.Locators.REDIRECT_TO_QUEUE_CHECKBOX)).is_selected()

        class Locators(object):
            WORD_RADIO_BUTTON = (By.ID, "Word")
            PDF_RADIO_BUTTON = (By.ID, "PDF")
            REDIRECT_TO_QUEUE_CHECKBOX = (By.ID, "RedirectToQueue")
