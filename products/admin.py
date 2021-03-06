""" Admin for 'products' app"""
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'author',
        'category',
        'image'
        )

    ordering = ('sku', 'author', 'name', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

