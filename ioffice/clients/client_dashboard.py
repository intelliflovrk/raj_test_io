from ioffice.clients.base import *


class ClientDashboardPage(BaseClientPage):
    def is_title_matches(self):
        return "Adviser Workplace | Clients | Dashboard | Intelligent Office" == self.driver.title

    class Locators(object):
        pass
