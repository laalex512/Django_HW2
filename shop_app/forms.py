import datetime
from .models import Product
from django import forms


class ProductEdit(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'price', 'count'
            ]
        exclude = ['added_date']
    added_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type':'date'
            })
        )
    
class ChoiceProduct(forms.Form):
    product = forms.ModelChoiceField(label='Product', queryset=Product.objects.all())