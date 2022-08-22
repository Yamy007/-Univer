from django.urls import path
from .import views

urlpatterns = [

    path('', views.index),
    path('about', views.about),
    path('information', views.information),
    path('flx', views.FLXhomevorwk),
]
