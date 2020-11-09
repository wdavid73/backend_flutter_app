from django.conf import settings
from django.urls import path, include
from .AuthUser.views.Register import RegisterAPI
from .AuthUser.views.Login import LoginAPI
from .AuthUser.views.Logout import Logout


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
