from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False,unique=True)
    price = models.FloatField(null=False,blank=False)
    isFree = models.BooleanField(default=False)
    isPremium = models.BooleanField(default=False)
    minimumPlayableAge = models.IntegerField(blank=True,null=True)
    company = models.CharField(max_length=60,blank=False,null=False)
    description = models.TextField(null=True,blank=True)
    rating = models.FloatField(null=True,blank=True)
    downloads=models.FloatField(null=True,blank=True)
    memory = models.FloatField(null=False,blank=False)
    image = models.ImageField(null=True,blank=True)
    introductionVideo = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name
    
class Discount(models.Model):
    percentage = models.FloatField(null=False,blank=False)
    gameId = models.OneToOneField(Game,on_delete=models.CASCADE)
    expireDate = models.DateField(null=False,blank=False)
    def __str__(self):
        return self.percentage

