# Create your views here.
# 创建基于类的视图,基于类的视图来编写我们的 API 视图，而不是基于函数的视图，
# 基于类的视图会允许我们重用常用功能
from django_filters import rest_framework as filters
from rest_framework import permissions
# tip REST框架还引入了一个Response对象，这是一种获取未渲染（unrendered）内容的TemplateResponse类型，并使用内容协商来确定返回给客户端的正确内容类型
from rest_framework.response import Response
from rest_framework.views import APIView
# 新使用的 ModelViewSet 类
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException

from apps.snippets.models import Snippet
from django.contrib.auth.models import User
from apps.snippets.serializers import (SnippetSerializer, UserSerializer)
from apps.snippets.permissions import IsOwnerOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# 使用基于函数的视图需要的依赖
from django.http import (Http404, HttpResponse)
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.openapi import IN_QUERY, Parameter
from drf_yasg.utils import swagger_auto_schema


# 自定义过滤后端 参考 https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html
class SnippetFilterBackend(filters.DjangoFilterBackend):
    """
    自定义过滤后端, 对 get_filterset_kwargs 方法进行重写
    """

    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)
        query_params = kwargs['data']
        queryset = kwargs['queryset']

        if 'language' in query_params:
            language_list = str(query_params['language']).split(',')
            queryset = queryset.filter(language__in=language_list)
            kwargs['queryset'] = queryset

        if 'linenos' in query_params:
            queryset = queryset.filter(linenos__exact=query_params['linenos'])

        if 'title' in query_params:
            queryset = queryset.filter(title__exact=query_params['title'])

        kwargs['queryset'] = queryset
        return kwargs

    # TIP 这个是文档中没有的要覆盖的一个方法,但是可以点击到父类里去看一下这个方法
    #  重写它的原因也很简单：自定义错误类型
    def filter_queryset(self, request, queryset, view):
        filterset = self.get_filterset(request, queryset, view)
        if filterset is None:
            return queryset

        if not filterset.is_valid() and self.raise_exception:
            # 一般这种情况出现在数据表中根本对应的查询的数据
            raise APIException('查询参数无效')
        return filterset.queryset


class SnippetFilter(filters.FilterSet):
    class Meta:
        model = Snippet
        fields = ('linenos', 'title', 'language')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# tip
#  继承自各个mixin类和GenericViewSet，所以默认就提供了增删查改等相关方法，使用起来更加方便
#  使用 ModelViewSet 之后
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # tip 可以重写默认的 list 方法来实现
    # def list


class SnippetViewSet(ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = (SnippetFilterBackend,)
    # 这是使用默认的过滤后端
    # filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SnippetFilter

    #     A viewset that provides default `create()`, `retrieve()`, `update()`,
    #     `partial_update()`, `destroy()` and `list()` actions.
    def get_throttles(self):
        if self.action in ['create', 'update']:
            self.throttle_scope = 'snippet'
        return super().get_throttles()

    # 使用 ModelViewSet 的时候重写 create 方法，比如增加一些参数校验等
    @swagger_auto_schema(
        operation_summary='创建新的代码片段',
        manual_parameters=[
            Parameter('code', IN_QUERY, description='代码内容', required=True, type='string'),
            Parameter('title', IN_QUERY, description='主题', required=False, type='string'),
            Parameter('linenos', IN_QUERY, description='未知信息', required=False, type='boolean'),
            Parameter('language', IN_QUERY, description='语言', required=False, type='string'),
        ],
        responses={status.HTTP_200_OK: openapi.Response('', SnippetSerializer)}
    )
    def create(self, request, *args, **kwargs):
        # 当使用 ModelViewSet 的时候这样使用
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(owner=self.request.user)

        return Response(SnippetSerializer(instance).data)

    # tip 注意使用 ModelViewSet 的这些默认 CURD 方法时，已经不需要自行定义比如 400 404 这样的状态码
    # 重写 retrieve 方法（这里实际上并没有重写，只是继承 ModelViewSet 的方法继续使用）
    # TIP 为每个请求该接口的用户设置 60s 缓存，缓存的内容存到 Cache settings 中设置的 redis 中
    @method_decorator(cache_page(60))
    def retrieve(self, request, *args, **kwargs):
        print(kwargs['pk'])
        snippet = Snippet.objects.filter(pk=kwargs['pk']).first()
        print('====> 获取外键的值', snippet.owner.username, snippet.owner.last_login)
        return super().retrieve(request, *args, **kwargs)

    # update destroy 方法沿用即可
    @swagger_auto_schema(operation_summary='该接口禁用')
    def destroy(self, request, *args, **kwargs):
        # TIP 方法禁用 https://stackoverflow.com/questions/23639113/disable-a-method-in-a-viewset-django-rest-framework
        response = {'message': 'Method "DELETE" not allowed.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


# ---------------------------------------split------------------------------------------------
# tip 删掉 JSONResponse 类重构我们的视图
#   但是这里我们还能看到最裸的一个关于 http 响应的内容
# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#
#     # __init__ 可以认为是类的构造器
#     # **kwargs 关键字参数
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         # tip super 用于调用父类的一个方法，用来解决多继承问题
#         #  super(JSONResponse, self).__init__(content, **kwargs)
#         #  python3 中可以这样使用
#         super().__init__(content, **kwargs)


# @csrf_exempt
@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    列出所有的code snippet，或创建一个新的snippet。
    """
    # 获取列表
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # return JOSNResponse(serializer.data)
        return Response(serializer.data)

    # 新增一个
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = SnippetSerializer(data=data)
        serializer = SnippetSerializer(data=request.data)
        # tip 检测数据类型是否符合要求，这个地方简直非常快捷
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# tip csrf_exempt 一般用来做 post 请求不需要携带 csrf token
#  实际开发中不会用到这种东西
# @csrf_exempt

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    获取，更新或删除一个 code snippet。
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# TIP 虽然使用 ModelViewSet 是如此的方便，但有时我们仍然可以使用 APIView 来编写只用到几个方法的一些视图
class SnippetDetailViewSet(APIView):
    """
    检索，更新或删除一个snippet示例。
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
