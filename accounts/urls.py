from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('art/edit/<slug:art_slug>/', views.draft_artwork_edit, name='art_edit'),
    path('art/delete/<slug:art_slug>/', views.draft_artwork_delete, name='art_delete'),
]