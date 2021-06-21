from .models import Category, ProductImage, Product
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, ProductImageSerializer, ProductSerializer
from django_filters import rest_framework as filters
from .permissions import IsAdminOrReadOmly


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['categories', 'is_instock', 'price', 'min_price', 'max_price']


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.prefetch_related('images')
    lookup_field = 'pk'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    # permission_classes = (IsAdminOrReadOmly, )


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    

class ProductImageView(ModelViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    lookup_field = 'pk'