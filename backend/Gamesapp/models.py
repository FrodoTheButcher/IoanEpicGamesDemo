from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    def __str__(self):
        return self.name

class GameSale(models.Model):
    percentage = models.FloatField(blank=False,null=False)
    expireDate = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return str(self.percentage)

class Game(models.Model):
    sale = models.ForeignKey(GameSale,on_delete=models.SET_NULL,blank=True,null=True)
    tags = models.ManyToManyField(Tag,blank=True,null=True)
    name = models.CharField(max_length=50,null=False,blank=False,unique=True)
    price = models.FloatField(null=False,blank=False)
    age = models.IntegerField(blank=True,null=True)
    company = models.CharField(max_length=60,blank=False,null=False)
    description = models.TextField(null=True,blank=True)
    rating = models.FloatField(null=True,blank=True)
    downloads=models.FloatField(null=True,blank=True)
    memory = models.FloatField(null=False,blank=False)
    image = models.ImageField(null=True,blank=True)
    introductionVideo = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name
