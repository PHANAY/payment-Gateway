
from django.forms import ModelForm
from .models import Users
from django import forms
from django.contrib.auth.models import User


class Registerform(ModelForm):
    password= forms.CharField(label='password', widget= forms.PasswordInput)
    password2= forms.CharField(label='confirm password', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields=['first_name','email','username'] 

    def clean_password2(self):
        cd= self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords don\'t match')
        return cd['password2']

class Loginform(forms.Form):
    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)
    
