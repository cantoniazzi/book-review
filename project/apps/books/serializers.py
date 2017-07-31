from rest_framework import serializers

from project.apps.books.models import Book, Cover


class BookSerializer(serializers.ModelSerializer):

    numRatings = serializers.ReadOnlyField(source='num_ratings')
    totalRatings = serializers.ReadOnlyField(source='total_ratings')
    averageRatting = serializers.SerializerMethodField('get_average_ratting')
    goodReadsAverageRatting = serializers.SerializerMethodField('get_good_reads_average_ratting')

   
    class Meta:
        model = Book
        fields = ('object_id', 'name', 'author', 'isbn', 'curator', 'cover', 'edition',
                  'pages', 'numRatings', 'totalRatings', 'blocked', 'averageRatting',
                  'goodReadsAverageRatting', 'created_at', 'updated_at')

    def get_average_ratting(self, obj):
        return obj.average_ratting()

    def get_good_reads_average_ratting(self, obj):
        return obj.good_reads_average_ratting()