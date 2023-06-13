from django.db import models
from django.contrib.auth.models import User
from account.models import CustUser
from account.models import products

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class OrderItem(models.Model):
    Customer=models.ForeignKey(CustUser, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transaction_id=models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
