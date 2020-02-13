from django.contrib import admin
from Book.models import Book, Author, BookCovers


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookCovers)
