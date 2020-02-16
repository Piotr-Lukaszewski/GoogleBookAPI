from django.test import TestCase, Client
from django.urls import reverse, resolve

from Book.views import BookAddView
from Book.models import Book, Author, BookCovers


class BookTestCase(TestCase):

    def setUp(self):
        client = Client()
        author_obj = Author.objects.create(
            name="test author"
            ).save()

        book_obj = Book.objects.create(
                title="Test_title",
                publication_date="2019-11-20",
                ISBN="9788381107419",
                pages=295,
                language="en"
            ).save()        

    def test_author_count(self):
        author_count = Author.objects.count()
        self.assertEqual(author_count, 1)

    def test_books_count(self):
        book_count = Book.objects.count()
        self.assertEqual(book_count, 1)

    def test_book_exist(self):
        book_name = Book.objects.last().title
        self.assertEqual(book_name, "Test_title")

    def test_author_name(self):
        author_name = Author.objects.last().name
        self.assertEqual(author_name, "test author")

    def test_url_add_is_revolved(self):
        url = reverse("book_add")
        self.assertEqual(resolve(url).func.view_class, BookAddView)