from rest_framework import viewsets

from .models import Book, Cover
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.books_ordered_by_edition()
    serializer_class = BookSerializer
