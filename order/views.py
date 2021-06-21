from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsUserOrReadOmly
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class OrderView(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'
    # permission_classes = (IsUserOrReadOmly, IsAuthenticated)

    def get_total_price(self):
        return sum(self.quantity * self.product.price)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response('success', status=status.HTTP_201_CREATED)