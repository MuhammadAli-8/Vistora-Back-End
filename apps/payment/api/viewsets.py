from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.orders.models import Shipping, Cart
from apps.payment.api.serializers import PaymentSerializer
from apps.payment.models import Payment


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    def create(self, request, *args, **kwargs):
        cart  = Cart.objects.get_or_create(user=request.user, ordered=False)[0]
        obj = Payment.objects.get_or_create(user=request.user, payment_status="PENDING")[0]
        obj.amount = cart.total_cost()
        obj.orders.set(cart.items.all())
        obj.save()
        return Response(data=self.get_serializer(obj).data)