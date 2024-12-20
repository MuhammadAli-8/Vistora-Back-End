from rest_framework import serializers

from apps.products.models import Product, Review
from core.utils import BaseSaveSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(BaseSaveSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
