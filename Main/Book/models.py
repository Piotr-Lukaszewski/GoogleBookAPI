from django.db import models
from isbn_field import ISBNField

class Book(models.Model):
    title = models.CharField(max_length=100)    
    publication_date = models.CharField(max_length=11)
    authors = models.ManyToManyField("Author", related_name="author")
    ISBN = ISBNField() 
    pages = models.IntegerField(blank=True)
    language = models.CharField(max_length=4)

    def __str__(self):
        return self.title

    def get_all_authors(self):
        return "".join([x.name +", " for x in self.authors.all()])[:-2]


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
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="covers")
    small_thumbnail= models.URLField(max_length=250, null= True, blank=True)
    big_thumbnail = models.URLField(max_length=250, null= True, blank=True)

    def __str__(self):
        return self.book.title



