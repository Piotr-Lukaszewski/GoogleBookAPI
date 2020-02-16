from rest_framework import serializers
from rest_framework.decorators import api_view

from Book.models import Book, Author, BookCovers




class AuthorSerializer(serializers.ModelSerializer):	

	class Meta:
		model = Author
		fields = ["name"]

class BookCoversSerializer(serializers.ModelSerializer):

	class Meta:
		model = BookCovers
		fields = ["small_thumbnail", "big_thumbnail"]


class BookSerializer(serializers.ModelSerializer):
	authors = AuthorSerializer(many=True, read_only=True)
	covers = BookCoversSerializer(many=True, required=False)

	class Meta:
		model = Book
		fields = ["title", "publication_date", "ISBN", "pages", "language", "authors", "covers"]


@api_view
def preview_response():
	end_point = "https://www.googleapis.com/books/v1/volumes"
	response = requests.get(url=end_point, params={"q":"Hobbit"}).json()
	my_serializer = BookSerializer(data=response, many=True)
	my_serializer.is_valid(True)
	print(my_serializer.data)
	return Response(data=my_serializer.data)




