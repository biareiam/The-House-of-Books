from django.contrib import admin
from .models import Product, Category

# This is what is going to be displayed in the admin
admin.site.register(Product)
admin.site.register(Category)

