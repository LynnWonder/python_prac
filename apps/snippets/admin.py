from django.contrib import admin
from django.contrib.auth.models import User

from .models import Snippet


class SnippetInline(admin.TabularInline):
    model = Snippet
    extra = 1


class UserInline(admin.TabularInline):
    model = User


class UserAdmin(admin.ModelAdmin):
    # TIP admin 中处理主键和外键的关系可以用内嵌来解决，不过是在主键所在表这边 inline
    # User 表的主键又是  snippets 的外键，所以是在 User 表这里内嵌 Snippet
    inlines = [SnippetInline]
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_superuser')


# Re-register UserAdmin
# 去掉在 admin 中的注册
admin.site.unregister(User)
# 用 UserAdmin 注册 user
admin.site.register(User, UserAdmin)


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    # 将表单分为几个字段集
    fieldsets = [
        (None, {'fields': ['title', 'code', 'linenos', 'language']}),
    ]
