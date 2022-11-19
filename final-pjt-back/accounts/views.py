from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404

from movies.models import Movie, Genre
from accounts.models import Preference
from .serializers import UserSerializer, UserAllSerializer, UserPreferenceDepthSerializer, UserPreferenceSerializer
from .serializers import UserOttSerializer

# Create your views here.
@api_view(['GET'])
def user_detail(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.method == 'GET':
        serializer = UserAllSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
def user_follow(request, username):
    target = get_object_or_404(get_user_model(), username=username)

    if target != request.user:
        if target.followers.filter(pk=request.user.pk).exists():
            target.followers.remove(request.user)
        else:
            target.followers.add(request.user)

    serializer = UserAllSerializer(target)
    return Response(serializer.data)


@api_view(['POST'])
def user_collect(request, movie_pk):
    target = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), username=request.user.username)
    
    if user.collection.filter(pk=movie_pk).exists():
        user.collection.remove(target)
    else:
        user.collection.add(target)
        
    serializer = UserSerializer(user)
    return Response(serializer.data)


# 선호 정보를 전부 출력
# 선호도 관계조사
# 아직안쓰임
@api_view(['GET'])
def perference_list(request):
    preferences = get_list_or_404(Preference)
    if request.method == 'GET':
        serializer = UserPreferenceSerializer(preferences, many=True)
        return Response(serializer.data)


# 개인 선호장르 정보를 출력
# 회원가입, 정보수정
@api_view(['GET'])
def user_perference(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    preferences = get_list_or_404(Preference, user=user)

    if request.method == 'GET':
        serializer = UserPreferenceDepthSerializer(preferences, many=True)
        return Response(serializer.data)



# 유저당 선호장르 수정
# 회원가입, 정보수정, 조회수, 선호 점수 수정
@api_view(['GET', 'PUT'])
def user_perference_like(request, username, genre_pk):
    user = get_object_or_404(get_user_model(), username=username)
    genre = get_object_or_404(Genre, pk=genre_pk)

    if request.method == 'GET':
        preferences = get_object_or_404(Preference, user=user, genre=genre)
        serializer = UserPreferenceSerializer(preferences)
        return Response(serializer.data)
    if request.method == 'PUT':
        preferences = get_object_or_404(Preference, user=user, genre=genre)
        serializer = UserPreferenceSerializer(preferences, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 회원가입 시 장르 전체 생성
@api_view(['POST'])
def user_perference_make_likes(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    genres = get_list_or_404(Genre)
    
    for genre in genres:
        default_data = {
            'user': f'{user.pk}', 
            'genre': f'{genre.pk}', 
            'like': 'false', 
            'score': 0
        }
        serializer = UserPreferenceSerializer(data=default_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, genre=genre)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


    