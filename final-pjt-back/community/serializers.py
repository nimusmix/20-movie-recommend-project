from rest_framework import serializers
from .models import Movie, Review
# from .serializers import MovieSerializer

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    plus_content = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','user',)
    
    def get_plus_content(self,obj):
        # 현재시간 - 생성시간
	    return (obj.content + 'aaaaaaaaaaaaaaaaaaaa')



class ReviewCustomSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', )
        #read_only_fields = ('movie','user','movie_set','movie_score')

