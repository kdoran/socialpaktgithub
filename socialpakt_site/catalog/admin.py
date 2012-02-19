from django.contrib import admin
from .models import *


class PhotoAdminInline(admin.StackedInline):
    model = ProductPhoto
    extra = 3

class VariationAdminInline(admin.StackedInline):
    model = ProductVariation
    extra = 8

class ProductAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'category', 'featured', 'active','date_expires','price')
    inlines = (PhotoAdminInline,VariationAdminInline)

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('display_order', 'slug')

class HomeCategoryAdmin(admin.ModelAdmin):
	list_display = ('slug', 'display_text', 'category')

admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(VariationCategory, CategoryAdmin)
admin.site.register(HomeCategory, HomeCategoryAdmin)

class CatalogGlobalsAdmin(admin.ModelAdmin):
	pass

admin.site.register(CatalogGlobals, CatalogGlobalsAdmin)