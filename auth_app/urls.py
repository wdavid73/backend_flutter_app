from .AuthUser.views.Register import RegisterAPI
from .AuthUser.views.Login import LoginAPI
from .AuthUser.views.Logout import Logout
from django.urls import path, include

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('restaurants', include("auth_app.Restaurant.urls")),
    path('positions', include("auth_app.Position.urls"))
]
