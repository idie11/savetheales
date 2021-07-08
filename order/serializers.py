from users.models import User
from products.models import Product
from rest_framework import serializers
from .models import Order
from .models import OrderProduct



class OrdersProductsSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Product
        fields = ('id', 'name', 'description','price')


class OrderProductSerializer(serializers.ModelSerializer):
    #product = OrdersProductsSerializer()


    class Meta:
        model = OrderProduct
        fields = ('id', 'quantity', 'product', 'order')

    def create(self, validated_data):
        order_product = OrderProduct.objects.create(**validated_data)
        order = validated_data.get('order')
        order.save()
        return order_product


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(read_only=True,max_digits=10, decimal_places=2)
    order_product = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'order_date', 'address', 'total_price', 'order_product')

    def create(self, validated_data):
        user = self.context.get('request').user
        customer = user if user else None
        if not customer.is_anonymous:
            order = Order.objects.create(customer=customer, **validated_data)
        else:
            order = Order.objects.create(**validated_data)
        return order


    