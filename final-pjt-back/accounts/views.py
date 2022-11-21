from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404

from movies.models import Movie, Genre
from accounts.models import Preference
from .serializers import UserSerializer, UserAllSerializer, UserPreferenceDepthSerializer, UserPreferenceSerializer, UserImgSerializer
from .serializers import UserOttSerializer, CollectedUserSerializer

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


# 개인 선호장르 정보를 출력
# 회원가입, 정보수정
@api_view(['GET'])
def user_perferences(request):
    preferences = get_list_or_404(Preference, user=request.user)
    serializer = UserPreferenceDepthSerializer(preferences, many=True)
    return Response(serializer.data)


# 장르별 조회수 수정
@api_view(['PUT'])
def edit_perferences_score(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    preference = get_object_or_404(Preference, user=request.user, genre=genre)
    
    preference.score += 1
    preference.save()

    serializer = UserPreferenceSerializer(preference)
    return Response(serializer.data)


# 장르별 선호여부
@api_view(['PUT'])
def edit_perferences_like(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    preference = get_object_or_404(Preference, user=request.user, genre=genre)
    
    preference.like = request.data['like']
    preference.save()

    serializer = UserPreferenceSerializer(preference)
    return Response(serializer.data)


# 회원가입 시 장르 전체 생성
@api_view(['POST'])
def make_preferences(request):
    genres = get_list_or_404(Genre)
    for genre in genres:
        default_data = {
            'like': 'false', 
            'score': 0
        }
        
        serializer = UserPreferenceSerializer(data=default_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, genre=genre)
            
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def otts(request):
    user = get_object_or_404(get_user_model(), username=request.user)
    serializer = UserOttSerializer(user)
    return Response(serializer.data)


@api_view(['PUT'])
def edit_otts(request, ott_pk):
    user = get_object_or_404(get_user_model(), username=request.user)
    if user.using_otts.filter(pk=ott_pk).exists():
        user.using_otts.remove(ott_pk)
    else:
        user.using_otts.add(ott_pk)
    serializer = UserOttSerializer(user)
    return Response(serializer.data)


@api_view(['PUT'])
def edit_profile_img(request):
    serializer = UserImgSerializer(request.user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

@api_view(['GET'])
def collected_users(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = CollectedUserSerializer(movie)
        return Response(serializer.data)