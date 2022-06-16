from django.contrib import admin
from django.urls import path, include
from blog import views


urlpatterns = [
    #user/
    path('', views.UserView.as_view())
]