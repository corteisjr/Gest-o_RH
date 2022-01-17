from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.empresas.models import Empresa


class NewCustomerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = [User, Empresa]
        fields = ('username', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(NewCustomerForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


