from django.contrib import admin
from django.urls import path,include
from homelog import views

urlpatterns = [
    path('', views.home, name="home"),
]