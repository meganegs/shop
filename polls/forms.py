from django import forms
from .models import Products
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class  UserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
class ProductForm(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100)