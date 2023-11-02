from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserUpdateSerializer
import logging
from drf_yasg.utils import swagger_auto_schema
from .models import Profile
from drf_yasg import openapi
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from constants import *

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
                return ReturnResponse.CreateSuccess()
            else:
                errors = serializer.error_messages
                return ReturnResponse.CreateFail(errors)   
        except Exception as e:
            return ExceptionHandler.handle_internal_server_error(e,"UserView POST")
   
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
    def put(self,request,pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserUpdateSerializer(user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ReturnResponse.UpdateSuccess()
            else:
                errors = serializer.error_messages
                return ReturnResponse.UpdateFail(errors)
        except user.DoesNotExist as e:
            return ExceptionHandler.handle_userNotFound()
        except Exception as e:
            logging.error("Exception occured in UserView PUT",e)
            return ExceptionHandler.handle_internal_server_error(e,"UserView UPDATE")
      

    def get(self,request,pk=None):
        if pk == None:
            try:
                users = User.objects.all()
                serializer = UserSerializer(users,many=True)
                return ReturnResponse.GetSuccess(serializer.data)
            except Exception as e:
                logging.error("Exception occured in UserView GET ALL",e)
                return ExceptionHandler.handle_internal_server_error(e,"UserView GET")
        else:
            try:
                users = User.objects.get(id=pk)
                serializer = UserSerializer(users,many=False)
                return ReturnResponse.GetSuccess(serializer.data)
            except Exception as e:
                logging.error("Exception occured in UserView GETBYID",e)
                return ExceptionHandler.handle_internal_server_error(e,"UserView GET")
                
    def delete(self,rquest,pk=None):
        if pk == None:
            try:
                users = User.objects.all()
                users.delete()
                return ReturnResponse.DeleteSuccess()
            except IntegrityError as e:
                return ExceptionHandler.handle_internal_server_error(e,"UserView DELETE")
        else:
            try:
                user = User.objects.get(id = pk)
                user.delete()
                return ReturnResponse.DeleteSuccess()
            except ObjectDoesNotExist:
                return ExceptionHandler.handle_userNotFound()
            
            except Exception as e:
                return ExceptionHandler.handle_internal_server_error(e,"UserView DELETE")
            

class PurchaseCoins(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties={
                'coins':openapi.Schema(type=openapi.TYPE_INTEGER)
            },
            required=['coins'],
        ),
        
        responses={
            status.HTTP_200_OK:"Success",
            status.HTTP_400_BAD_REQUEST:"Bad request",
            status.HTTP_500_INTERNAL_SERVER_ERROR:"Server error",
        }        
    )
    
    def post(self,request,pk):
        try:
            user = User.objects.get(id = pk)
            profile_instance = Profile.objects.get(user=user)
            data = request.data
            profile_instance.coins += int(data['coins'])
            profile_instance.save()
            return ReturnResponse.CreateSuccess()
        
        except ObjectDoesNotExist:
            return ExceptionHandler.handle_userNotFound()
        
        except Exception as e:
            return ExceptionHandler.handle_internal_server_error(e,"PurchaseCoins POST")
            

            