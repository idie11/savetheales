from order.models import Order, OrderProduct
from order.serializers import OrderSerializer, OrderProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from .permissions import IsUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, F


class OrderProductView(ModelViewSet):
    serializer_class = OrderProductSerializer
    queryset = OrderProduct
    lookup_field = 'pk'
    permission_classes = (IsUserOrReadOnly, )




class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.prefetch_related('product_order').order_by('-id')
    lookup_field = 'pk'
    permission_classes = (IsUserOrReadOnly, )



    # def get_total_price(self):
    #     return sum(self.quantity * self.product.price)

    
    # @classmethod
    # def get_total_price(self):
    #     return Order.objects.aggregate(total_price=Sum(F('drink__price') * F('quantity'),
    #         output_field=models.DecimalField(decimal_places=2)))['total']
    
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response('success', status=status.HTTP_201_CREATED)