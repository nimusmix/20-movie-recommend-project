from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404

from movies.models import Movie
from .serializers import UserSerializer, UserAllSerializer

# Create your views here.
@api_view(['GET'])
def user_detail(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.method == 'GET':
        serializer = UserAllSerializer(user)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT'])
def user_follow(request, username):
    target = get_object_or_404(get_user_model(), username=username)

    if target != request.user:
        if target.followers.filter(pk=request.user.pk).exists():
            target.followers.remove(request.user)
        else:
            target.followers.add(request.user)

    serializer = UserAllSerializer(target)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def user_collect(request, movie_pk):
    target = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), username=request.user.username)
    
    if user.collection.filter(pk=movie_pk).exists():
        user.collection.remove(target)
    else:
        user.collection.add(target)
        
    serializer = UserSerializer(user)
    return Response(serializer.data)