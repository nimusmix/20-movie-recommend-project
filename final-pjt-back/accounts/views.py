from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserAllSerializer
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET', 'DELETE', 'PUT'])
def user_detail(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.method == 'GET':
        serializer = UserAllSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserAllSerializer(get_user_model(), data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)