from ioffice.base import IOBasePage, WebDriverWait, EC, By


class ViewWorkflowPage(IOBasePage):

    def get_steps_table_rows(self):
        return WebDriverWait(self.driver, self.TIMEOUT)\
            .until(EC.presence_of_all_elements_located(ViewWorkflowPage.Locators.STEP_DETAILS_ROW))

    class Locators(object):
        STEP_DETAILS_ROW = (By.CSS_SELECTOR, "#grid_WorkflowHistoryGrid tbody tr")
