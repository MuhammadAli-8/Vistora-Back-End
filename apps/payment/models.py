from django.db import models

# Create your models here.
from django.db import models

from apps.orders.models import OrderItem


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    ]

    orders = models.ManyToManyField(OrderItem, related_name='payments')
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    user= models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='payments', null=True)

    def __str__(self):
        return f"Payment #{self.id} - Status: {self.payment_status}"

    def save(self, *args, **kwargs):
        if self.payment_status == "Completed":
            orders=self.orders.all()
            orders.update(ordered=True)
            orders[0].carts.all().update(ordered=True)
        super().save(*args, **kwargs)

