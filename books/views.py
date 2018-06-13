from django.shortcuts import render
from .models import Book, Author

# Create your views here.

def get_index(request):
    books_items = Book.objects.all()     
    authors = Author.objects.all()     
    return render(request, "books/index.html", {'books': books_items, 'authors': authors})
