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



# ListView – All users can view books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only for everyone

# DetailView – All users can view a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# CreateView – Only authenticated users can create
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# UpdateView – Only authenticated users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# DeleteView – Only authenticated users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
