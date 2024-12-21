from django.contrib import admin
from apps.orders.models import OrderItem, Cart, Shipping

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Shipping)
