# Using Fully Built Generic Views
# Instead of writing Mixins, we can directly use DRF’s Generic Views.

# 🔥 Replacing RestaurantListCreateAPI with ListCreateAPIView

from .models import Movie
from .serializers import MovieSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# ✅ List all movies & Add new movie
class MovieListCreateAPI(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# ✅ Retrieve, Update & Delete a specific movie
class MovieDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
