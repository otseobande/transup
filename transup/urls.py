from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, permissions

# views
from transup.views import index
from providers.views import ProviderViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Transup API",
      default_version='v1',
      description="An application that help manage transportation suppliers.",
      contact=openapi.Contact(email="otseobande@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'providers', ProviderViewSet)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', index),
    path('api/v1', index),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^api/v1/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api/v1/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
