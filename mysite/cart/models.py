from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    data = models.DateTimeField(null=False, default=timezone.now)
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.user} / {self.product} :: {self.data}'

