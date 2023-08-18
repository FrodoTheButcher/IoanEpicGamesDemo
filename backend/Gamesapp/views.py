from django.shortcuts import render
from rest_framework.decorators import APIView , api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer, CustomGameSerializer
from constants import Data , ErrorMessage
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


class GameView(APIView):
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
              except Exception as e:
                return Response({"message":"error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         else:    
            try:
                games = Game.objects.all()
                serializer = CustomGameSerializer(games,many=True)
                return Response(Data.ReturnResponse(serializer.data),status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"message":"error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
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
         except ObjectDoesNotExist:
                 return Response(ErrorMessage.GETBYID_NOTFOUND,status=status.HTTP_400_BAD_REQUEST)
         except Exception as e:
            return Response({"message":"error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         

    def delete(self,request,pk):
         try:
            game = Game.objects.get(id=pk)
            game.delete()
            return Response(Data.ReturnResponse("game deleted"),status=status.HTTP_200_OK)
         except ObjectDoesNotExist as e:
            return Response(ErrorMessage.GETBYID_NOTFOUND,status=status.HTTP_400_BAD_REQUEST)
         except Exception as e:
            return Response({"message":"error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

