from rest_framework import serializers
from rest_framework.decorators import api_view

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










	# def book_search(self, form)
	# 	#self.kwargs['title']
	# 	#key = settings.API_KEY
	# 	query_param = {"q": "Tolkien", "key":key}
	# 	api_url = "https://www.googleapis.com/books/v1/volumes"
	# 	response = requests.get(url=api_url, params=query_param)
	# 	items = response.json()['items']#["volumeInfo"]
	# 	for i in items:
	# 		print(i['volumeInfo']['title'])
	# 	#print(items["volumeInfo"]["title"])