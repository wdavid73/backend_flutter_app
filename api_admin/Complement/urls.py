from django.urls import path
from .View.ComplementGetAndPost import GetAndPost

urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post_complement")
]
