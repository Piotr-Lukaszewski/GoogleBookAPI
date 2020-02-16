from django.contrib import admin
from django.urls import path

from API import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name="books_api"),
    path('books/<int:pk>', views.BookDetailView.as_view()),
    # path('authors/', views.AuthorListView.as_view()),
    # path('authors/<int:pk>', views.AuthorDetailView.as_view()),
    path('new/', views.GoogleImportBook.as_view(), name="import_books"),    
]