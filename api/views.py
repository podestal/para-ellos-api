from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class CustomerViewSet(ModelViewSet):

    queryset = models.Customer.objects.select_related('user')
    serializer_class = serializers.GetCustomerSerializer

class CategoryViewSet(ModelViewSet):

    queryset = models.Category.objects.all()
    serializer_class = serializers.GetCategorySerializer

class ProductViewSet(ModelViewSet):

    queryset = models.Product.objects.all()
    serializer_class = serializers.GetProductSerializer

class OrderViewSet(ModelViewSet):

    queryset = models.Order.objects.select_related('customer')
    serializer_class = serializers.GetOrderSerializer

class OrderItemSerializer(ModelViewSet):

    queryset = models.OrderItem.objects.select_related('order', 'product')
    serializer_class = serializers.GetOrderItemSerializer

class CartViewSet(ModelViewSet):

    queryset = models.Cart.objects.all()
    serializer_class = serializers.GetCartSerializer

class CartItemViewSet(ModelViewSet):

    queryset = models.CartItem.objects.select_related('product')
    serializer_class = serializers.GetCartItemSerializer




