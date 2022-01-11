from django.http import HttpResponse
from django.conf import settings
from django.urls import URLPattern, URLResolver, get_resolver
from django.urls.conf import re_path
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import NotFound

urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])


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


def listEndpoints(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        yield acc + [str(l.pattern)]
    elif isinstance(l, URLResolver):
        yield from listEndpoints(l.url_patterns, acc+[str(l.pattern)])
    yield from listEndpoints(lis[1:], acc)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_endpoints(request: Request):
    list = []
    for p in listEndpoints(urlconf.urlpatterns):
        list.append(''.join(p))
    return Response({'endpoint': list}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def test_view(request: Request):
    """ try:
        print(request.FILES)
        filepath = True if 'file' in request.FILES else False
        return Response({'data': filepath}, status=status.HTTP_200_OK)    
    except: """
    return Response({"error": "ha ocurrido un error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)