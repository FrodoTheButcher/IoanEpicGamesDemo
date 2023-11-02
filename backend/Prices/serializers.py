from .models import Price
from rest_framework import serializers

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        fiels = '__all__'
        model = Price
    