from django_filters import FilterSet
 
from Book.models import Book, Author, BookCovers


class BookFilter(FilterSet):
	#date = DateFromToRangeFilter()

	class Meta:
		model = Book
		fields = {
			"title":["icontains", ], 
			"language":["icontains", ],			
            "authors__name": ["icontains", ],
            "publication_date": [],
		}