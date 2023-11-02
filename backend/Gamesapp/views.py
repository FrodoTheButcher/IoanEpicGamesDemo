from django.shortcuts import render
from rest_framework.decorators import APIView , api_view
from rest_framework import status
from .models import Game
from .serializers import GameSerializer, CustomGameSerializer
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from constants import *

@api_view(['GET'])
def getMostRatedGames(request): 
    try:
        games = Game.objects.all().order_by('-rating')[:5]
        games = GameSerializer(games,many=True)
        return ReturnResponse.GetSuccess()
    
    except Exception as e:
        return ExceptionHandler.handle_internal_server_error(e,"getMostRatedGames GET")


class GameView(APIView):
    @swagger_auto_schema(
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'name':openapi.Schema(type=openapi.TYPE_STRING),
                    'age':openapi.Schema(type=openapi.TYPE_INTEGER),
                    'price':openapi.Schema(type=openapi.TYPE_NUMBER),
                    'company':openapi.Schema(type=openapi.TYPE_STRING),
                    'description':openapi.Schema(type=openapi.TYPE_STRING),
                    'memory':openapi.Schema(type=openapi.TYPE_NUMBER),
                    'multiplayer':openapi.Schema(type=openapi.TYPE_BOOLEAN),

                },
            ),
            responses={
                status.HTTP_200_OK:'Success',
                status.HTTP_400_BAD_REQUEST:'Bad data',
                status.HTTP_500_INTERNAL_SERVER_ERROR:'Server error',
            }
    )
    def post(self,request):
        try:
            serializer = GameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ReturnResponse.CreateSuccess()
            else:
                serializer_errors = serializer.errors
                return ReturnResponse.CreateFail(serializer_errors)
        except Exception as e:
            return ExceptionHandler.handle_internal_server_error(e,"GameView POST")
        
    def get(self,request,pk=None):
         if pk:
              try:
                game = Game.objects.get(id=pk)
                serializer = CustomGameSerializer(game,many=False)
                return ReturnResponse.GetSuccess()
              except ObjectDoesNotExist as e:
                return ExceptionHandler.handle_gameNotFound()
              except Exception as e:
                return ExceptionHandler.handle_internal_server_error(e,"GameView GET")
         else:    
            try:
                games = Game.objects.all()
                serializer = CustomGameSerializer(games,many=True)
                return ReturnResponse.GetSuccess()

            except Exception as e:
                return ExceptionHandler.handle_internal_server_error(e,"GameView GET")
         
    def put(self,request,pk):
         try:
            game = Game.objects.get(id=pk)
            serializer = GameSerializer(instance=game,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ReturnResponse.UpdateSuccess()
            else:
                 serializer_errors = serializer.errors
                 return ReturnResponse.UpdateFail(serializer_errors)
         except Exception as e:
            return ExceptionHandler.handle_internal_server_error(e,"GameView UPDATE")
         

    def delete(self,request,pk):
         try:
            game = Game.objects.get(id=pk)
            game.delete()
            return ReturnResponse.DeleteSuccess()
         except ObjectDoesNotExist as e:
            return ExceptionHandler.handle_gameNotFound()
         except Exception as e:
            return ExceptionHandler.handle_internal_server_error(e,"GameView DELETE")

    
@api_view(['GET'])
def paginateGames(request):
    try:
        query = request.query_params.get("keyword")
        page = request.query_params.get("page")
        print("query",query)
        if page[-1] == '/':
            page = page[0]
            
        print("page",page)    
        if query == None:
            query = ""       
        if page == None:
            page = 1
            
        games = Game.objects.filter(name__contains = query).order_by("-downloads")      
        paginator = Paginator(games,4)  
        pages = paginator.num_pages  
        products = paginator.page(int(page))    
        serializer = GameSerializer(products,many = True)    
        return ReturnResponse.GetSuccess()
    
    except PageNotAnInteger as e:
        return ExceptionHandler.handle_pageNotAnInteger()
    
    except Exception as e:
        return ExceptionHandler.handle_internal_server_error(e,"paginateGames GET")
        