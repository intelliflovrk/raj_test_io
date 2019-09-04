from ioffice.clients.activities.base import ActivitiesBasePage, By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ViewClientWorkflowsPage(ActivitiesBasePage):

    def get_workflow_table_rows(self):
        return WebDriverWait(self.driver, self.TIMEOUT)\
            .until(EC.presence_of_all_elements_located(ViewClientWorkflowsPage.Locators.WORKFLOW_DETAILS_ROW))

    class Locators(object):
        WORKFLOW_DETAILS_ROW = (By.CSS_SELECTOR, "#grid_WorkflowInstanceGrid tbody tr:not(.filter)")
