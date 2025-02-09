from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



    def validate(self, data):
            """Check if the book already exists before saving"""
            title = data.get('title')
            author = data.get('author')
            published_date = data.get('published_date')

            # Check if a book with the same details already exists
            if Book.objects.filter(title=title, author=author, published_date=published_date).exists():
                raise serializers.ValidationError("This book already exists!")

            return data