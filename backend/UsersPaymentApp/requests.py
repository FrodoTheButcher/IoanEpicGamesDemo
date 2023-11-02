from rest_framework import serializers


class AddMoney(serializers.Serializer):
    money = serializers.FloatField(required = True)
        
class RemoveMoney(serializers.Serializer):
    money = serializers.FloatField(required = True)
