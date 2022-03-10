from django.contrib import admin
from .models import Snippet
from django.contrib.auth.models import User


class SnippetInline(admin.TabularInline):
    model = Snippet


class UserAdmin(admin.ModelAdmin):
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
