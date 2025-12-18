from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id':'Product ID',
            'name':'Name',
            'sku':'SKU',
            'price':'Price',
            'quantity':'Quantity',
            'supplier':'Supplier',
        }
        widgets = {
            'product_id':forms.NumberInput(
                attrs={'placeholder':'e.g 1' , 'class':'form-control'}
            ),
            'name':forms.TextInput(
                attrs={'placeholder':'e.g shirt' , 'class':'form-control'}
            ),
            'sku':forms.TextInput(
                attrs={'placeholder':'e.g S12345' , 'class':'form-control'}
            ),
            'price':forms.NumberInput(
                attrs={'placeholder':'e.g 19.99' , 'class':'form-control'}
            ),
            'quantity':forms.NumberInput(
                attrs={'placeholder':'e.g 10' , 'class':'form-control'}
            ),
            'supplier':forms.TextInput(
                attrs={'placeholder':'e.g ABC corp' , 'class':'form-control'}
            ),
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "password"]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'address']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }