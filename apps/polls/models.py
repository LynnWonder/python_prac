import datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.
# tip 一个模型 model 就是单个定义你的数据的信息源

from django.db import models


# question model 包含问题描述和发布时间
class Question(models.Model):
    # tip 关键字参数 max_length （参考函数参数中的 **kwargs）
    # TIP 注意这确实是一个类属性，这个属性虽然归类所有，但是类的所有实例都能访问的到
    #  因为我们访问的时候会首先查找实例的属性，找不到就向上继续寻找类的属性
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 因为实例没有 question_text 属性，会继续向上找类，直到找到类属性
    # tip 这里其实是覆盖 __str__ 函数
    def __str__(self):
        return self.question_text

    # 为了方便管理端显示
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
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