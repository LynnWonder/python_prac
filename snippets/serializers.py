from rest_framework import serializers
# tip 从 models 中引入这几个变量
from snippets.models import Snippet, LANGUAGE_CHOICES


# class SnippetSerializer(serializers.Serializer):
class SnippetSerializer(serializers.ModelSerializer):
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
    # tip
    #  使用 ModelSerializer 类，是创建序列化类的快捷方式
    #  一组自动确定的字段
    #  默认简单实现的 create() 和 update() 方法
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language')
