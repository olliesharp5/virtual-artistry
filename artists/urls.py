from django.urls import path
from . import views
from .views import ArtistList

urlpatterns = [
    path('', ArtistList.as_view(), name='artists'),
    path('artist/<str:username>/', views.artist_profile, name='artist_profile')
]
