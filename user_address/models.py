from django.db import models
from user.models import User


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address1 = models.CharField('Address Line 1', max_length=100)
    address2 = models.CharField('Address Line 2', max_length=100, blank=True)
    zip_code = models.CharField('ZIP or POSTAL Code', max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return ", ".join(
            [
                self.name, self.address1, self.address2, self.zip_code,
                self.city, self.state, self.country
            ]
        )
