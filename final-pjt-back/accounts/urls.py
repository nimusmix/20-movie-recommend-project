from django.urls import path
from . import views

urlpatterns = [
    # 선호장르 리스트 GET
    path('accounts/perferences/', views.perference_list),
    # 선호장르 like의 GET and PUT
    path('accounts/perferences/<str:username>/<int:genre_pk>/', views.user_perference_like),
    # 선호 장르 유저별 GET
    path('accounts/perferences/<str:username>/', views.user_perference),
    # 선호장르 한번에 19개 만들기 POST
    path('accounts/perferences-make/<str:username>/', views.user_perference_make_likes),

    path('accounts/follow/<str:username>/', views.user_follow),
    path('accounts/collect/<int:movie_pk>/', views.user_collect),
    path('accounts/<str:username>/', views.user_detail),
]