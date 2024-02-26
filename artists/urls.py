from django.urls import path
from . import views

urlpatterns = [
   path('', views.ArtistList.as_view(), name='artists'),
   path('artist/<slug:artist_slug>/', views.artist_profile, name='artist_profile'),
]
