from django.urls import path
from . import views

urlpatterns = [
    path('accounts/<str:username>/', views.user_detail),
    path('accounts/follow/<str:username>/', views.user_follow),
    path('accounts/collect/<int:movie_pk>/', views.user_collect),
]