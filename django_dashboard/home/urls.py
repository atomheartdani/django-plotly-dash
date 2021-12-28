from django.urls import path
from . import views
from home.dash_apps import logarithm_example, square_example, weird_example

urlpatterns = [
    path('', views.index, name='index'),
    path('weird', views.weird, name='weird'),
]
