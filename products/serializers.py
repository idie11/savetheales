from rest_framework import serializers
from .models import Product, Category, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
         model = Category
         fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImage

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'is_instock', 'categories', 'images')


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields =('id', 'image')