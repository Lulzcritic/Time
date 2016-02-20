from django.conf.urls import url

from views import Home
from views import RegisterView
from views import ConnexionView
from views import DeconnexionView
from views import CharacterCreateView
from views import DashboardView
from views import CreateSyndicatView
from views import SelectSyndicatView
from views import SyndicatDashboardView
from views import SelectRoleView
from views import WorkPageView
from views import AddTimeView
from views import MarketView
from views import SellView
from views import DieView
from views import InventoryView

urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    url(r'^register/', RegisterView.as_view(), name='perso'),
    url(r'^connexion/', ConnexionView.as_view(), name='log-in'),
    url(r'^deconnexion/', DeconnexionView.as_view(), name='deconnexion'),
    url(r'^create_character/', CharacterCreateView.as_view(), name='create_character'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^create_syndicat/', CreateSyndicatView.as_view(), name='create_syndicat'),
    url(r'^select_syndicat/', SelectSyndicatView.as_view(), name='select_syndicat'),
    url(r'^dashboard_syndicat/', SyndicatDashboardView.as_view(), name='dashboard_syndicat'),
    url(r'^select_role/', SelectRoleView.as_view(), name='select_role'),
    url(r'^workpage/', WorkPageView.as_view(), name='workpage'),
    url(r'^add_time/', AddTimeView.as_view(), name='add_time'),
    url(r'^market/', MarketView.as_view(), name='market'),
    url(r'^die/', DieView.as_view(), name='die'),
    url(r'^market_sell/', SellView.as_view(), name='market_sell'),
    url(r'^inventory/', InventoryView.as_view(), name='inventory')
]