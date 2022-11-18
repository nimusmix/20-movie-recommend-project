from rest_framework import serializers
from .models import Movie, Review
from datetime import date, timedelta, datetime, timezone
# from .serializers import MovieSerializer


class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    movie_poster_path = serializers.CharField(source='movie.poster_path', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    last_time = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','user',)
    
    def get_last_time(self, obj):
        ## 어웨어와 네이브 타입 주의!!
        time = datetime.now(timezone.utc) - obj.created_at
        str_time = str(time)
        hour, minute, second = str_time.split(':')
        second = second.split('.')[0]
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        result = ''
        if hour > 24:
            result = f'{hour//24}일 전'
        elif hour >= 1:
            result = f'{hour}시간 전'
        elif minute >= 1:
            result = f'{minute}분 전'
        else:
            result = f'{second}초 전'
        return result


class MovieReviewSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ['review_set']



# class ReviewCustomSerializer(serializers.ModelSerializer):
#     movie_title = serializers.CharField(source='movie.title', read_only=True)
#     username = serializers.CharField(source='user.username', read_only=True)
#     class Meta:
#         model = Review
#         fields = '__all__'
#         read_only_fields = ('user', )
#         #read_only_fields = ('movie','user','movie_set','movie_score')

