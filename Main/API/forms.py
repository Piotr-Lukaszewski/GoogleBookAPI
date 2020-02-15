from django import forms

from Book.models import Book, Author, BookCovers
searching_types = (
		("1", "q"),
		("2", "intitle"),
		("3", "inauthor"),
		("4", "inpublisher"),
		("5", "subject"),
		("6", "isbn"),
		("7", "lccn"),
		("8", "oclc")
	)

class GoogleImportForm(forms.Form):
	
	search_phrase = forms.CharField()
	search_type = forms.ChoiceField(choices=searching_types, widget=forms.Select(), required=True)
	class Meta:
		model = Book
		fields=["search_phrase", "search_type"]


