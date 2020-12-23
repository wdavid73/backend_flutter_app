from api_waiter.Order.View.FindOrder import find_order
from django.urls import path, include
from .views import api_chef
from api_waiter.Order.View.OrderGetAndPost import GetAndPost
from api_waiter.Order.View.OrderAction import order_action
from api_waiter.Order.View.FindOrder import find_order


urlpatterns = [
    path("", api_chef, name="index_api_chef"),
    path("get_orders/", GetAndPost.as_view(), name="get_orders"),
    path("action/", order_action, name="change_action"),
    path("details_order/", find_order, name="details_order"),

    path('api_auth/', include('auth_app.urls_auth')),

]
