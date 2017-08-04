import calendar
import locale

from django.db import models
from django.db.models import Case, When

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class BookManager(models.Manager):

    def books_ordered_by_edition(self):
        abbr_to_num = {name.lower(): num for num,
                       name in enumerate(calendar.month_abbr) if num}
        queryset = super().get_queryset()

        query_sorted = sorted(queryset, key=lambda b: int(
            abbr_to_num[b.edition[:3].lower()]), reverse=True)
        id_list_sorted = [book.id for book in query_sorted]

        edition_year_order = {
            'edition_year_order': "substr(edition, LENGTH(edition)-4, LENGTH(edition))"}
        ids_month_order = Case(*[When(id=id, then=pos)
                                 for pos, id in enumerate(id_list_sorted)])

        sorted_books = super().get_queryset().filter(id__in=id_list_sorted).extra(
            select=edition_year_order).order_by(
            '-edition_year_order',
            ids_month_order)

        return sorted_books
