from rest_framework import serializers

from apps.orders.models import OrderItem, Cart
from apps.products.api.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'total_price']
        read_only_fields = ['total_price',"id"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = ProductSerializer(instance.product).data
        return data


    def save(self):
        """
        Saves service data.
        """
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            self.validated_data["user"] = user
        super().save()
class CartSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_cost']

    def get_total_cost(self, obj):
        return obj.total_cost()