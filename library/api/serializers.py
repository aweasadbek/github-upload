from rest_framework import serializers

from books.models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("first", "second")

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")

