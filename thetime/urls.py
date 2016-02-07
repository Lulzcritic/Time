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

urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    url(r'^register/', RegisterView.as_view(), name='perso'),
    url(r'^connexion/', ConnexionView.as_view(), name='log-in'),
    url(r'^deconnexion/', DeconnexionView.as_view(), name='deconnexion'),
    url(r'^create_character/', CharacterCreateView.as_view(), name='create_character'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^create_syndicat/', CreateSyndicatView.as_view(), name='create_syndicat'),
    url(r'^select_syndicat/', SelectSyndicatView.as_view(), name='select_syndicat'),
    url(r'^dashboard_syndicat/', SyndicatDashboardView.as_view(), name='dashboard_syndicat')
]