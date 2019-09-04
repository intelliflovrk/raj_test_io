from ioffice.base import *


class BaseOpportunitiesPage(IOBasePage):
    def is_title_matches(self):
        return "Adviser Workplace | Clients | Opportunities | Intelligent Office" == self.driver.title
