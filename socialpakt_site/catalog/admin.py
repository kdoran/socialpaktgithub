from django.contrib import admin
from .models import *


class PhotoAdminInline(admin.StackedInline):
    model = ProductPhoto
    extra = 3

class VariationAdminInline(admin.StackedInline):
    model = ProductVariation
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'active','date_expires','price')
    inlines = (PhotoAdminInline,VariationAdminInline)

admin.site.register(Product, ProductAdmin)
