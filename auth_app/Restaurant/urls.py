from django.urls import path
from .views.get_and_post import GetAndPost

urlpatterns = [
    path('', GetAndPost.as_view(), name="get_and_post"),
]
