from . import views
from django.urls import path
from .views import like_artwork


urlpatterns = [
    path('', views.ArtList.as_view(), name='home'),
    path('art/<slug:art_slug>/', views.art_details, name='art_details'),
    path('create_advert/', views.create_advert, name='create_advert'), 
    path('art/<slug:art_slug>/edit_review/<int:review_id>/',
         views.review_edit, name='review_edit'),
    path('art/<slug:art_slug>/delete_review/<int:review_id>/',
         views.review_delete, name='review_delete'),
    path('art/<slug:art_slug>/edit_artwork/', views.artwork_edit, name='artwork_edit'),
    path('art/<slug:art_slug>/delete_artwork/', views.artwork_delete, name='artwork_delete'),
    path('art/<slug:art_slug>/like/', views.like_artwork, name='like_artwork'),
]
