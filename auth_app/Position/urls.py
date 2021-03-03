from django.urls import path
from .views.get_and_post import GetAndPost, GetByUser

urlpatterns = [
    path('', GetAndPost.as_view(), name="get_and_post"),
    path('by_user/<id>/', GetByUser.as_view(), name="get_by_user"),

]
