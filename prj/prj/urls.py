from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MIDIA_ROOT)
