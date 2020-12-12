from django.urls import path, include
from .View.OrderGetAndPost import GetAndPost
from .View.FindOrder import find_order
from .View.OrderAction import order_action
from .View.OrderClose import order_close


urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post"),
    path("find_order/<str:code>/", find_order, name="find_order"),
    path("action/<str:code>/<int:action>/", order_action, name="order_action"),
    path("close/<str:code>/", order_close, name="order_close"),
    path("dish/", include("api_waiter.Order.Order_Dish.urls")),
    path("complement/", include("api_waiter.Order.Order_Complement.urls")),
    path("drink/", include("api_waiter.Order.Order_Drinks.urls")),
]
