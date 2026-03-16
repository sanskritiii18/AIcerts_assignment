from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Entity Mapping API",
        default_version='v1',
        description="API documentation for Vendor, Product, Course, Certification mappings",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/", include("vendor.urls")),
    path("api/", include("product.urls")),
    path("api/", include("course.urls")),
    path("api/", include("certification.urls")),
    path("api/", include("vendor_product_mapping.urls")),
    path("api/", include("product_course_mapping.urls")),
    path("api/", include("course_certification_mapping.urls")),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),

    # ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

]