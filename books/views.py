from django.shortcuts import render, redirect
from .models import Book
from .forms import AddBookForm
from django.http import HttpResponse

# Create your views here.

def get_index(request):
    books_items = Book.objects.all()     
    return render(request, "books/index.html", {'books': books_items})
    
def add_book(request):
    if request.method=="POST":
      form=AddBookForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
      return redirect("/")
    else:
        form = AddBookForm()
    return render(request, 'books/add_book.html', {'form': form})
