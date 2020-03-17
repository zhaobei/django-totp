from django.urls import path
from .views import greet

urlpatterns = [
    path('greet/', greet, name='example_greet'),
    path('oops/', greet, name='example_oops'),
]
