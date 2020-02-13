from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Book.forms import BookForm
from Book.models import Book, Author


def homeviewfunc(request, *args, **kwargs):
    return render(request, "home.html", {})


class HomeView(View):
    template_name = "home.html"



class BookListView(ListView):
    model = Book
    template_name = "Books/books_list.html"
    context_object_name = "object" #by default it's object_list 
    paginate_by = 2

    def get_context_data(self, **kwargs):      
        msg_storage = messages.get_messages(self.request)
        context = super().get_context_data(**kwargs)
        context['message'] = msg_storage
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "Books/detail_view.html"


class BookAddView(FormView):
    model = Book
    template_name = "Books/create_view.html"    
    form_class = BookForm
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        if Book.objects.filter(title=form.cleaned_data["title"].lower()).count() > 0:
            messages.warning(self.request, f'Book "{form.cleaned_data["title"].lower()}" already exist in database.')
        else:
            new_book = Book(
                    title=form.cleaned_data["title"].lower(),
                    publication_date=form.cleaned_data['publication_date'],
                    ISBN=form.cleaned_data["ISBN"],
                    pages=form.cleaned_data["pages"],
                    language=form.cleaned_data["language"]
                )
            authors = Author.objects.filter(pk__in=form.cleaned_data["authors"])
            new_book.save()
            for author in authors:
                new_book.authors.add(author)
            new_book.save()
        return redirect(reverse_lazy("book_list"))
















