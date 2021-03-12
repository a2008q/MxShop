# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.


from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ["user", "goods", "nums", ]


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(admin.TabularInline):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(OrderInfo, OrderInfoAdmin)
