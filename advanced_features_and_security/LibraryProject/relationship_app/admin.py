from django.contrib import admin
from .models import CustomUser

class CustomAdminModel(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name')

# Register your models here.
admin.site.register(CustomUser, CustomAdminModel)

