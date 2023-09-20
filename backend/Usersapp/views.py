from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from constants import *
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserUpdateSerializer
import logging
from drf_yasg.utils import swagger_auto_schema
from .models import Profile
from drf_yasg import openapi


logger = logging.getLogger(__name__)
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['id'] = user.id
        token['is_superuser'] = user.is_superuser

        return token
            
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    


class UserView(APIView):
    @swagger_auto_schema(
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'username':openapi.Schema(type=openapi.TYPE_STRING),
                    'email':openapi.Schema(type=openapi.TYPE_STRING),
                    'password':openapi.Schema(type=openapi.TYPE_STRING),
                    'password2':openapi.Schema(type=openapi.TYPE_STRING),
                },
                required=['username','email','password','password2'],
            ),
            responses={
                status.HTTP_200_OK:'Success',
                status.HTTP_400_BAD_REQUEST:'Bad data',
                status.HTTP_500_INTERNAL_SERVER_ERROR:'Server error',
            }
    )
   
    def post(self,request):
        try:
            data = request.data
            dataForSerializer = {
                "email":data['email'],
                "username":data['username'],
                "password":data['password']
            }
            context = {
                "password2":data['password2']
            }
            serializer = UserSerializer(data=dataForSerializer,context=context)
            
            if serializer.is_valid():
                serializer.save()
                return Response(Data.ReturnResponse("Create success"),status=status.HTTP_200_OK)
            else:
                errors = serializer.error_messages
                return Response(Data.ReturnResponse(errors),status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error("Exception occured in UserView POST",e)
            return Response(ErrorMessage.POST_REQUEST_SERVER,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self,request,pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserUpdateSerializer(user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(Data.ReturnResponse("Update success"),status=status.HTTP_200_OK)
            else:
                errors = serializer.error_messages
                return Response(Data.ReturnResponse(errors),status=status.HTTP_400_BAD_REQUEST)
        except user.DoesNotExist as e:
            return Response(ErrorMessage.GETBYID_NOTFOUND,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error("Exception occured in UserView PUT",e)
            return Response(ErrorMessage.POST_REQUEST_SERVER,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
            
    def get(self,request,pk=None):
        if pk == None:
            try:
                users = User.objects.all()
                serializer = UserSerializer(users,many=True)
                return Response(Data.ReturnResponse(serializer.data),status=status.HTTP_200_OK)
            except Exception as e:
                logging.error("Exception occured in UserView GET ALL",e)
                return Response(ErrorMessage.POST_REQUEST_SERVER,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            try:
                users = User.objects.get(id=pk)
                serializer = UserSerializer(users,many=False)
                return Response(Data.ReturnResponse(serializer.data),status=status.HTTP_200_OK)
            except Exception as e:
                logging.error("Exception occured in UserView GETBYID",e)
                return Response(ErrorMessage.POST_REQUEST_SERVER,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                