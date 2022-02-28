from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.snippet_list),
    # path('<int:pk>/', views.snippet_detail)
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view())
]
# 允许给我们的网址添加可选的格式后缀
urlpatterns = format_suffix_patterns(urlpatterns)

