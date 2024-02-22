from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArtList.as_view(), name='home'),
]