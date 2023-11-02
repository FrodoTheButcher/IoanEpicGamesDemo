from django.db import models

class Price(models.Model):
    money = models.FloatField(default = 0,blank=False,null=False)
    bonus = models.FloatField(default = 0,blank=False,null=False)
    expireDate = models.DateTimeField(blank=False,null=False)

    def __str__(self):
        return str(self.money)