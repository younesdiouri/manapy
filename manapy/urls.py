from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index$', views.home),
    url(r'^redirection$', views.view_redirection),
    url(r'^article/(?P<id_article>\d+)$', views.view_article, name="afficher_article"),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
]
