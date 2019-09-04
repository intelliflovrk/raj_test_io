from pfp.userdashboard import UserDashboardPage
from pfp.recommendation import RecommendationPage
from pfp.accept_recommendation_dialog import AcceptRecommendationDialog


class AcceptRecommendation:

    def __init__(self, config):
        self.config = config

    def accept_recommendation(self):
        UserDashboardPage(self.config).click_rebalance_recommended()
        recommendatio_page = RecommendationPage(self.config)
        recommendatio_page.click_accept()
        AcceptRecommendationDialog(recommendatio_page).click_accept()
        return self
