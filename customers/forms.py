from django import forms
from django.contrib.auth import get_user_model
from customers.models import Customer

User = get_user_model()

class CustomerForm(forms.ModelForm):
    email = forms.EmailField(required=True,max_length=200)
    username = forms.CharField(required=True,max_length=100)

    class Meta:
        model = Customer
        fields = ['username','email','phone']

    def __init__(self, *args, **kwargs):
        # Transmettez l'instance utilisateur dans kwargs si vous devez préremplir le formulaire avec les données utilisateur
        self.user = kwargs.pop('user', None)
        super(CustomerForm, self).__init__(*args, **kwargs)

        if self.user:
            self.fields['email'].initial = self.user.email
            self.fields['username'].initial = self.user.username
    def save(self, commit=True):

        if self.user:
            self.user.email = self.cleaned_data['email']
            self.user.username = self.cleaned_data['username']
            self.user.save()
        customer = super(CustomerForm, self).save(commit=False)
        customer.user = self.user
        if commit:
            customer.save()
        return customer


