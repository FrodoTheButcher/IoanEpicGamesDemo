from django.db import models
from django.contrib.auth.models import User
from Gamesapp.models import Game
# Create your models here.
class ProfileGameRelation(models.Model):
    userId = models.OneToOneField(User,on_delete=models.CASCADE)
    gameId = models.OneToOneField(Game,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.userId)
    
class GameReview(models.Model):
    idGame = models.OneToOneField(Game,on_delete=models.CASCADE)
    idUser = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


