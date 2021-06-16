from products.models import Category, Product, ProductImage
from django.contrib import admin

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)