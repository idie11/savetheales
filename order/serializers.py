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
    product = OrdersProductsSerializer(read_only=True)
    class Meta:
        model = OrderProduct
        fields = ('id', 'quantity', 'product')



class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(read_only=True,max_digits=10, decimal_places=2)
    product = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'order_date', 'address', 'total_price', 'product', 'status')

    def create(self, validated_data):
        user = self.context.get('request').user
        customer = User.objects.get(user=user)
        order = Order.objects.create(customer=customer, **validated_data)
        product = self.context.get('request').data.get('product')
        for i in product:
            OrderProduct.objects.create(product_id=i.get('product'), quantity=i.get('quantity'), order=order)
        return order