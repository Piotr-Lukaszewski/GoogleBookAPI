from django.contrib import admin
from django.urls import path

from Book import views

urlpatterns = [
    path("Book_list/", views.BookListView.as_view(), name="book_list"),
    path("Book_list/<int:pk>", views.BookDetailView.as_view(), name="book_details"),
    path("Book_list/add", views.BookAddView.as_view(), name="book_add"),
    path("Book_list/add_author", views.AddAuthorView.as_view(), name="author_add"),
    #path("Book_list/add/cover<int:pk>", views.create_book_cover, name="covers_add")
    path("Book_list/add/cover<int:pk>", views.AddBookCoverView.as_view(), name="covers_add"),
]