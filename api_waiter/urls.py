from django.urls import path, include
from .views import api_waiter

urlpatterns = [
    path("", api_waiter, name="index_api_waiter"),
    path("orders/", include("api_waiter.Order.urls")),

    # Authentication
    #path('api_auth/', include('auth_app.urls_auth')),


]
