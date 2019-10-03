from django.contrib import admin
from django.urls import path, include
from backend import views
urlpatterns = [
    path('', views.index, name='index')
]