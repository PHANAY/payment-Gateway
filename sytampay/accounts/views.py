from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import Users
from .forms import Registerform, Loginform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def payment_view(request):
    return render(request,'accounts/payments.html')

@login_required
def dashboard(request):
 return render(request,
 'account/dashboard.html',
 {'section': 'dashboard'})

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
    if request.method =='POST':
        user_form= Registerform(request.POST)
        if user_form.is_valid:
            new_user= user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'accounts/register_done.html',{'new_user':new_user})
    else:
        user_form= Registerform()
        return render(request,'accounts/register.html',{'user_form':user_form})

def dashboard_view(request):
    return render(request,'accounts/dashboard.html')

def profile(request):
    #transactions=
    #profile_detail=
    return render (request,'accounts/profile.html')


