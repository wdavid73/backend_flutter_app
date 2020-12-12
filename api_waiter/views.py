from django.shortcuts import render
from django.http import HttpResponse
from my_restaurant_app.validations import validate_user


def api_waiter(request):
    if validate_user(request):
        print(request.user.position)
        return HttpResponse("api waiter , user is authenticated and user is a waiter")
    else:
        return HttpResponse("api waiter , user is not authenticated or user is not a waiter")
