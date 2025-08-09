from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
Book API Views:

- BookListView (ListAPIView): Lists all books. Public access.
- BookDetailView (RetrieveAPIView): Shows details for a single book. Public access.
- BookCreateView (CreateAPIView): Creates a new book. Requires authentication.
- BookUpdateView (UpdateAPIView): Updates an existing book. Requires authentication.
- BookDeleteView (DestroyAPIView): Deletes a book. Requires authentication.

These views use DRF's generic class-based views for CRUD operations.
"""
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
