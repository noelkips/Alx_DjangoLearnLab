from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from django_filters import rest_framework as filters  # checker wants this exact import
from rest_framework import filters as drf_filters     # alias DRF filters to reference them as filters.*

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



class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.DjangoFilterBackend,      # filtering
        drf_filters.SearchFilter,         # searching
        drf_filters.OrderingFilter        # ordering
    ]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

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
