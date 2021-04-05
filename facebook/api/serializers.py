from rest_framework import serializers 
from django.contrib.auth.models import User
from account.models import UserProfile,FriendRequest
from postapp.models import Post,Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username', 'first_name','last_name','password']


class UserSerializerforaccess(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username']
# account serializers
class UserProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer('user.username')
    friends=UserSerializer(many=True, read_only=True)

    class Meta:
        model= UserProfile
        fields=['id','user','dob','gender','profile_pic','profile_cover','friends']

# FriendRequest serializers
class FriendRequestSerializer(serializers.ModelSerializer):
    request_sender=UserSerializerforaccess( read_only=True)
    # request_accepter=UserSerializerforaccess(read_only=True)


    class Meta:
        model=FriendRequest
        fields=['id','request_sender','request_accepter']
    
    # def create(self, validated_data):
    #     return FriendRequest.objects.create(**validated_data)


# Post serializers
class PostSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    liked=UserSerializer(many=True, read_only=True)

    class Meta:
        model=Post
        fields=['id','contain','image','user','liked']

# Comment serializers
class CommentSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model=Comment
        fields=['id','user','post','comment','reply','date']



# # Reply serializers
# class ReplySerializer(serializers.HyperlinkedModelSerializer):
    # user=serializers.ReadOnlyField(source='user.username')
#   

#     class Meta:
#         model=Comment
#         fields=['id','user','post','comment','replies','date']

