from django.urls import path
from .Views.GetAndPost import GetAndPost

urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post")
]
