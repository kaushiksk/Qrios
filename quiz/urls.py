from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'quiz'

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    url(r'^detail/(?P<questionid>[0-9]+)/$', views.detail, name="detail"),
    url(r'^answer/(?P<questionid>[0-9]+)/$', views.answer, name="answer"),
    url(r'^leaderboard/$', views.leaderboard, name="leaderboard"),
]
