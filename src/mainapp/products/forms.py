from django.forms import ModelForm
from .models import Product #when dealing with classes, use capitals

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__' #grab all fields from our Product and pass them into this form