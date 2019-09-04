from ioffice.clients.base import *


class BaseQuotesPage(BaseClientPage):
    def is_title_matches(self):
        return "Quotes & Apps | Intelligent Office" == self.driver.title
