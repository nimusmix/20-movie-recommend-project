from collections import defaultdict
from operator import itemgetter

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

from .serializers import MovieSerializer, GenreListSerializer, LabelSerializer, MovieSearchSerializer
from .models import Movie, Genre
from community.models import Review
from accounts.models import Preference

from django.db.models import Q

User = get_user_model()


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)


# 잠재 모델 기반 추천 알고리즘
@api_view(['GET'])
def recommend_latent_model(request):
    user_preferences = get_list_or_404(Preference, user=request.user)
    # genres = get_list_or_404(Genre)
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
    # for genre in genres:         
    #     score[genre.pk] = score[genre.pk] * 100 // all_score

    # 영화와 비교하기
    movies = get_list_or_404(Movie)
    
    result_movie_scores = defaultdict(int)
    for movie in movies:  # movie 하나를 구해서
        # 여러 장르를 구한다.
        genres_len = movie.genres.count()

        # 점수 = (가중치 // 장르개수) * 장르수
        genres_id = list(movie.genres.values_list('id', flat=True))
        for genre_id in genres_id:
            result_movie_scores[movie.pk] += (score[genre_id] * 1000) // genres_len

    # 본 영화 제외하기
    # reviews = get_list_or_404(Review, user=request.user)
    reviewed_movies = list(Review.objects.filter(user_id=request.user.id).values_list('movie_id', flat=True))
    for reviewed_movie in reviewed_movies:
        result_movie_scores[reviewed_movie] = 0

    result_movie_scores = list(result_movie_scores.items())
    result_movie_scores.sort(key=lambda x:x[1], reverse=True)

    # 10개를 잘라서 pk만 조립한다.
    results = list(map(list, zip(*result_movie_scores)))[0][:10]
    
    # Movie모델로 바꿔주는 과정을 거쳐야한다.
    results_movies = list()
    for result in results:
        results_movies.append(Movie.objects.get(pk=result))

    serializer = MovieSerializer(results_movies, many=True)
    return Response(serializer.data)


# 유사 사용자 기반 알고리즘
@api_view(['GET'])
def recommend_similar_user(request):
    all_information = []
    not_yet_list = []

    # 로그인한 유저가 리뷰 남긴 영화의 id
    my_review_ids = list(Review.objects.filter(user_id=request.user.id).values_list('movie_id', flat=True))

    # 모든 유저의 id
    user_ids = list(User.objects.values_list('id', flat=True))

    for user_id in user_ids:
        if user_id == request.user.id:
            continue
        
        score = 0
        not_yet = []

        # 해당 유저가 리뷰 남긴 영화의 id
        user_review_ids = list(Review.objects.filter(user_id=user_id).values_list('movie_id', flat=True))
        for user_review_id in user_review_ids:
            if user_review_id in my_review_ids:                                     # 유저가 리뷰 남긴 영화가 내가 리뷰 남긴 영화 리스트에 있으면 점수 올리기
                score += 1
            else:                                                                   # 그렇지 않으면 아직 안 본 영화 리스트에 추가
                not_yet.append(user_review_id)

        all_information.append((score, user_id, not_yet))                           # (점수, 유저, 아직 안 본 영화 리스트)
    all_information = sorted(all_information, reverse=True)[:10]                    # 점수 높은 순으로 정렬하여 10개를 자름.

    not_yet_list = list(map(list, zip(*all_information)))[2]                        # 아직 안 본 영화 리스트만 추출
    not_yet_score_dict = defaultdict(int)
    for not_yet in not_yet_list:                                                    # 아직 안 본 영화가 겹칠 때마다 해당 영화의 id를 key로 하고 value에 +1
        for movie_id in not_yet:
            not_yet_score_dict[movie_id] += 1

    not_yet_score_dict = sorted(not_yet_score_dict.items(), reverse=True, key=itemgetter(1))[:10]
    
    result = []
    for movie_id in not_yet_score_dict:
        movie = get_object_or_404(Movie, pk=movie_id[0])
        result.append(movie)

    serializer = MovieSerializer(result, many=True)
    return Response(serializer.data)


# 선호 장르 추출
@api_view(['GET'])
def recommend_preference_genre(request):
    # 유저 선호 장르를 전체 불러온다.
    user_preferences = Preference.objects.filter(user=request.user).filter(like=True)#.order_by('score')
    # 유저 선호 장르 top 3를 genre.pk 로 가져온다.
    if len(user_preferences[:3]) < 3 :
        user_preferences = Preference.objects.filter(user=request.user).order_by('score')
    prefers_top3 = list(user_preferences[:3].values_list('genre', flat=True))
    print(11)
    # 결과 값 form을 세팅
    result = [
        {
            'label': user_preferences[0].genre.name,
            'movies': [],
            'count': 0,
        },
        {
            'label': user_preferences[1].genre.name,
            'movies': [],
            'count': 0,
        },
        {
            'label': user_preferences[2].genre.name,
            'movies': [],
            'count': 0,
        }
    ]
    movies = Movie.objects.all()
    # 장르당 10개씩만 구함
    for movie in movies:
        for idx, prefer in enumerate(prefers_top3):
            if result[idx]['count'] < 10:
                if(movie.genres.filter(pk=prefer)):
                    result[idx]['movies'].append(movie)
                    result[idx]['count'] += 1
    
    # Json 추출
    serializer = LabelSerializer(result, many=True)
    return Response(serializer.data)


# 검색
@api_view(['GET'])
def movie_search(request, movie_title):
    movies = []
    try:
        movies.append(Movie.objects.get(title=movie_title))
    except:
        pass
    movies.extend((Movie.objects.filter(title__contains=movie_title) & Movie.objects.exclude(title=movie_title))[:5])
    serializer = MovieSearchSerializer(movies, many=True)
    return Response(serializer.data)