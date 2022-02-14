
from django.forms import ModelForm
from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Registerform(UserCreationForm):
    #password= forms.CharField(label='password', widget= forms.PasswordInput)
    #password2= forms.CharField(label='confirm password', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields=['first_name','username','email','password1','password2'] 

    

class Loginform(forms.Form):
    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)
    
