from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('artwork/', include('artwork.urls')),  # include artwork app urls
]