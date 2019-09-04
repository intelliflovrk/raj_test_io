from ioffice.adviserworkplace import AdviserWorkplacePage
from ioffice.adviser_workplace.fund_analysis.base import FundAnalysisBasePage
from ioffice.base import IOBasePage
from ioffice.income.administration import IncomeAdministrationBasePage, PaymentRunsPage
from ioffice.income.base import IncomeBasePage
from ioffice.income.provider_statements import ProviderStatementsBasePage
from ioffice.plans.base import BasePlanPage


class UserSystemNavigation:

    def __init__(self, config):
        self.config = config

    def adviser_workplace(self):
        IOBasePage(self.config).level1_menu().hover_over_navigation_menu().click_adviserworkplace()
        return AdviserWorkplaceNavigation(self.config)

    def income(self):
        IOBasePage(self.config).level1_menu().hover_over_navigation_menu().click_income()
        return IncomeNavigation(self.config)


class AdviserWorkplaceNavigation(UserSystemNavigation):

    def fund_analysis_tab(self):
        AdviserWorkplacePage(self.config).adviser_workplace_level_menu().click_fund_analysis_tab()
        return FundAnalysisNavigation(self.config)


class IncomeNavigation(UserSystemNavigation):

    def income_administration_tab(self):
        IncomeBasePage(self.config).level2_menu().click_administration()
        return IncomeAdministrationNavigation(self.config)

    def provider_statements_tab(self):
        IncomeBasePage(self.config).level2_menu().click_provider_statements()
        return ProviderStatementsNavigation(self.config)


class UserHomeNavigation(UserSystemNavigation):
    pass


class MyDashboardNavigation(UserHomeNavigation):
    pass


class FundAnalysisNavigation(AdviserWorkplaceNavigation):

    def rebalance_tab(self):
        FundAnalysisBasePage(self.config).fund_analysis_level_menu().click_rebalance_tab()
        return RebalanceNavigation(self.config)


class ProviderStatementsNavigation(IncomeNavigation):

    def statement_search_tab(self):
        ProviderStatementsBasePage(self.config).click_statement_search_tab()
        return self

    def electronic_imports_tab(self):
        ProviderStatementsBasePage(self.config).click_electronic_imports_tab()
        return self


class IncomeAdministrationNavigation(IncomeNavigation):

    def payment_runs_tab(self):
        IncomeAdministrationBasePage(self.config).click_payment_run()
        return PaymentRunsNavigation(self.config)


class PaymentRunsNavigation(IncomeAdministrationNavigation):

    def payment_history_tab(self):
        PaymentRunsPage(self.config).click_payment_history()
        return self

    def period_end_history_tab(self):
        PaymentRunsPage(self.config).click_period_end_history()
        return self


class RebalanceNavigation(FundAnalysisNavigation):
    pass


class ClientNavigation(AdviserWorkplaceNavigation):
    pass


class PlanNavigation(ClientNavigation):

    def more_tabs(self):
        BasePlanPage(self.config).plan_level_menu().click_more_tabs()
        return self

    def recommendations_tab(self):
        BasePlanPage(self.config).plan_level_menu().click_recommendations_tab()
        return self
