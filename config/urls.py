from django.contrib import admin
from django.urls import path, include, re_path
from .views import index
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", index),
    path(settings.ADMIN_URL, admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    re_path(
        r"^docs/(?P<path>.*)$",
        login_required(serve),
        {"document_root": settings.DOCS_ROOT},
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("drf-api-auth/", include("rest_framework.urls"))]
