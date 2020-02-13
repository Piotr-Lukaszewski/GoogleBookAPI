from django.contrib import admin
from django.urls import path

from Book import views

urlpatterns = [
    path("Book_list/", views.BookListView.as_view(), name="book_list"),
    path("Book_list/<int:pk>", views.BookDetailView.as_view(), name="book_details"),
    path("Book_list/add", views.BookAddView.as_view(), name="book_add"),
]