from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from webapp.models import Userinfo, Post


class UserinfoInline(admin.StackedInline):
    model = Userinfo


class UserinfoAdmin(UserAdmin):
    inlines = [UserinfoInline]


admin.site.unregister(User)
admin.site.register(User, UserinfoAdmin)
admin.site.register(Post)