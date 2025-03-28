from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Task, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'username', 'password', 'name', 'is_staff', 'is_superuser'] 
        
