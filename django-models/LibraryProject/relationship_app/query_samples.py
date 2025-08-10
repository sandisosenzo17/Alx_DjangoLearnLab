from relationship_app.models import models

#List all books in a library.
library_name = models.Library.objects.create(name="Lib")
models.Library.objects.get(name=library_name)

#Query all books by a specific author.
author = models.Author.objects.create(name="Michio Kaku")
book = models.Book.objects.create(title="The book of Mad Libs", author=author)
book = models.Book.objects.create(title="The Physics of the Impossible", author=author)
books = models.Library.books.all()
_books = models.Book.objects.filter(author__name = author)
#Retrieve the librarian for a library.