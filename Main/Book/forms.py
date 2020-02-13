from django import forms
from isbn_field import ISBNField
from Book.models import Book, Author
from django.shortcuts import get_object_or_404



class BookForm(forms.ModelForm): #forms.Form
    title = forms.CharField()
    publication_date = forms.CharField()
    authors = forms.ModelMultipleChoiceField(Author.objects.all())
    ISBN = ISBNField()
    pages = forms.IntegerField()
    language = forms.CharField()

    
    class Meta:
        model = Book
        fields = ["title", "publication_date", "authors", "ISBN", "pages", "language"]



    


  