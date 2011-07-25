from django.contrib import admin
from .models import *


class LinkAdminInline(admin.StackedInline):
    model = PartnerLink
    extra = 3

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name',)
    inlines = (LinkAdminInline,)

admin.site.register(Partner, PartnerAdmin)