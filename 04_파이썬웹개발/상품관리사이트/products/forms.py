from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'code', 'name', 'price', 'stock', 'description']
