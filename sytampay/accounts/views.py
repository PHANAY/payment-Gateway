from audioop import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import *
from .forms import Registerform, Loginform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def payment_view(request):
    return render(request,'accounts/payments.html')

#@login_required
#def dashboard(request):
 #return render(request,
 #'account/dashboard.html',
 #{'section': 'dashboard'})

def loginPage(request):

    if request.method == 'POST':
        form= Loginform(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            user= authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    
                    return redirect('dashboard')
                else:
                    return HttpResponse('disabled account')
            else:
                return HttpResponse('invalid login')
    else:
        form= Loginform()
    return render(request,'accounts/login.html', {'form':form})    



def registerPage(request):
    form=Registerform
    if request.method == 'POST':
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()


    context={'form':form}
    return render (request,'accounts/register.html',context)
def dashboard_view(request,pk):
    owner= Profile.objects.get(id=pk)
    account_details= User_account.objects.get(id=pk)

    context={'owner':owner,'account_details':account_details}
    return render(request,'accounts/dashboard.html',context)

def profile(request):
    #transactions=
    #profile_detail=
    return render (request,'accounts/profile.html')


