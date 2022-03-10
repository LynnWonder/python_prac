# Create your views here.
# 创建基于类的视图,基于类的视图来编写我们的 API 视图，而不是基于函数的视图，
# 基于类的视图会允许我们重用常用功能
from rest_framework import permissions
# tip REST框架还引入了一个Response对象，这是一种获取未渲染（unrendered）内容的TemplateResponse类型，并使用内容协商来确定返回给客户端的正确内容类型
from rest_framework.response import Response
from rest_framework.views import APIView
# 新使用的 ModelViewSet 类
from rest_framework.viewsets import ModelViewSet

from apps.snippets.models import Snippet
from django.contrib.auth.models import User
from apps.snippets.serializers import (SnippetSerializer, UserSerializer)
from apps.snippets.permissions import IsOwnerOrReadOnly

# 使用基于函数的视图需要的依赖
from django.http import (Http404, HttpResponse)
from rest_framework import status
from rest_framework.decorators import api_view


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

    # 使用 ModelViewSet 的时候重写 create 方法，比如增加一些参数校验等
    def create(self, request, *args, **kwargs):
        # 当使用 ModelViewSet 的时候这样使用
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(owner=self.request.user)

        return Response(SnippetSerializer(instance).data)

    # tip 注意使用 ModelViewSet 的这些默认 CURD 方法时，已经不需要自行定义比如 400 404 这样的状态码
    # 重写 retrieve 方法（这里实际上并没有重写，只是继承 ModelViewSet 的方法继续使用）
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # update destroy 方法沿用即可

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

    def retrieve(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def update(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
