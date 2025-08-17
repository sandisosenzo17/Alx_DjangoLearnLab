from django.shortcuts import render
from relationship_app.models import Author, Book, Librarian, Library

# Create your views here.
def list_all_books(request):
  #Retrieve all books
  books = Book.objects.select_related.all()

  return render(request, "relationship/list_books.html", {'books': books})

