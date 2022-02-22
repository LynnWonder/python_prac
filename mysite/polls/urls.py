from django.urls import path
from . import views

app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name='index'),
#     # the 'name' value as called by the {% url %} template tag
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]

# 将代码改造成通用视图模式
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
