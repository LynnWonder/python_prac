from django.contrib.auth.models import User
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

# tip 从 models 中引入这几个变量
from apps.snippets.models import Snippet

from .exceptions import SnippetNotExistException


# tip 主要对 model 对象进行序列化，
class SnippetSerializer(serializers.ModelSerializer):
    # tip 下面的代码暂不删除
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.save()
    #     return instance

    # -------------------------------正文分隔线-----------------------------
    # tip
    #  使用 ModelSerializer 类，是创建序列化类的快捷方式
    #  一组自动确定的字段
    #  默认简单实现的 create() 和 update() 方法
    # 这里标识 username 只能是可读的，只能用于序列化表示，不能用于反序列化更新模型实例
    # 通过 source 来指定需要关联的外键对象的值
    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.SerializerMethodField(label="own 信息")

    class Meta:
        # TIP 指定需要序列化的 model
        model = Snippet
        # TIP 需要序列化的字段，是一个元组，`__all__` 表示所有字段
        fields = ('id', 'title', 'code', 'linenos', 'language', 'owner')

    @swagger_serializer_method(serializer_or_field=serializers.JSONField)
    def get_owner(self, obj):
        # TIP 这是查询外键值的一种方式即直接 filter 出来值之后取对象中的值
        user = User.objects.filter(pk=obj.owner_id).first()
        return {"user_name": user.username, "user_id": user.id}


class SnippetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        # TIP 需要序列化的字段，是一个元组，`__all__` 表示所有字段
        fields = ('id', 'title', 'code', 'linenos', 'language', 'owner')

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class TestSerializer(serializers.Serializer):
    """
    测试自定义接口名称
    """
    test_id = serializers.CharField(
        label='测试 id'
    )

    # TIP 字段级别的 validation
    def validate_test_id(self, test_id):
        try:
            Snippet.objects.get(id__exact=test_id)
        except Snippet.DoesNotExist:
            raise SnippetNotExistException


# 在 api 中添加这些用户的标识，接下来就是创建一个新的关于 user 的序列化器
class UserSerializer(serializers.ModelSerializer):
    # 因为 snippets 在用户模型中是一个反向关联的关系，
    # 在使用 ModelSerializer 类的时候它默认不会被包含
    # 因此我们需要为它添加一个显式字段
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
