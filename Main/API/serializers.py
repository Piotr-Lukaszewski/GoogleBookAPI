from rest_framework import serializers

from Book.models import Book, Author, BookCovers



# HyperlinkedModelSerializer
# ModelSerializer

class AuthorSerializer(serializers.ModelSerializer):	

	class Meta:
		model = Author
		fields = ["name"]

class BookCoversSerializer(serializers.ModelSerializer):

	class Meta:
		model = BookCovers
		fields = ["small_thumbnail", "big_thumbnail"]


class BookSerializer(serializers.ModelSerializer):
	authors = AuthorSerializer(many=True, read_only=True)# klasy powiazanych serializerow musi sie znajdowac "fizycznie" nad 
	covers = BookCoversSerializer(many=True)

	class Meta:
		model = Book
		fields = ["title", "publication_data", "ISBN", "pages", "language", "authors", "covers"]













