from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns= [
    path('',views.home_view,name='home'),
    #path('login/',views.loginPage, name= 'login'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/Login.html'),name= 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.registerPage,name='register'),
    path('profile/',views.profile,name='profile'),
    path('dashboard/',views.dashboard_view,name= 'dashboard'),

    path('reset_password/',auth_views.PasswordResetView.as_view(),name= 'reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name= 'password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]