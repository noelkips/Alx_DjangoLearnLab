from rest_framework import serializers
from .models import Author, Book
from datetime import date

"""
Serializers:
- BookSerializer: Serializes Book model, includes validation to prevent future publication years.
- AuthorSerializer: Serializes Author model and includes a nested BookSerializer for related books.

Nested Relationships:
- AuthorSerializer uses the related_name 'books' from the Book model to include all books for an author.
"""


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation: Ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: Shows all books for an author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
