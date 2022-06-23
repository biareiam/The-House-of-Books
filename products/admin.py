from django.contrib import admin
from .models import Product, Category, Review


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

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'comment',
        'created_on',
        'approved',
    )
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

