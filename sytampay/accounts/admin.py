from django.contrib import admin
from .models import Profile,Wallet,User_account,Topup,Payments

# Register your models here.
admin.site.register (Profile)
admin.site.register (User_account)
admin.site.register (Topup)
admin.site.register (Payments)
admin.site.register (Wallet)
