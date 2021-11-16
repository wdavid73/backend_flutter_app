from django.urls import path
from .views.get_and_post import post, GetCodeByUserId
from .views.getRestaurants import getRestaurants

urlpatterns = [
    path('', post, name="post"),
    path('get/', getRestaurants, name="get"),
    path('code/<int:id>/', GetCodeByUserId.as_view(), name="get_code_by_user_id"),
]
