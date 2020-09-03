from django.db import models
from user.models import User


# Create your models here.
class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)

class Product(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ActiveManager()

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price

    def is_active(self):
        return self.active

    def in_stock(self):
        return self.available

    def get_vendor(self):
        return self.vendor
