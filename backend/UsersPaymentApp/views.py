from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import ProfilePayments
from constants import *
from django.contrib.auth.models import User
from .requests import AddMoney,RemoveMoney
from drf_yasg.utils import swagger_auto_schema


class BuyCoins(APIView):
    @swagger_auto_schema(
        request_body=AddMoney,
        required='__all__',
                
    ) 
    
    def put(self,request):
        user = User.objects.get(id = 11)
        profile = ProfilePayments.objects.get(user = user)
        data = request.data
        response = profile.addMoney(data['money'])
        if "error" in response:
            return ReturnResponse.UpdateFail("We had a problem. Try again later!")
        profile.save()
        return ReturnResponse.UpdateSuccess()
    
    
class RemoveCoins(APIView):
    @swagger_auto_schema(
        request_body=RemoveMoney,
        reqired = '__all__',
    )
    
    def put(self,request):
        user = User.objects.get(id = 11)
        profile = ProfilePayments.objects.get(user = user)
        data = request.data
        response = profile.removeMoney(data['money'])
        if "error" in response:
            return ReturnResponse.UpdateFail("We had a problem. Try again later!")
        profile.save()
        return ReturnResponse.UpdateSuccess()
    
