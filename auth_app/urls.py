from .views import RegisterAPI
from django.urls import path, include

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('restaurants', include("auth_app.Restaurant.urls"))
]
