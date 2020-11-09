from django.urls import path, include
from .views import api_chef

urlpatterns = [
    path('api_auth/', include('auth_app.urls_auth')),
    path("", api_chef, name="index_api_chef")
]
