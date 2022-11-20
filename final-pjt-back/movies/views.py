from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import MovieSerializer, GenreListSerializer
from .serializers import MoviePkSerializer
from .models import Movie, Genre
from community.models import Review
from accounts.models import Preference


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        print(movies)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         # serializer.save()
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # elif request.method == 'DELETE':
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def genre_list(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data)


# 잠재 모델 기반 추천 알고리즘
@api_view(['GET'])
def user_recommend_movies_latent_model(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    user_preferences = get_list_or_404(Preference, user=user)
    genres = get_list_or_404(Genre)
    score = dict()
    all_score = 0
    # 선호장르와 조회수 점수 구하기
    for user_preference in user_preferences: 
        score[user_preference.genre.pk] = user_preference.score
        if user_preference.like:
            score[user_preference.genre.pk] += 10
        else:
            score[user_preference.genre.pk] += 0
        all_score += score[user_preference.genre.pk]
    
    # 백분율 환산 -> 일단 패스(유의미한지 체크)
    for genre in genres:         
        score[genre.pk] = score[genre.pk]# * 100 // all_score

    # 영화와 비교하기
    movies = get_list_or_404(Movie)
    print('--------------------')
    
    result_movies_score = dict()
    for movie in movies:  # movie 하나를 구해서 
        movie_score = 0
        # 여러 장르를 구한다.
        movie_genres_len = len(movie.genres.values('id'))
        genres = []

        # 점수 = (가중치 // 장르개수) * 장르수
        for value in movie.genres.values('id'): 
            movie_score += (score[value['id']] * 1000) // movie_genres_len
        if movie_score > 0:
            result_movies_score[movie.pk] = movie_score

    # 본 영화 제외하기
    reviews = get_list_or_404(Review, user=user)
    for review in reviews:
        result_movies_score[review.movie.pk] = 0
    result_movies_score = list(result_movies_score.items())
    result_movies_score.sort(key=lambda x:x[1], reverse=True)

    # 20개를 잘라서 pk만 조립한다.
    results = list(map(list, zip(*result_movies_score)))[0][:20]
    
    # Movie모델로 바꿔주는 과정을 거쳐야한다.
    results_movies = list()
    for result in results:
        results_movies.append(Movie.objects.get(pk=result))

    # 결과값이 제대로 나왔음에 환호한다.
    print(results_movies)

    # 결과값 찾아내기
    if request.method == 'GET':
        serializer = MovieSerializer(results_movies, many=True)
        return Response(serializer.data)
    