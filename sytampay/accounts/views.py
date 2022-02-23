from audioop import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponse
from .models import *
from .forms import Registerform, Loginform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



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
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(username=username,password=password)
         
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
    return render(request,'accounts/login.html')    



def registerPage(request):
    form=Registerform()
    if request.method == 'POST':
        form=Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('invalid form')


    context={'form':form}
    return render (request,'accounts/register.html',context)


def logoutuser(request):
    logout(request)
    return redirect('login')


def dashboard_view(request):
    
    return render(request,'accounts/dashboard.html')

def profile(request):
    #transactions=
    #profile_detail=
    return render (request,'accounts/profile.html')


