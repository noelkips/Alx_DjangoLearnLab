from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old read-only list view (optional, can be removed)
    path('books/', BookList.as_view(), name='book-list'),

    # Router-generated CRUD URLs
    path('', include(router.urls)),
]
