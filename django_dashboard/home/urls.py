from django.urls import path
from . import views
from home.dash_apps import logarithm_example, square_example

urlpatterns = [
    path('', views.index, name='index'),
]
