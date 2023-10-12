from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Product

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}),
        }

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.widget.attrs.update({'placeholder':f'{field_name}'})