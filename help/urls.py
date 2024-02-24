from django.urls import path
from . import views

urlpatterns = [
    path('', views.help_page, name='help'),
]