from cgitb import html
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns= [
    path('',views.home_view,name='home'),
    #path('login/',views.loginPage, name= 'login'),
    path('login/',auth_views.LoginView.as_view(),name= 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.registerPage,name='register'),
    path('profile/',views.profile,name='profile'),
    path('',views.dashboard,name= 'dashboard')
]