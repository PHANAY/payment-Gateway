from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    USER_TYPE=(('business', 'business account'),('personal','Personal account'))
    name= models.CharField(max_length=100)
    email=models.EmailField(max_length=256)
    userid = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    password= models.CharField(max_length=256)
    city=models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    account_type= models.CharField(max_length=100,choices=USER_TYPE)
    created= models.DateTimeField(auto_now_add=True)
