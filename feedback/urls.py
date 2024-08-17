from django.urls import path
from .views import *

app_name = 'feedback'
urlpatterns = [
    path('community/', feedback_list, name='feedback_list'),
    path('community/create/', feedback_create, name='feedback_create'),
    path('community/delete/<int:pk>/', feedback_delete, name='feedback_delete'),
    path('community/detail/<int:pk>/', feedback_detail, name='feedback_detail'),
    path('edit/<int:pk>/', feedback_edit, name='feedback_edit'),
]
