from django.shortcuts import render
from rest_framework.decorators import APIView , api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer, CustomGameSerializer
from constants import Data , ErrorMessage
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


@api_view(['GET'])
def getMostRatedGames(request): 
    try:
        games = Game.objects.all().order_by('-rating')[:5]
        games = GameSerializer(games,many=True)
        return Response(Data.ReturnResponse(games.data),status=status.HTTP_200_OK)
    except Exception as e:
        return Response(ErrorMessage.GETBYID_SERVERERROR,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
                return Response(Data.ReturnResponse("game created"),status=status.HTTP_200_OK)
            else:
                serializer_errors = serializer.errors
                return Response(Data.ReturnResponse(serializer_errors),status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(ErrorMessage.POST_REQUEST_SERVER,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self,request,pk=None):
         if pk:
              try:
                game = Game.objects.get(id=pk)
                serializer = CustomGameSerializer(game,many=False)
                return Response(Data.ReturnResponse(serializer.data),status=status.HTTP_200_OK)
              except ObjectDoesNotExist as e:
                return Response(ErrorMessage.GETBYID_NOTFOUND,status=status.HTTP_500_INTERNAL_SERVER_ERROR)                  
              except Exception as e:
                return Response(ErrorMessage.GETBYID_SERVERERROR,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         else:    
            try:
                games = Game.objects.all()
                serializer = CustomGameSerializer(games,many=True)
                return Response(Data.ReturnResponse(serializer.data),status=status.HTTP_200_OK)

            except Exception as e:
                return Response(ErrorMessage.GETBYID_SERVERERROR,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
    def put(self,request,pk):
         try:
            game = Game.objects.get(id=pk)
            serializer = GameSerializer(instance=game,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(Data.ReturnResponse("game updated"),status=status.HTTP_200_OK)
            else:
                 serializer_errors = serializer.errors
                 return Response(Data.ReturnResponse(serializer_errors),status=status.HTTP_400_BAD_REQUEST)
         except Exception as e:
            return Response(ErrorMessage.GETBYID_SERVERERROR,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         

    def delete(self,request,pk):
         try:
            game = Game.objects.get(id=pk)
            game.delete()
            return Response(Data.ReturnResponse("game deleted"),status=status.HTTP_200_OK)
         except ObjectDoesNotExist as e:
            return Response(ErrorMessage.GETBYID_NOTFOUND,status=status.HTTP_400_BAD_REQUEST)
         except Exception as e:
            return Response({"message":"error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
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
        return Response({"data":serializer.data,"pages":pages},status=status.HTTP_200_OK)
    
    except PageNotAnInteger as e:
        return Response({"massage":"page should be an integer"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    except Exception as e:
        return Response({"massage":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        