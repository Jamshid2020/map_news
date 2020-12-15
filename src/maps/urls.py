from django.urls import path
from .views import index, search

urlpatterns = [
    path('', index),
    path('search/', search),
]
