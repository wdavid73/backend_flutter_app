from django.urls import path, include
from .views.get_and_post import GetAndPost
from .views.get_dish import get_dish_with_ingredient
from .views.get_ingredients import get_ingredients_of_dish

urlpatterns = [
    path("", GetAndPost.as_view(), name="dish_get_post"),
    path("get_dish/<int:id>", get_dish_with_ingredient,
         name="get_details_of_dish"),
    path("get_ingredients/<int:id>", get_ingredients_of_dish,
         name="get_ingredients_of_dish"),
    path("dish_ingredient", include("api_admin.Dish.Dish_Ingredient.urls"))
]
