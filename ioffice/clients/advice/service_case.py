from ioffice.clients.base import BaseClientPage
from ioffice.clients.advice.planning_tabs_section import PlanningTabsSection


class ServiceCaseBasePage(BaseClientPage):

    def __init__(self, config):
        super().__init__(config)
        self.planning_tabs = PlanningTabsSection(self)
