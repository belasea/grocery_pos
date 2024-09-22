from django.contrib import admin
from .models import Category, Products, Sales, salesItems


# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)

