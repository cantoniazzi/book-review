from django.conf.urls import include, url
from django.contrib import admin

from project.apps.books.urls import router

admin.autodiscover()


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
