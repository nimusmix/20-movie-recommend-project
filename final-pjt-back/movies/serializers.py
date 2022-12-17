from rest_framework import serializers

from .models import Movie, Genre


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class TestSerializer(serializers.Serializer):
    label = serializers.CharField()
    movies = MovieSerializer(many=True, read_only=True)


class MovieSearchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['id','title']