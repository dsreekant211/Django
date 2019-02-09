from django.contrib import admin
from catalog.models import Author, Genere, Book, BookInstance

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genere)
#admin.site.register(BookInstance)
# Define the admin class 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# Register the admin class with the associatef model
admin.site.register(Author, AuthorAdmin)
#Register the Admin classes for book using the decorator
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genere')
    inlines = [BookInstanceInline]

#Register the Admin classes for book using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')
    
    fieldsets = (
        ('Details', {
            "fields": (
                'book', 'imprint', 'id'
            ),
        }),
        ('Availability', {
            'fields' : ('status', 'due_back')
        })
    )
    


