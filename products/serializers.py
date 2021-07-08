from rest_framework import serializers
from .models import Product, Category, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
         model = Category
         fields = ('id', 'name')


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields =('id', 'image')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'is_instock', 'categories', 'images')


    def update(self, instance, validated_data):
        data = validated_data.copy()
        data.pop('name','description', 'price', 'category','is_instock', 'images', None)
        for attr, value, in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance 


