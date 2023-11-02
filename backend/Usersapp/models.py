from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,blank=False,null=False,on_delete=models.CASCADE)
    email = models.EmailField(blank=False,null=False,unique=True)
    name = models.CharField(blank=True,null=True,max_length=30)
    numberOfGames = models.IntegerField(blank=True,null=True)
    accountMoney = models.FloatField(blank=True,null=True,default=0)
    isPremium = models.BooleanField(default=False)
    image = models.ImageField(blank=True,null=True)
    
    
    def __str__(self):
        return self.email
