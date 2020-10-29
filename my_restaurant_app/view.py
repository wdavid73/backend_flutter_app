from django.http import HttpResponse
from rest_framework.request import Request

def index(request : Request):
    return HttpResponse(
        '<h1 style="text-align : center ; margin-top : 50px">Hello, You are at the index of app</h1>'
        )
