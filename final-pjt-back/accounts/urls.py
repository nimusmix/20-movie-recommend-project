from django.urls import path
from . import views

urlpatterns = [
    # 선호 장르 유저별 GET
    path('accounts/perferences/', views.user_perferences),
    # 장르별 조회수 수정
    path('accounts/edit-perferences-score/<int:genre_pk>/', views.edit_perferences_score),
    # 장르별 선호여부 수정
    path('accounts/edit-perferences-like/<int:genre_pk>/', views.edit_perferences_like),
    # 선호장르 한번에 19개 만들기 POST
    path('accounts/make-preferences/', views.make_preferences),
    # 선호장르 리스트 GET
    path('accounts/all-perferences/', views.perferences_list),

    path('accounts/follow/<str:username>/', views.user_follow),
    path('accounts/collect/<int:movie_pk>/', views.user_collect),
    path('accounts/<str:username>/', views.user_detail),
]