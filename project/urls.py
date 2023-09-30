from django.urls import path
from . import views
# from django import forms

urlpatterns = [
    path('', views.home ),
    path('create/', views.create ),
    path('<str:url>', views.redirect ),
]
