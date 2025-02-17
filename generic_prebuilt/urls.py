
# from django.conf import settings
# from django.conf.urls.static import static

from django.urls import path
from .views import MovieListCreateAPI, MovieDetailAPI

urlpatterns = [
    path('movies/', MovieListCreateAPI.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailAPI.as_view(), name='movie-detail'),
]

