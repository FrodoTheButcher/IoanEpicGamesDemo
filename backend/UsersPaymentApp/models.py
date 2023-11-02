from django.db import models
from Usersapp.models import Profile
from constants import *

class ProfilePayments(Profile):
    class Meta:
        proxy = True
    
    def addMoney(self,amountOfMoney):
        try:
            if self.accountMoney == None:
                self.accountMoney = 0
                
            if amountOfMoney > 0:
                self.accountMoney += float(amountOfMoney)
                return{
                    "success":True
                }
                
        except ValueError as e:
            return {
                "error":e,
                "success":False                
                }
        
        except Exception as e:
            return {
                "error":e,
                "success":False
            }
            
    def removeMoney(self,amountOfMoney):
        amountOfMoney = float(amountOfMoney)
        try:
            if self.accountMoney - amountOfMoney > 0:
                self.accountMoney -= amountOfMoney
                return{
                    "success":True,
                }
            else:
                return{
                    "success":False,
                    "error":"not enough money"
                }
                
        except ValueError as e:
            return {
                "error":e,
                "success":False                
                }
                      
        except Exception as e:
            return{
                "success":False,
                "error":e
            }