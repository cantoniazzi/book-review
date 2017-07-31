from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import BookViewSet, list_table

router = DefaultRouter()
router.register(r'books', BookViewSet)
# router.register(r'table-list/', list_table)

urlpatterns = [
	url(r'^table-list/$', list_table, name='index'),
]