from django.db import models
from uuid import uuid4
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    date_of_birth= models.DateField()
    photo= models.ImageField()




class Users(models.Model):
    user_id= models.UUIDField(primary_key=True,default= uuid4,editable=False)
    first_name= models.CharField(max_length=100)
    second_name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    phone_number= models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    password= models.CharField(max_length=256,default=123)



class Wallet(models.Model):
    wallet_id= models.UUIDField(primary_key=True,default=uuid4,editable=False)
    user_id= models.ForeignKey(Users,on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)

    
class User_account(models.Model):
    account_type= (('personal','Personal'),
    ('merchant','Merchant'))
    user_id= models.ForeignKey(Users,on_delete=models.PROTECT)
    user_type= models.CharField(max_length=30,choices=account_type)
    created= models.DateTimeField(auto_now_add=True)
    balance= models.IntegerField(default=0)

class Topup (models.Model):
    transaction_id= models.UUIDField(default=uuid4,editable=False)
    reference_id= models.UUIDField(primary_key=True,default=uuid4,editable=False)
    date=models.DateTimeField(auto_now_add=True)
    amount= models.IntegerField()
    wallet_id= models.ForeignKey(Wallet,on_delete=models.PROTECT)

class Payments(models.Model):
    transaction_id= models.UUIDField(default=uuid4,editable=False)
    reference_id= models.UUIDField(default=uuid4,editable=False)
    date=models.DateTimeField(auto_now_add=True)
    #credited_wallet=
    #debited_wallet=