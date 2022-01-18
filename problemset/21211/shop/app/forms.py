# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/21211/ ###

from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    description = forms.CharField(
        min_length=20,
        error_messages={'min_length': 'Product must have a good description'}
    )
    price = forms.DecimalField(
        max_value=1000, max_digits=10, decimal_places=2,
        error_messages={'max_value': 'Product is too expensive'}
    )

    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock']
