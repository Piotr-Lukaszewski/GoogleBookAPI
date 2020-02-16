from django_filters import FilterSet
 
from Book.models import Book, Author, BookCovers


class BookFilter(FilterSet):

	class Meta:
		model = Book
		fields = {
			"title":["icontains", ], 
			"language":["icontains", ],			
            "authors__name": ["icontains", ],
            "publication_date": ["icontains", ],
		}