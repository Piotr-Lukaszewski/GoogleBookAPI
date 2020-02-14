from django.shortcuts import render, redirect
from rest_framework import mixins
from rest_framework import generics
from django.views.generic import ListView, DetailView, CreateView, View, FormView
from django.urls import reverse_lazy
import requests

from django.conf import settings
from Book.models import Book, Author, BookCovers 
from API.serializers import BookSerializer, AuthorSerializer
from API.forms import GoogleImportForm


class BookListView(generics.ListCreateAPIView):#mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView 
	
	queryset = Book.objects.all()
	serializer_class = BookSerializer



class BookDetailView(generics.RetrieveUpdateDestroyAPIView):# RetrieveAPIView

	queryset = Book.objects.all()
	serializer_class = BookSerializer



class AuthorListView(generics.ListCreateAPIView):#ListCreateAPIView
	
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer



class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer
#generics.CreateAPIView



class GoogleImportBook(FormView):
	model = Book
	form_class = GoogleImportForm
	template_name = "API/search_for_book.html"
	#success_url = reverse_lazy("import_books")	


	def form_valid(self, form):
		search_type = form.cleaned_data['search_type']
		search_type = dict(form.fields['search_type'].choices)[search_type]
		value = str(search_type) + ":" + str(form.cleaned_data["search_phrase"])
		print(value)
		param = {"q":value, "key":settings.API_KEY}
		api_url = "https://www.googleapis.com/books/v1/volumes"
		response = requests.get(url=api_url, params=param)
		items = response.json()["items"]
		for item in items:
			isbn = ""
			for element in item["volumeInfo"]["industryIdentifiers"]: 	
				if element["type"] == "ISBN_13":
					isbn = element["identifier"]
			if isbn == "":
				continue
			if Book.objects.filter(ISBN=isbn).count() > 0:				
				continue
			new_book = Book(
					title=item["volumeInfo"].get("title"),
					publication_date=item["volumeInfo"].get("publishedDate"),
					pages=item["volumeInfo"].get("pageCount", 0),
					language=item["volumeInfo"].get("language"),
					ISBN=isbn
				)
			new_book.save()
			new_cover = BookCovers(book=new_book)
			new_cover.save()
			if "imageLinks" in item["volumeInfo"]:
				new_cover.small_thumbnail = item["volumeInfo"]["imageLinks"].get("smallThumbnail")
				new_cover.big_thumbnail = item["volumeInfo"]["imageLinks"].get("thumbnail")
			new_cover.save()
			if "authors" not in item["volumeInfo"]:
				continue
			for author_name in item["volumeInfo"]["authors"]:
				new_author, created = Author.objects.get_or_create(name=author_name.lower())
				if created:
					new_author.save()
				new_book.authors.add(new_author)
			new_book.save()








		 	# if "ISBN_13" not in item["volumeInfo"]["industryIdentifiers"]:
		 	# 	print("Nie istnieje pole ISBN_13")
		 	# 	print(item["volumeInfo"]["industryIdentifiers"])

		 	#industryIdentifiers for i in industryIdentifiers:;  if i["type"] == "ISBN_13":;     print(i["identifier"])

    # title = models.CharField(max_length=100)    
    # publication_date = models.CharField(max_length=11)
    # pages = models.IntegerField(blank=True)
    # language = models.CharField(max_length=4)

    # authors = models.ManyToManyField("Author", related_name="author")
    # ISBN = ISBNField() 

















		return redirect(reverse_lazy("import_books"))































	# def book_search(self, form)
	# 	#self.kwargs["title"]
	# 	#key = settings.API_KEY
	# 	query_param = {"q": "Tolkien", "key":key}
	# 	api_url = "https://www.googleapis.com/books/v1/volumes"
	# 	response = requests.get(url=api_url, params=query_param)
	# 	items = response.json()["items"]#["volumeInfo"]
	# 	for i in items:
	# 		print(i["volumeInfo"]["title"])
	# 	#print(items["volumeInfo"]["title"])




