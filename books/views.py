from django.shortcuts import render, redirect
from .models import Book
from .forms import AddBookForm
from django.http import HttpResponse

# Create your views here.

def get_index(request):
    if request.user.is_authenticated:
        books_items = Book.objects.filter(owner=request.user) 
    else:
        books_items = []
    return render(request, "books/index.html", {'books': books_items})
    
def add_book(request):
    if request.method=="POST":
        form=AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect("/")
    else:
        form = AddBookForm()
    return render(request, 'books/add_book.html', {'form': form})
