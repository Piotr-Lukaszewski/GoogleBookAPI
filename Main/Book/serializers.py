from rest_framework import serializers

from Book.models import Book, Author



# HyperlinkedModelSerializer
# ModelSerializer

class AuthorSerializer(serializers.ModelSerializer):	

	class Meta:
		model = Author
		fields = ["name"]

class BookSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(read_only=True, many=True)# klasy powiazanych serializerow musze sie znajdowac "fizycznie" nad

	class Meta:
		model = Book
		fields = ["title", "publication_data", "ISBN", "pages", "cover_addres", "language", "author"]













