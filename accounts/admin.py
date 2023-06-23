from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Customer)

class useradmin(admin.ModelAdmin):
    list_display = ['email','user_type']

admin.site.register(User,useradmin)
