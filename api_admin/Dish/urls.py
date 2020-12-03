from django.urls import path
from .views.get_and_post import GetAndPost
from .views.get_dish import get_dish_with_ingredient

urlpatterns = [
    path("", GetAndPost.as_view(), name="dish_get_post"),
    path("get_dish/<int:id>", get_dish_with_ingredient,
         name="get_details_of_dish")
]
