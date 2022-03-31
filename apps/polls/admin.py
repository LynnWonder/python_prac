from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# register 装饰器用于注册一个 ModelAdmin 类
# https://docs.djangoproject.com/zh-hans/4.0/ref/contrib/admin/
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # 将表单分为几个字段集
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date']
        })
    ]
    # 这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。
    # 默认提供 3 个足够的选项字段。”
    inlines = [ChoiceInline]
    # 使用 list_display 后台选项，它是一个包含要显示的字段名的元组，
    # 在更改列表页中以列的形式展示这个对象
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 管理端展示的过滤器类型
    list_filter = ['pub_date']
    # 后台使用
    search_fields = ['question_text']
