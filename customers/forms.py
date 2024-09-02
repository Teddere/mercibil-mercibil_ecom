from django import forms
from users.models import Shopper
from customers.models import Customer

User = Shopper

class CustomerCreateForm(forms.ModelForm):
    phone = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username','email','password','phone']

class CustomerUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True,max_length=200)
    username = forms.CharField(required=True,max_length=100)
    class Meta:
        model = Customer
        fields = ['username','email','phone']
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)

        if self.user:
            self.fields['email'].initial = self.user.email
            self.fields['username'].initial = self.user.username

    def save(self, commit=True):
        if self.user:
            self.user.email = self.cleaned_data['email']
            self.user.username = self.cleaned_data['username']
            self.user.save()
        customer = super(CustomerUpdateForm, self).save(commit=False)
        customer.user = self.user
        if commit:
            customer.save()
        return customer




