from django.shortcuts import render
from .models import Book

# Create your views here.

def get_index(request):
    books_items = Book.objects.all()     
    return render(request, "books/index.html", {'books': books_items})
