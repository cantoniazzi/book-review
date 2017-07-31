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
    # imoveis = Imovel.objects.exclude(foto__isnull=True).exclude(foto__exact='')
    # context = {'imoveis': imoveis}
    return render(request, template_name, {})
