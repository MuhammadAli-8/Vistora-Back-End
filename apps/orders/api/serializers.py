from rest_framework import serializers

from apps.orders.models import OrderItem, Cart, Shipping
from apps.products.api.serializers import ProductSerializer
from core.utils import BaseSaveSerializer


class OrderItemSerializer(BaseSaveSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'total_price']
        read_only_fields = ['total_price',"id"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = ProductSerializer(instance.product).data
        return data



class CartSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_cost']

    def get_total_cost(self, obj):
        return obj.total_cost()


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'
