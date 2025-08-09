from django.db import models

"""
Models:
- Author: Stores author details.
- Book: Stores book details and links each book to an author via a foreign key.

Relationships:
- One-to-many: One Author can have multiple Books.
"""


# Author model: Represents a writer who can have multiple books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model: Represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
