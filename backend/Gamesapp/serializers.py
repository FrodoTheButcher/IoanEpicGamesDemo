
from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Game

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag


class CustomGameSerializer(serializers.ModelSerializer):
    gameTags = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = Game
    
    def get_gameTags(self,obj):
        gameTagsArray = obj.tags.all()
        gameTagsSerialized = TagsSerializer(gameTagsArray,many=True)
        return gameTagsSerialized.data


    
