from django import forms
from .models import CartItem
from account.models import products

class AddCart(forms.ModelForm):
    class Meta:
        model=CartItem
        fields=["quantity"]

class OrderForm(forms.ModelForm):
    class Meta:
        model=products
        fields=["price"]
