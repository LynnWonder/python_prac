"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets & polls demo API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    url=settings.SWAGGER_BASE_URL,
    public=True,
    permission_classes=[AllowAny, ]
)

router = routers.DefaultRouter()
# tip 根 URLconf，配置所有路由
#
urlpatterns = [
    # 通过 URL 自动路由来给我们的 API 布局
    path('', include(router.urls)),
    path('polls/', include('apps.polls.urls')),
    path('snippets/', include('apps.snippets.urls')),
    # tip 根 URLconf，配置 admin 管理路由
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]
