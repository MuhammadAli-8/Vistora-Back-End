from rest_framework import viewsets

from apps.orders.api.serializers import OrderItemSerializer, CartSerializer
from apps.orders.models import OrderItem, Cart


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user, ordered=False)

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    allowed_methods = ['get']
    def get_object(self):
        obj = Cart.objects.get_or_create(user=self.request.user, ordered=False)[0]
        order_items = OrderItem.objects.filter(user=self.request.user, ordered=False)
        obj.items.set(order_items)
        obj.save()
        return obj
    def list(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)