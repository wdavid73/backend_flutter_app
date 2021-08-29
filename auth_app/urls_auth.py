from django.urls import path
from .AuthUser.views.Register import RegisterAPI
from .AuthUser.views.Login import LoginAPI
from .AuthUser.views.Logout import Logout
from .AuthUser.views.recovery_password import RecoveryPasswordAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('recovery_password/', RecoveryPasswordAPI.as_view(), name='recovery_password'),
]
