from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'transaction_date', 'fulfilled']
    pass

admin.site.register(Order, OrderAdmin)