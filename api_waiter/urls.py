from django.urls import path, include
from .views import api_waiter

urlpatterns = [
    path('api_auth/', include('auth_app.urls_auth')),
    path("", api_waiter, name="index_api_waiter")
]
