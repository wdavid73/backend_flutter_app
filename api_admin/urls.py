from django.urls import path, include
from .views.api_admin import api_admin
from .views.list_users import list_chefs, list_waiters

urlpatterns = [
    path("", api_admin, name="index_api_admin"),
    path("dish/", include("api_admin.Dish.urls")),
    path("ingredients/", include("api_admin.Ingredient.urls")),
    path("dish/ingredients/", include("api_admin.Dish.urls")),
    path("tables/", include("api_admin.Table.urls")),
    path("register/", include("api_waiter.Waiter.urls")),
    path("complement/", include("api_admin.Complement.urls")),
    path("drink/", include("api_admin.Drink.urls")),
    path("list_chefs/", list_chefs, name="list_of_chefs"),
    path("list_waiters/", list_waiters, name="list_of_waiters"),
    # Authentication
    path('api_auth/', include('auth_app.urls')),
]
