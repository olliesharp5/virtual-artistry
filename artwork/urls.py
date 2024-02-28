from . import views
from django.urls import path

urlpatterns = [
    path('', views.ArtList.as_view(), name='home'),
    path('art/<slug:art_slug>/', views.art_details, name='art_details'),
    path('<slug:art_slug>/edit_review/<int:review_id>/',
         views.review_edit, name='review_edit'),
]