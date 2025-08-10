from django.shortcuts import render
from relationship_app.models import Author, Book, Librarian, Library
from django.http import HttpResponse

# Create your views here.
def list_all_books(request):
  #Retrieve all books
  books = Book.objects.all()

  lines = []

  #Prepare a view in a list form
  for book in books:
    author = book.author.name
    line = book.title + " by " + author
    lines.append(line)

  if lines:
    response_text = "\n".join(lines)
  else:
    response_text = "No books found"
  
  return HttpResponse(response_text, content_type="text/plain")