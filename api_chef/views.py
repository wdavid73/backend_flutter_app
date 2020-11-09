from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def api_chef(request):
    print(request.user)
    if request.user.is_authenticated:
        return HttpResponse("api chef , user is authenticated")
    else:
        return HttpResponse("api chef , user is not authenticated")
