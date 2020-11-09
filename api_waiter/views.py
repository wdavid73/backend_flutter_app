from django.shortcuts import render
from django.http import HttpResponse
from .validate_user import validate


def api_waiter(request):
    if validate(request, 'waiter'):
        print(request.user.position)
        return HttpResponse("api waiter , user is authenticated and user is a waiter")
    else:
        return HttpResponse("api waiter , user is not authenticated or user is not a waiter")
