from django.urls import path
from . import views

app_name = 'wtp'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('gender/<int:emotion_index>/', views.Gender.as_view(), name="gender"),
    path('gender/<int:emotion_index>/age/<int:gender_index>/', views.Age.as_view(), name="age"),
    path('gender/<int:emotion_index>/age/<int:gender_index>/book/<int:age_index>/', views.Book.as_view(), name="book"),
]
