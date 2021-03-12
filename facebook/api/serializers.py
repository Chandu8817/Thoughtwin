from rest_framework import serializers 
from postapp.models import UserPost

class UserPostSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    postcontain=serializers.CharField(required=False,allow_blank=True,max_length=500)
    postimage=serializers.ImageField(required=False)