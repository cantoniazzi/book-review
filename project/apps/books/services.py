import requests

from django.conf import settings


def get_book_average_ratting_by_isbn(isbn):
    url = 'https://www.goodreads.com/book/review_counts.json'
    params = {'key': settings.GOOD_READS_API_KEY, 'isbns': isbn}
    return_json = requests.get(url, params=params)

    if return_json.status_code == requests.codes.ok:
        book = return_json.json()
        average_ratting = book['books'][0]['average_rating']
        return average_ratting
    return ''
