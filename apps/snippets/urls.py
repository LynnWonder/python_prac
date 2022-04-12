from django.urls import path, include
from apps.snippets import views
# 使用 ModelViewSet 之后也要更新路由设置，使用 register 的方式
from rest_framework.routers import DefaultRouter

# tip 必须添加这个，不添加 app_name UT 跑不过
app_name = 'snippet'

# TIP 这里是使用 ModelViewSet 之后注册视图的用法
router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('snippets', views.SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # TIP 使用
    path('apiview/<int:pk>/', views.SnippetDetailViewSet.as_view())
]
# 允许给我们的网址添加可选的格式后缀 暂时不这么设置
# urlpatterns = format_suffix_patterns(urlpatterns)

