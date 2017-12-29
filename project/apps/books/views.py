from django.shortcuts import render

from rest_framework import viewsets

from .models import Book, Cover
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.books_ordered_by_edition()
    pagination_class = None
    serializer_class = BookSerializer


def list_table(request):
    template_name = 'books/list.html'
    return render(request, template_name, {})
