from django.urls import path, include
from apps.snippets import views
# 使用 ModelViewSet 之后也要更新路由设置，使用 register 的方式
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('snippets', views.SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# 允许给我们的网址添加可选的格式后缀 暂时不这么设置
# urlpatterns = format_suffix_patterns(urlpatterns)

