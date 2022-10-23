
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_store import settings

urlpatterns = [
    path('', include('store.urls')),
    path('checkout/', include('checkout.urls')),
    path('admin/', admin.site.urls),
    ]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)