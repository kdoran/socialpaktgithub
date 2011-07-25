### -*- coding: utf-8 -*- ####################################################

from django.contrib.contenttypes import generic
from django.contrib import admin

from .models import Cart, Item


class ItemAdminInline(generic.GenericTabularInline):
    model = Item
    extra = 1
    ct_field = "content_type"
    ct_fk_field = "object_pk"

class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'creation_date')
    list_filter = ('creation_date',)
    date_hierarchy = 'creation_date'
    readonly_fields = ('creation_date',)
    inlines = (ItemAdminInline,)

admin.site.register(Cart, CartAdmin)
