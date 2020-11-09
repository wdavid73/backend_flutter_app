from django.urls import path, include
from .views import api_admin

urlpatterns = [
    path('api_auth/', include('auth_app.urls')),
    path("", api_admin, name="index_api_admin")
]
