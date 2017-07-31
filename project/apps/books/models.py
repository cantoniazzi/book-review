
from collections import OrderedDict

from django.db import models

from .managers import BookManager
from .services import get_book_average_ratting_by_isbn


class Cover(models.Model):

    TYPE_CHOICES = (
        ('File', 'Arquivo'),
        (None, 'Selecione um tipo')
    )

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField('Nome', max_length=200)
    url = models.TextField('Url')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cover'
        verbose_name_plural = 'Covers'
        ordering = ['name', 'url']


class Book(models.Model):

    cover_file = models.OneToOneField(
        Cover,
        verbose_name='Cover',
        related_name='book',
        null=True
    )
    object_id = models.CharField('object_id', max_length=100)
    name = models.CharField('Nome', max_length=200)
    author = models.CharField('Autor', max_length=200)
    isbn = models.CharField('ISBN', max_length=20)
    curator = models.CharField('Curador', max_length=200)
    edition = models.CharField('Edição', max_length=100)
    pages = models.IntegerField(verbose_name='Número de páginas', default=1)
    num_ratings = models.IntegerField(default=1)
    total_ratings = models.IntegerField(default=1)
    blocked = models.BooleanField(blank=True, default=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = BookManager()

    def average_ratting(self):
        result = round((self.total_ratings / self.num_ratings),
                       2) if self.num_ratings > 0 else 0
        return result

    def good_reads_average_ratting(self):
        return get_book_average_ratting_by_isbn(self.isbn)

    def cover(self):
        if self.cover_file:
            return OrderedDict([
                ('__type', self.cover_file.type),
                ('name', self.cover_file.name),
                ('url', self.cover_file.url)])
        return {}

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name', 'author']
