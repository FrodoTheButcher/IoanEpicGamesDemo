from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Profile
class UserSerializer(serializers.ModelSerializer):
    money = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['email','username','password','money']
    
    def get_money(request,obj):
        try:
            return obj.profile.accountMoney
        except Profile.DoesNotExist as e:
            return 0
            

    
    def create(self, validated_data):

        password2 = self.context.get("password2")
        if validated_data['password'] != password2:
            raise serializers.ValidationError("Passwords do not match")
        
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['username'] = validated_data['email']
        
        return super().create(validated_data)

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'is_superuser', 'is_active']

   