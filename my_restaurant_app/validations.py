from rest_framework.request import Request
from auth_app.Restaurant.models.RestaurantModel import Restaurant

types_authorized_users = ["admin", "chef", "waiter"]


def validate_user(request: Request) -> bool:
    if request.user.is_authenticated:
        if request.user.position.name.lower() in types_authorized_users:
            return True
    return False


def validate_restaurant_code(request: Request) -> bool:
    code = request.data["restaurant_code"]
    restaurant = Restaurant.objects.filter(state=1, code=code)
    if restaurant.exists():
        return True
    return False
