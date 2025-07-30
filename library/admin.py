from django.contrib import admin
from .models import Book, Borrower

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'book', 'borrowed_date')
