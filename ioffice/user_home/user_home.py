from ioffice.base import IOBasePage, BasePageSection


class HomeBasePage(IOBasePage):

    def home_level_menu(self):
        return HomeLevelMenuSection(self)


class HomeLevelMenuSection(BasePageSection):
    pass