from django.db import models
from cart.models import CartItem
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    create = models.DateTimeField(null=False, default=timezone.now)
    complete = models.DateTimeField(null=True)
    status = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f'{self.user.name} / {self.amount} :: {self.create}'


class Purchase(models.Model):
    item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
