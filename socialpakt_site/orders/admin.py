from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)