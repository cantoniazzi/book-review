import json
import os

from django.conf import settings
from django.contrib.auth.admin import User

from .models import Book, Cover


def create_super_user():
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.com.br'
    superuser.set_password('admin')
    superuser.save()

def import_json_books():
    with open(os.path.join(settings.BASE_DIR, '../database/livros.json')) as json_data:
        return json.load(json_data)


def create_books():
    books_json = import_json_books()

    for book_json in books_json['results']:

        cover = Cover()
        cover.id = None
        cover.name = book_json['cover']['name']
        cover.url = book_json['cover']['url']
        cover.type = book_json['cover']['__type']
        cover.save()

        book = Book()
        book.id = None
        book.cover_file = cover
        book.object_id = book_json['objectId']
        book.name = book_json['name']
        book.author = book_json['author']
        book.curator = book_json['curator']
        book.isbn = book_json['isbn']
        book.edition = book_json['edition']
        book.pages = book_json['pages']
        book.num_ratings = book_json['numRatings']
        book.total_ratings = book_json['totalRatings']
        book.blocked = book_json['blocked']
        book.created_at = book_json['createdAt']
        book.updated_at = book_json['updatedAt']
        book.save()


