from django.conf.urls import url

from views import Home
from views import RegisterView
from views import ConnexionView
from views import DeconnexionView
from views import CharacterCreateView

urlpatterns = [
    url(r'^$', Home.as_view(), name='index'),
    url(r'^register/', RegisterView.as_view(), name='perso'),
    url(r'^connexion/', ConnexionView.as_view(), name='log-in'),
    url(r'^deconnexion/', DeconnexionView.as_view(), name='deconnexion'),
    url(r'^create_character/', CharacterCreateView.as_view(), name='create_character')
]