from django.core.exceptions import PermissionDenied
from rest_framework.request import Request
from auth_app.Restaurant.models.RestaurantModel import Restaurant

types_authorized_users = ["admin", "chef", "waiter"]
type_users_valid = ["admin", "waiter"]


def user_validate_required(view_func=None):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.position.name.lower() in types_authorized_users:
                return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = view_func.__doc__
    wrap.__name__ = view_func.__name__
    return wrap


def validate_user(request: Request) -> bool:
    if request.user.is_authenticated:
        if request.user.position.name.lower() in types_authorized_users:
            return True
    else:
        raise PermissionDenied


def type_user_valid(request: Request) -> bool:
    if request.user.is_authenticated:
        if request.user.position.name.lower() in type_users_valid:
            return True
    else:
        raise PermissionDenied


def validate_restaurant_code(request: Request) -> bool:
    code = request.user.restaurant.code
    restaurant = Restaurant.objects.filter(state=1, code=code)
    if restaurant.exists():
        return True
    else:
        raise PermissionDenied
