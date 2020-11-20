from django.shortcuts import render
from django.http import HttpResponse
from auth_app.Restaurant.models.RestaurantModel import Restaurant


def api_admin(request):
    print(Restaurant.objects.filter(state=1))
    if request.user.is_authenticated:
        return HttpResponse("api admin , user is authenticated")
    else:
        return HttpResponse("api admin , user is not authenticated")
