from django.urls import path
from . import views

urlpatterns = [
    path('accounts/<str:username>/', views.user_detail),
    path('accounts/<str:username>/follow', views.user_follow),
    path('accounts/<str:username>/collect', views.user_collect),
]