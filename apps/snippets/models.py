from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 创建 snippets 的 model 文件

# 一些常量定义
LANGUAGE_ALL_CHOICES = ['python', 'golang', 'javascript']
LANGUAGE_CHOICES = [(item, item) for item in LANGUAGE_ALL_CHOICES]


# Tutorial4 认证与权限设置
# 目前，我们的API对谁可以编辑或删除代码段没有任何限制。我们希望有更高级的行为，以确保：
# 代码片段始终与创建者相关联。
# 只有通过身份验证的用户可以创建片段。
# 只有代码片段的创建者可以更新或删除它。
# 未经身份验证的请求应具有完全只读访问权限。
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # TIP 创建一个外键，注意此处定义 ForeignKey 时设置 related_name 参数重写了这个 snippet_set 名 为 snippets。
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)

    # tip 这是一个元数据选项，以下代码表示获取对象列表时候的默认排序方式
    class Meta:
        pass
        ordering = ['-created']
