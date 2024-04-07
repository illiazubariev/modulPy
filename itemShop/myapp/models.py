from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    

class Return(models.Model):
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)