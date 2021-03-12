from django.contrib import admin

# Register your models here.


from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message_type', "message", "add_time"]


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ["signer_name", "signer_mobile", "district", "address"]


admin.site.register(UserFav, UserFavAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
