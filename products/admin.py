from django.contrib import admin
from .models import Category, Products

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'date_added', 'date_updated')
    search_fields = ('name',)
    list_filter = ('status', 'date_added', 'date_updated')
    readonly_fields = ('date_added', 'date_updated')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('code', 'category_id', 'name', 'price', 'status', 'date_added', 'date_updated')
    search_fields = ('code', 'name', 'category_id__name')
    list_filter = ('category_id', 'status', 'date_added', 'date_updated')
    readonly_fields = ('date_added', 'date_updated')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
