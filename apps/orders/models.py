from django.db import models

from apps.products.models import Product


# Create your models here.
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='order_items', null=True)

    def save(self, *args, **kwargs):
        # Automatically calculate the total price based on the product price and quantity
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Cart(models.Model):
    items = models.ManyToManyField(OrderItem, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='cart', null=True)


    def __str__(self):
        return f"Cart {self.id} with {self.items.count()} items"

    def total_cost(self):
        return sum(item.total_price for item in self.items.all())
