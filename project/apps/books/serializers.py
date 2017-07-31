from rest_framework import serializers

from project.apps.books.models import Book, Cover


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('object_id', 'name', 'author', 'isbn', 'curator', 'cover', 'edition',
                  'pages', 'numRatings', 'totalRatings', 'blocked', 'average_ratting',
                  'good_reads_average_ratting', 'created_at', 'updated_at')
