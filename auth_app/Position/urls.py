from django.urls import path
from .views.get_and_post import GetAndPost, GetByUser, GetByName

urlpatterns = [
    path('', GetAndPost.as_view(), name="get_and_post"),
    path('by_user/<id>/', GetByUser.as_view(), name="get_by_user"),
    path('by_name/<str:name>/', GetByName.as_view(), name="get_by_name"),

]
