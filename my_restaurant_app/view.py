from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.exceptions import NotFound


def index(request: Request):
    if request.user.is_authenticated:
        return HttpResponse(
            '<h1 style="text-align : center ; margin-top : 50px">Welcome {}, You are at the index of app</h1>'.format(
                request.user.get_full_name())
        )

    else:
        return HttpResponse(
            '<h1 style="text-align : center ; margin-top : 50px">Hello, You are at the index of app</h1>'
        )


def error404(request):
    raise NotFound(detail="Error 404, page not found", code=404)
