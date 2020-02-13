from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics

import json
import requests

from Book.models import Book, Author 
from API.serializers import BookSerializer, AuthorSerializer


class BookListView(generics.ListCreateAPIView):#mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView 
	
	queryset = Book.objects.all()
	serializer_class = BookSerializer



class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer



class AuthorListView(generics.ListCreateAPIView):
	
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer



class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer




class GoogleImportBook(generics.CreateAPIView):
	#self.kwargs['title']
	#settings.API_KEY
	query_param = {"q": "Tolkien"}
	api_url = "https://www.googleapis.com/books/v1/volumes"
	response = requests.get(url=api_url, params=query_param)
	items = response.json()['items']
# 	for i in items:
# 		print(i['volumeInfo']['title'])
# 	#print(items["volumeInfo"]["title"])