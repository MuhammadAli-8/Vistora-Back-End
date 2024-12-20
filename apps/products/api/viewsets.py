from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ProductSerializer, ReviewSerializer
from ..models import Product, Review


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting Products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name']
    ordering_fields = ['id', 'price']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "stock_quantity": ["gt"],"price": ["gte","lte"]
    }
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["product"]
    permission_classes = [IsAuthenticatedOrReadOnly]
