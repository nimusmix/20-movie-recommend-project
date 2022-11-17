from rest_framework import serializers
from .models import Movie, Genre


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        # fields = ('id', 'title', 'content')
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class MoviePutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('backdrop_path','title','overview','release_date','popularity','poster_path','original_language','original_title','genres','otts')


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

