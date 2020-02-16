from django.db import models
from isbn_field import ISBNField

from Book.validators import page_validator, date_validator #book_unique_validator

class Book(models.Model):
    """
        To do:
        -page & date validation(x)
        -convert date from string to date-format and set filters.
    """
    title = models.CharField(max_length=100)    
    publication_date = models.CharField(validators=[date_validator,], max_length=10)
    authors = models.ManyToManyField("Author", related_name="author")
    ISBN = ISBNField() #validators=[book_unique_validator,]
    pages = models.IntegerField(validators=[page_validator,], blank=True)
    language = models.CharField(max_length=4)

    def __str__(self):
        return self.title

    def get_all_authors(self):
        return "".join([x.name.title() +", " for x in self.authors.all()])[:-2]


    class Meta:
        ordering = ["title"] 



class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name.title()

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Author, self).save(*args, **kwargs)



class BookCovers(models.Model):
    """
        To do:
        -set default cover in case of null value inserted to db. (x)
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="covers")
    small_thumbnail= models.URLField(max_length=250, null= True, blank=True, default='https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781442499577/random-9781442499577_hr.jpg')
    big_thumbnail = models.URLField(max_length=250, null= True, blank=True, default='https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781442499577/random-9781442499577_hr.jpg')

    def __str__(self):
        return self.book.title



