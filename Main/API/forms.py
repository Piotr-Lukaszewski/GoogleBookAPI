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

# q - Search for volumes that contain this text string. There are special keywords you can specify in the search terms to search in particular fields, such as:
# intitle: Returns results where the text following this keyword is found in the title.
# inauthor: Returns results where the text following this keyword is found in the author.
# inpublisher: Returns results where the text following this keyword is found in the publisher.
# subject: Returns results where the text following this keyword is listed in the category list of the volume.
# isbn: Returns results where the text following this keyword is the ISBN number.
# lccn: Returns results where the text following this keyword is the Library of Congress Control Number.
# oclc: Returns results where the text following this keyword is the Online Computer Library Center number.
