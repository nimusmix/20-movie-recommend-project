from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404

from accounts.serializers import UserSerializer
from .serializers import ReviewSerializer, MovieReviewSerializer
from .models import Movie, Review

User = get_user_model()

@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        # reviews = Review.objects.all()
        reviews = get_list_or_404(Review)
        reviews.reverse()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # review = Review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_reviews(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        serializer = MovieReviewSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
def get_similar_user(request):
    all_information = []

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

    similar_user_list = list(map(list, zip(*all_information)))[1]
 
    result = []
    for user_id in similar_user_list:
        user = get_object_or_404(User, pk=user_id)
        result.append(user)

    serializer = UserSerializer(result, many=True)
    return Response(serializer.data)