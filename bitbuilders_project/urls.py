"""
URL configuration for bitbuilders_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

from django.contrib import admin

from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions
# schema_view = get_schema_view(
#     openapi.Info(
#         title="BitBuilders API",
#         default_version='v1',
#         description="API documentation for the BitBuilders project",
#         terms_of_service="https://example.com/terms/",
#         contact=openapi.Contact(email="contact@bitbuilders.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="bitbuilders API",
        default_version='v1',
        description="API documentation for the bitbuilders project",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="contact@bitbuilders.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)





urlpatterns = [
    # path('bitbuilders/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('bitbuilders/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),
    path('api/', include('user.urls')), 
    path('api/', include ("api.urls")),
    path('api/', include("order.urls")),
    path('ecoconnect/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ecoconnect/redoc/',  schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),

]


    


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




