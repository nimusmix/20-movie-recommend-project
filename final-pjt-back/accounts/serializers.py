from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Preference, Genre

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]


class UserAllSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]

class PreferenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Preference
        fields = '__all__'
        read_only_fields = ('user', 'genre')


class UserPreferenceSerializer(serializers.ModelSerializer):
    # genre_preference를 쓰지않고 set을 사용하여 확인하는 것이 더 잘되었다.
    preference_set =  PreferenceSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = '__all__'
        depth = 2


class PreferenceMakeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Preference
        fields = '__all__'

