from django.contrib import admin
from .models import Book
from .models import CustomUser

class CustomAdminModel(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year')

# Register your models here.
admin.site.register(Book)
admin.site.register(CustomUser, CustomAdminModel)



