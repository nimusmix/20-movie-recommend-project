from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserSerializer, UserAllSerializer, UserFollowSerializer, UserCollectSerializer
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET'])
def user_detail(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.method == 'GET':
        serializer = UserAllSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserFollowSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def user_follow(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    
    if request.method == 'PUT':
        serializer = UserFollowSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def user_collect(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    
    if request.method == 'PUT':
        serializer = UserCollectSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)