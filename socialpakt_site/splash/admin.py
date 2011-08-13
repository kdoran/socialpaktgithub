from django.contrib import admin
from .models import *

class SignupAdmin(admin.ModelAdmin):
    list_display = ('email', )
    
admin.site.register(Signup, SignupAdmin)