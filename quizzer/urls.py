from django.conf.urls import url
from django.contrib import admin
from . import views


app_name='quizzer'
urlpatterns = [
    url(r'^register/$',views.QuizzerRegistration, name="register"),
]
