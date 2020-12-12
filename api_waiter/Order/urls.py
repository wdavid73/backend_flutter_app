from django.urls import path, include
from .View.OrderGetAndPost import GetAndPost
from .View.FindOrder import find_order
from .View.OrderAction import order_action
from .View.OrderClose import order_close
from .View.EditOrder import edit_order, EditOrder

urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post"),
    path("find_order/<str:code>/", find_order, name="find_order"),
    path("action/<str:code>/<int:action>/", order_action, name="order_action"),
    path("close/<str:code>/", order_close, name="order_close"),
    path("edit/<str:code>/", EditOrder.as_view(), name="edit_order"),
    path("edit2/<str:code>/", edit_order, name="edit_order_2"),
    path("dish/", include("api_waiter.Order.Order_Dish.urls")),
    path("complement/", include("api_waiter.Order.Order_Complement.urls")),
    path("drink/", include("api_waiter.Order.Order_Drinks.urls")),
]
