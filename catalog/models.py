from django.db import models


# Create your models here.
class Genere(models.Model):
    """model representing a book genere"""
    name = models.CharField(max_length = 200, help_text = "Enter a book Genere")
    def __str__(self):
        """string representing the model object"""
        return self.name
    objects = models.Manager()


from django.urls import reverse

class Book(models.Model):
    """Model representing a book but not specefic copy of a book"""
    title = models.CharField(max_length = 200)

    #Foreign key can be used because book can have only one author, but author can have multiple genere
    #Author as a string rather than object because it hasn't been declared yet in the program
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
    summary = models.CharField(max_length = 200, help_text = "enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length = 13, help_text = '13 character<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    objects = models.Manager()
    #ManyToMany field is used because genere can contain many books, books can cover many generes
    #Genere model as already declared as object so we can specify the object above
    genere = models.ManyToManyField(Genere, help_text = "select genere for this book")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])
    def display_genere(self):
        """create a string for a genere . This is requred dislay genere in admin"""
        return ', '.join(genere.name for genere in self.genere.all()[:3])
    display_genere.short_description = 'Genere'


import uuid

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    book = models.ForeignKey('book', on_delete = models.SET_NULL, null = True)
    imprint = models.CharField(max_length = 200)
    due_back = models.DateField(null = True, blank = True)

    LOAN_STATUS = (
        ('m', 'Maintance'),
        ('o', 'on loan'),
        ('a', 'available'),
        ('r', 'reserved'),
    )
    status = models.CharField(
        max_length = 1,
        choices = LOAN_STATUS,
        blank = True,
        default = 'm',
        help_text = ' book availability',
    )
    class Meta:
        ordering = ['due_back']
    def __str__(self):
        """string for representing object model"""
        return f'{self.id} ({self.book.title})'
    objects = models.Manager()
class Author(models.Model):
    """model representing an author"""
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    date_of_birth = models.DateField('DOB',null = True, blank =True)
    date_of_death = models.DateField('Died', null = True, blank = True)

    class Meta:
        ordering = ['last_name', 'first_name']
    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])
    def __str__(self):
        """string for representing the model object."""
        return f'{self.last_name}, {self.first_name}'
    
    objects = models.Manager()