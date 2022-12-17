from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('genres/', views.genre_list),
    # # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # 잠재 모델 기반 추천 알고리즘
    path('recommend/latent/', views.recommend_latent_model),

    # 유사 사용자 기반 알고리즘
    path('recommend/similar/', views.recommend_similar_user),

    # 사용자 선호장르 추천
    path('recommend/preference/', views.recommend_preference_genre),

    # 카테고리view에서 검색
    path('movies-search/<str:movie_title>/', views.movie_search),
]
