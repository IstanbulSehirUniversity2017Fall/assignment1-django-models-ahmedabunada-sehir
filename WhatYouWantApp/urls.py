from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'test', views.test,name='test'),
    url(r"^(?P<EpisodeId>[0-9]+)/$", views.WhichEpisode, name='details'),
]