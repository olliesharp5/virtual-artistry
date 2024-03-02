from . import views
from django.urls import path
from .views import like_artwork, unlike_artwork


urlpatterns = [
    path('', views.ArtList.as_view(), name='home'),
    path('art/<slug:art_slug>/', views.art_details, name='art_details'),
    path('art/<slug:art_slug>/edit_review/<int:review_id>/',
         views.review_edit, name='review_edit'),
    path('art/<slug:art_slug>/delete_review/<int:review_id>/',
         views.review_delete, name='review_delete'),
    path('art/<slug:art_slug>/like/', like_artwork, name='like_artwork'),
    path('art/<slug:art_slug>/unlike/', unlike_artwork, name='unlike_artwork'),
]