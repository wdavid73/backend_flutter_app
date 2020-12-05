from django.urls import path, include
from .View.OrderGetAndPost import GetAndPost
from .View.FindOrder import find_order


urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post"),
    path("find_order/<str:code>/", find_order, name="find_order"),
    path("dish/", include("api_waiter.Order.Order_Dish.urls")),
]
