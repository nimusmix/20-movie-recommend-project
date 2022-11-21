from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Preference, Ott


# 기본 선호 조사, 다수사용
class UserPreferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preference
        fields = '__all__'
        read_only_fields = ('user', 'genre')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]
        depth = 2


class UserAllSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)
    preference_set = UserPreferenceSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        exclude = ['password',]
        depth = 2


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
    # name = serializers.CharField(source='movie.title', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['using_otts',]
        # depth = 2
        # read_only_fields = ('user', 'genre')


class UserImgSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['profile_img',]
        # read_only_fields = ('username', 'followings', )