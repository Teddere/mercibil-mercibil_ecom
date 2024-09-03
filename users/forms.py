from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import Shopper

User = get_user_model()



class LoginFormUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Entrez votre email'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Entrez votre mot de passe'}),
        }
        labels = {
            'email': 'E-mail',
            'password': 'Mot de passe'
        }


class RegisterShopperUser(forms.ModelForm):
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder': 'Confirmez votre mot de passe'}
    ),required=True)
    class Meta:
        model = Shopper
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Entrez un nom utilisateur', 'required': 'true'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Entrez votre email', 'required': 'true'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'}),
        }

