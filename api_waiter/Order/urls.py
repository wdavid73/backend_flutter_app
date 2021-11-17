from django.urls import path, include
from .View.OrderGetAndPost import GetAndPost
from .View.FindOrder import find_order
from .View.OrderAction import order_action
from .View.OrderClose import order_close
from .View.EditOrder import edit_order
from .Order_Complement.Views.Delete import delete_complement
from .Order_Dish.Views.Delete import delete_dish
from .Order_Drinks.Views.Delete import delete_drinks
from .View.AllOrders import all_orders

urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post"),
    path("all/" , all_orders, name="all_orders"),
    path("find_order/<str:code>/", find_order, name="find_order"),
    path("action/<str:code>/<int:action>/", order_action, name="order_action"),
    path("close/<str:code>/", order_close, name="order_close"),
    path("edit/<str:code>/", edit_order, name="edit_order"),
    path("delete_dish/<str:code>/", delete_dish, name="delete_order_dish"),
    path("delete_drink/<str:code>/", delete_drinks, name="delete_order_drink"),
    path("delete_complement/<str:code>/",
         delete_complement, name="delete_order_complement"),
    path("dish/", include("api_waiter.Order.Order_Dish.urls")),
    path("complement/", include("api_waiter.Order.Order_Complement.urls")),
    path("drink/", include("api_waiter.Order.Order_Drinks.urls")),
]
