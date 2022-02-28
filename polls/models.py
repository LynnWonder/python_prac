import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# TIP 一个模型 model 就是单个定义你的数据的信息源

from django.db import models


# question model 包含问题描述和发布时间
class Question(models.Model):
    # tip 关键字参数 max_length （参考函数参数中的 **kwargs）
    # Ques 这不是一个类属性吗，为什么下面用 self 访问
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 因为实例没有 question_text 属性，会继续向上找类，直到找到类属性
    # tip 这里其实是覆盖 __str__ 函数
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# choice model 两个字段：选项描述和当前得票数
class Choice(models.Model):
    # 定义一个外键，每一个 Choice 对象都关联一个 Question 对象。
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# 之后开启了一系列的 python 交互命令行操作，一切特性需要参照 querySet 文档