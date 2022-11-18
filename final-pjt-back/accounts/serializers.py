from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]


class UserAllSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]
        
        
class UserFollowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]
        read_only_fields = ('collection', 'genre_preference', 'using_otts',)
        

class UserCollectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]
        read_only_fields = ('followings', 'genre_preference', 'using_otts',)