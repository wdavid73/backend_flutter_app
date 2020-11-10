from django.conf.urls import handler400
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import view

# handler404 = view.error404

urlpatterns = [
    path('', view.index, name="index"),
    path('endpoints/', view.get_endpoints, name="endpoints"),
    path('api_waiter/', include('api_waiter.urls')),
    path('api_chef/', include('api_chef.urls')),
    path('api_admin/', include('api_admin.urls')),
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
