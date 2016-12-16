from django.conf.urls import url
from django.contrib import admin
from . import views


app_name='quizzer'
urlpatterns = [
    url(r'^register/$',views.QuizzerRegistration, name="register"),
    url(r'^login/$', views.LoginRequest, name="login"),
    url(r'^logout/$', views.LogoutRequest, name="logout"),
]
