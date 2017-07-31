from django.contrib import admin

from .models import Book, Cover


class CoverAdmin(admin.ModelAdmin):

	search_fields = ('type', 'name')
	list_display = ('type', 'name')
	list_filter = ['name']
	save_on_top = True


class BookAdmin(admin.ModelAdmin):

	search_fields = ('name', 'author','isbn')
	list_display = ('name', 'author','isbn','edition')
	list_filter = ['name']
	save_on_top = True

admin.site.register(Cover, CoverAdmin)
admin.site.register(Book, BookAdmin)