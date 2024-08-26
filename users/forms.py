from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Shopper




class LoginForm(forms.ModelForm):
    email = forms.EmailField(label='E-mail',max_length=100)
    password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput)

class RegisterShopperUser(UserCreationForm):

    class Meta:
        model = Shopper
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez un nom utilisateur','required':'true'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Entrez votre email','required':'true'}),
        }
        labels = {
            'username': 'Nom utilisateur',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super(RegisterShopperUser, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirmez votre mot de passe'})