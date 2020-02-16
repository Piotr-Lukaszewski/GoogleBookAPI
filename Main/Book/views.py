from django.views.generic import ListView, DetailView, CreateView, View, FormView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from Book.forms import BookForm, AuthorForm, CoversForm
from Book.models import Book, Author, BookCovers
from Book.filters import BookFilter

def homeviewfunc(request, *args, **kwargs):
    return render(request, "home.html", {})


class HomeView(View):
    template_name = "home.html"



class BookListView(ListView, SuccessMessageMixin):
    model = Book
    template_name = "Books/books_list.html"
    context_object_name = "object" 
    #paginate_by = 5
    filterset_class = BookFilter
    


    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)     
        msg_storage = messages.get_messages(self.request)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())        
        context['message'] = msg_storage
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "Books/detail_view.html"


class BookAddView(FormView):
    model = Book
    template_name = "Books/create_book.html"    
    form_class = BookForm
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):    
        if Book.objects.filter(ISBN=form.cleaned_data["ISBN"]).count() > 0:#title
            messages.warning(self.request, f'Book "{form.cleaned_data["ISBN"]}" already exist in database.')
            return redirect("book_details", pk=Book.objects.get(ISBN=form.cleaned_data["ISBN"]).pk)
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
            pk = new_book.pk
            return redirect("covers_add", pk=pk)#
           

class AddAuthorView(FormView):
    model = Author
    template_name = "Books/add_author.html"
    success_url = reverse_lazy("book_list")
    form_class = AuthorForm

    def form_valid(self, form):# form_valie
        if Author.objects.filter(name=form.cleaned_data["name"].lower()).count() > 0:
            messages.warning(self.request, f'Author "{form.cleaned_data["name"].lower()}" already exist in database.')
        else:
            new_author = Author(name=form.cleaned_data["name"])
            new_author.save()
        return redirect(reverse_lazy("book_add"))
        
        
class AddBookCoverView(FormView):
    model = BookCovers
    template_name = "Books/add_covers.html"
    success_url = reverse_lazy("book_list")
    form_class = CoversForm

    def form_valid(self, form):
        new_book = Book.objects.get(pk=self.kwargs["pk"])
        new_covers, status = BookCovers.objects.get_or_create(book=new_book)
        new_covers.small_thumbnail = form.cleaned_data["small_thumbnail"]
        new_covers.big_thumbnail = form.cleaned_data["big_thumbnail"]
        new_covers.save()
        return redirect("book_details", pk=self.kwargs['pk'])












