from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    """
    Authentication:
    - Uses DRF TokenAuthentication.
    - Obtain token via POST to /api/auth/token/ with username/password.

    Permissions:
    - Global: IsAuthenticated (set in settings.py).
    - BookViewSet: Requires authentication for all CRUD operations.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only logged-in users can access

