from django.urls import path
from .views import *

app_name = 'feedback'
urlpatterns = [
    # 게시판
    path('community/', feedback_list, name='feedback_list'),
    path('community/create/', feedback_create, name='feedback_create'),
    path('community/<int:pk>/', feedback_detail, name='feedback_detail'),
    path('community/update/<int:pk>', feedback_update, name='feedback_update'),
    path('community/delete/<int:pk>', feedback_delete, name='feedback_delete'),

    # 댓글
    path('comments/create/<int:pk>', comment_create, name='comment_create'),
    path('comments/delete/<int:pk>', comment_delete, name='comment_delete'),

    # 좋아요
    path('like/create/<int:pk>/', like_create, name='like_create'),
    path('like/delete/<int:pk>/', like_delete, name='like_delete'),
]
