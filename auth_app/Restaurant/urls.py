from django.urls import path
from .views.get_and_post import GetAndPost, GetCodeByUserId
from .views.getRestaurants import getRestaurants

urlpatterns = [
    path('', GetAndPost.as_view(), name="post"),
    path('get/', getRestaurants, name="get"),
    path('code/<int:id>/', GetCodeByUserId.as_view(), name="get_code_by_user_id"),
]
