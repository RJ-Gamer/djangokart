from django.db import models
from user.models import User
from product.models import Product
import logging

logger = logging.getLogger(__name__)

# Create your models here.
class Order(models.Model):
    NEW = 10
    PAID = 20
    DONE = 30
    STATUSES = (
        (NEW, 'New'),
        (PAID, 'Paid'),
        (DONE, 'Done'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=NEW, choices=STATUSES)
    billing_name = models.CharField(max_length=100)
    billing_address1 = models.CharField(max_length=100)
    billing_address2 = models.CharField(max_length=100, blank=True)
    billing_zip_code = models.CharField(max_length=12)
    billing_city = models.CharField(max_length=100)
    billing_state = models.CharField(max_length=100)
    billing_country = models.CharField(max_length=100)
    shipping_name = models.CharField(max_length=100)
    shipping_address1 = models.CharField(max_length=100)
    shipping_address2 = models.CharField(max_length=100, blank=True)
    shipping_zip_code = models.CharField(max_length=12)
    shipping_city = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_country = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class OrderLine(models.Model):
    NEW = 10
    PROCESSING = 20
    SENT = 30
    CANCELLED = 40
    STATUSES = (
        (NEW, 'New Order'),
        (SENT, 'Order Sent'),
        (PROCESSING, 'Order Processing'),
        (CANCELLED, 'Order Cancelled'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUSES, default=NEW)
