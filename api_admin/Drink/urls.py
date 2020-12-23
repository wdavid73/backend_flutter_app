from django.urls import path
from .View.DrinkGetAndPost import GetAndPost

urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post_drink")
]
