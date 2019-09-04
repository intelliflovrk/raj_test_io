from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class AddValuationDialog(BasePageSection, IOFrameDialog):

    def __init__(self, client_id, plan_id, parent_page):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, AddValuationDialog.Locators._FRAME.format(client_id, plan_id))
        self.frame_locator = self.FRAME
        self._switch_to_frame()

    def valuation_type_step(self):
        return AddValuationDialog.ValuationTypeStep(self.frame_locator, self.page)

    def manual_valuation_step(self):
        return AddValuationDialog.ManualValuationStep(self.frame_locator, self.page)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/Ce/{0}/SelectValuationType/{1}']"

    class ValuationTypeStep(BasePageSection, IOFrameDialog):
        def __init__(self, frame, parent_page):
            super().__init__(parent_page)
            self.frame_locator = frame
            self._switch_to_frame()

        def select_manual_valuation_type(self):
            self.page.click(AddValuationDialog.ValuationTypeStep.Locators.MANUAL_RADIO_BUTTON)
            return self

        def click_next_button(self):
            self.page.click(AddValuationDialog.ValuationTypeStep.Locators.NEXT_BUTTON)
            return self

        class Locators(object):
            MANUAL_RADIO_BUTTON = (By.ID, "ValuationType_2")
            NEXT_BUTTON = (By.CSS_SELECTOR, "#Description_2_7")

    class ManualValuationStep(BasePageSection, IOFrameDialog):
        def __init__(self, frame, parent_page):
            super().__init__(parent_page)
            self.frame_locator = frame
            self.prev_frame_locator = None
            self._switch_to_frame()

        def clear_plan_value(self):
            self.page.clear(AddValuationDialog.ManualValuationStep.Locators.PLAN_VALUE_FIELD)
            return self

        def fill_in_plan_value(self, value):
            self.page.fill_in_field(AddValuationDialog.ManualValuationStep.Locators.PLAN_VALUE_FIELD, value)
            return self

        def click_add_button(self):
            self.page.click(AddValuationDialog.ManualValuationStep.Locators.ADD_BUTTON)
            return self

        class Locators(object):
            ADD_BUTTON = (By.CSS_SELECTOR, "#id_root_2_2_2_4")
            PLAN_VALUE_FIELD = (By.ID, "id_Amount")
