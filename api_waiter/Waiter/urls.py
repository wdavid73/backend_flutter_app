from django.urls import path, include
from .View.WaiterGetAndPost import GetAndPostFromAdmin

urlpatterns = [
    path("waiter/", GetAndPostFromAdmin.as_view(),
         name="get_and_post_waiter_from_admin")
]
