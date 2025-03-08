# viewsets.ViewSet (Manual ViewSet)ViewSet	Basic version. You write some logic.

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ViewSet):
    
    """
    A ViewSet for manually handling movie operations.
    """
    
    def list(self, request):  # ✅ GET /movies/
        
        """List all movies."""
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)



    def retrieve(self, request, pk=None):  # ✅ GET /movies/{id}/
        
        
        """Get a single movie by ID."""
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)



    def create(self, request):  # ✅ POST /movies/
        """Create a new movie."""
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def update(self, request, pk=None):  # ✅ PUT /movies/{id}/
        """Update a movie (Full Update)."""
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)

    def partial_update(self, request, pk=None):  # ✅ PATCH /movies/{id}/
        """Update a movie (Partial Update)."""
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)

    def destroy(self, request, pk=None):  # ✅ DELETE /movies/{id}/
        """Delete a movie."""
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({"message": "Movie deleted"}, status=204)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)
