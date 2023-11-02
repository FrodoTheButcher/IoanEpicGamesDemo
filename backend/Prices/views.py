from django.shortcuts import render
from rest_framework.decorators import APIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .serializers import PriceSerializer
from constants import *
from drf_yasg.utils import swagger_auto_schema


class Price(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'money':openapi.Schema(type=openapi.TYPE_NUMBER),
                'bonus':openapi.Schema(type=openapi.TYPE_NUMBER),
                'expireDate':openapi.Schema(type=openapi.FORMAT_DATETIME),
            },
            
            required=['money', 'bonus']
        ),
        
        responses = {
            status.HTTP_200_OK:"Price Posted",
            status.HTTP_400_BAD_REQUEST:"Price unuploaded",
            status.HTTP_500_INTERNAL_SERVER_ERROR:"Server crashed! Please come back later!"
        }
    )
    def post(self,request):
        try:         
            data = request.data
            dataForSerializer = {
                'money':data['money'],
                'bonus':data['bonus'],
                'expireDate':data['expireDate']
            }
            
            serializedData = PriceSerializer(data=dataForSerializer,many = True)
            if serializedData.is_valid():
                serializedData.save()
                return ReturnResponse.CreateSuccess()
            
            else: 
                errors = serializedData.error_messages
                return ReturnResponse.CreateFail(errors)
        
        except Exception as e:
            return ExceptionHandler.handle_internal_server_error(e,"Price POST")
                   