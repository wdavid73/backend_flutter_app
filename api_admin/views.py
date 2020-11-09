from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def api_admin(request):
    print(request.user)
    if request.user.is_authenticated:
        return HttpResponse("api admin , user is authenticated")
    else:
        return HttpResponse("api admin , user is not authenticated")
