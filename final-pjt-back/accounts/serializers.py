from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Preference, Ott

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]


class UserAllSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]


# 기본 선호 조사, 다수사용
class UserPreferenceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Preference
        fields = '__all__'
        read_only_fields = ('user', 'genre')


# 사용자 모든 선호 장르 출력
# 사용위치 : UserEditView
class UserPreferenceDepthSerializer(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.name', read_only=True)

    class Meta:
        model = Preference
        fields = ['genre', 'score', 'like', 'genre_name']
        # read_only_fields = ('user', 'genre')


# 유저 Ott 조사, 다수 사용
class UserOttSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ott
        fields = '__all__'
        # read_only_fields = ('user', 'genre')