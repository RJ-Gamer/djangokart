from django.db import models
from django.core.validators import MinValueValidator
from user.models import User
from product.models import Product
from order.models import Order, OrderLine
import logging
# Create your models here.

logger = logging.getLogger(__name__)

class Basket(models.Model):
    OPEN = 1
    SUBMITTED = 2
    STATUSES = (
        (OPEN, 'Open'),
        (SUBMITTED, 'Submitted'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=STATUSES, default=OPEN)

    def is_empty(self):
        return self.basketline_set.all().count() == 0

    def count(self):
        return sum(i.quantity for i in self.basketline_set.all())

    def create_order(self, billing_address, shipping_address):
        if not self.user:
            raise 'Cannot create order without user'
        logger.info(
            'Creating order for basket_id: %d'
            ', Shipping address: %d, billing address: %d',
            self.id, shipping_address.id, billing_address.id
        )
        order_data = {
            'user': self.user,
            'billing_name': billing_address.name,
            'billing_address1': billing_address.address1,
            'billing_address2': billing_address.address2,
            'billing_zip_code': billing_address.zip_code,
            'billing_city': billing_address.city,
            'billing_state': billing_address.state,
            'billing_country': billing_address.country,
            'shipping_name': shipping_address.name,
            'shipping_address1': shipping_address.address1,
            'shipping_address2': shipping_address.address2,
            'shipping_zip_code': shipping_address.zip_code,
            'shipping_city': shipping_address.city,
            'shipping_state': shipping_address.state,
            'shipping_country': shipping_address.country,
        }
        order = Order.objects.create(**order_data)
        c=0
        for line in self.basketline_set.all():
            for item in range(line.quantity):
                order_line_data = {
                    'order': order,
                    'product': line.product,
                }
                orderline = OrderLine.objects.create(
                    **order_line_data
                )
        logger.info(
            'Created order with id: %d and lines count: %d', order.id, c,
        )
        self.status = Basket.SUBMITTED
        self.save()
        return order


class BasketLine(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,
        validators=[MinValueValidator(1)])
