from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_nested import routers

from .views import CoordinatesViewSet, ResultViewSet, status_service

v1_router = routers.SimpleRouter()

v1_router.register("coordinates", CoordinatesViewSet, basename="coordinates")
v1_router.register("result", ResultViewSet, basename="result")

cadastral_router = routers.NestedSimpleRouter(
    v1_router,
    "coordinates",
    lookup="coordinate",
)

schema_view = get_schema_view(
    openapi.Info(
        title="WhatUR Coordinates",
        default_version="v1",
        description="Документация для API WhatUR Coordinates",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(v1_router.urls)),
    path("", include(cadastral_router.urls)),
    path("ping/", status_service),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]

urlpatterns += staticfiles_urlpatterns()
