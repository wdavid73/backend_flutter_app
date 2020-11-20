from django.urls import path, include
from .views.get_and_post import GetAndPost

urlpatterns = [
    path("", GetAndPost.as_view(), name="ingredient_get_post")
]
