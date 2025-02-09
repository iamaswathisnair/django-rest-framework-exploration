from django.shortcuts import render  ,get_object_or_404
from rest_framework.views import APIView
from .models import Book
from  . serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()   # Get ALL books 📚
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)   # Create a new book 🆕
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
#-----------------------------------------#
class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)  # Get ONE book by ID
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)  # Update ONE book by ID
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)  # Partially update ONE book
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)  # Delete ONE book by ID
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
