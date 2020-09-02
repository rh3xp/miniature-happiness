from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from home import views

urlpatterns = [
        path('', RedirectView.as_view(url="home/")),  
        path('home/', views.home),
        ]

