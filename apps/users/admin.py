from django import views
from django.contrib import admin

# Register your models here.


from .models import VerifyCode, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["username", "password"]


class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile', "add_time"]


admin.site.register(VerifyCode, VerifyCodeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
