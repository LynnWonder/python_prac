from django.db import models

# Create your models here.

# 创建 snippets 的 model 文件

# 一些常量定义
LANGUAGE_ALL_CHOICES = ['python', 'golang', 'javascript']
LANGUAGE_CHOICES = [(item, item) for item in LANGUAGE_ALL_CHOICES]


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    # ques 这难道是一个索引吗？
    class Meta:
        ordering = ['created']
