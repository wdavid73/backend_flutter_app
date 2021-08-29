from django.conf import settings
from django.urls import path, include
from .AuthUser.views.Register import RegisterAPI
from .AuthUser.views.Login import LoginAPI
from .AuthUser.views.Logout import Logout
from .AuthUser.views.recovery_password import RecoveryPasswordAPI


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('recovery_password/', RecoveryPasswordAPI.as_view(), name='recovery_password'),
    path('restaurants/', include("auth_app.Restaurant.urls")),
    path('positions/', include("auth_app.Position.urls")),
]
