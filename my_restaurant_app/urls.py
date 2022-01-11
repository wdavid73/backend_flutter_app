from django.conf.urls import handler400
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import view

# handler404 = view.error404

urlpatterns = [
    path('', view.index, name="index"),
    path('endpoints/', view.get_endpoints, name="endpoints"),
    path('endpoints/test', view.test_view, name="endpoints"),
    path('api_waiter/', include('api_waiter.urls')),
    path('api_chef/', include('api_chef.urls')),
    path('api_admin/', include('api_admin.urls')),
    path("api_auth/", include("auth_app.urls_auth")),
    path('restaurant/', include('auth_app.Restaurant.urls')),
    path('positions/', include("auth_app.Position.urls")),

    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# ROUTE MAP OF LOGIN
# 1. api_admin/api_auth/register (POST)
# 2. dj-rest-auth/login (POST)
# 3. dj-rest-auth/user (GET)
# 4. api_admin/positions/by_user (GET)
