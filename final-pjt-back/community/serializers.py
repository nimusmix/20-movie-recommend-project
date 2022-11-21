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
        ## 속성이 days와 seconds존재, hours... 없음!!
        time = datetime.now(timezone.utc) - obj.created_at
        result = ''
        days = time.days
        hours = time.seconds // 3600
        minutes = time.seconds // 60
        seconds = time.seconds % 60

        if time.days >= 30:
            result = f'{days // 31}달 전'
        elif time.days >= 1:
            result = f'{days}일 전'
        elif hours >= 1:
            result = f'{hours}시간 전'
        elif minutes >= 1:
            result = f'{minutes}분 전'
        else:
            result = f'{seconds}초 전'
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

